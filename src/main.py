from pathlib import Path
import pandas as pd

from preprocessing import (
    load_dataset,
    duplicate_url_check,
    remove_if_duplicate,
    check_for_missing_vals,
    drop_missing_val_rows,
    balance_dataset,
    label_encoding,
)
from train import split_train_test, build_feature_row, apply_features_to_df, train_models
from predict import (
    model_predict,
    model_eval,
    classification_report_plot,
    confusion_matrix_plot,
)
from test import balanced_train_test_split_test, apply_feature_to_df_test
from features import (
    get_url_length,
    count_digits,
    equals_count,
    question_count,
    hyphen_count,
    count_other_special_chars,
    https_check,
    count_nums_in_domain,
    domain_is_ip,
    suspicious_suffix,
    count_suspicious,
)

DATASET_URL = str(Path(__file__).resolve().parents[1] / "data" / "trimmed_dataset.csv")
SHOW_PLOTS = False
SHOW_UI = True


def run_url_checker(random_forest_model,le):
    print("\n" + "="*60)
    print("         URL Safety Checker")
    print("="*60)
    print("\nEnter a URL to check, a sample number, or 'q' to quit.")

    while True:
        print("\n" + "-"*60)
        url = input("Enter URL or sample #: ").strip()

        if not url:
            print("Please enter a URL.")
            continue

        if url.lower() == 'q':
            print("\nProgram Exited.")
            break

        extracted_features = pd.DataFrame([build_feature_row(url)]) 

        prediction = random_forest_model.predict(extracted_features)[0]
        
        GREEN = "\033[92m"
        RED = "\033[91m"
        RESET = "\033[0m"
        
        label = le.inverse_transform([prediction])[0]
        
        if label == "benign":
            colored_label = f"{GREEN}Benign — Safe{RESET}"
        elif label == "defacement":
            colored_label = f"{RED}Malicious — Possible Defacement{RESET}"
        elif label == "malware":
            colored_label = f"{RED}Malicious — Possible Malware{RESET}"
        elif label == "phishing":
            colored_label = f"{RED}Malicious — Possible Phishing{RESET}"
            
        print(f"\n{'>'*10} URL Safety Prediction {'<'*10}")
        print(f"URL:        {url.replace('://', '://\u200b')}")
        print(f"Prediction: {colored_label}")


def main():
    # Load the dataset, remove duplicates, and drop missing rows.
    mal_ds = load_dataset(DATASET_URL)
    total_dupes = duplicate_url_check(mal_ds)
    mal_dups_removed = remove_if_duplicate(mal_ds, total_dupes)

    missing_counts = check_for_missing_vals(mal_dups_removed)
    mal_ds_cleaned = drop_missing_val_rows(mal_dups_removed, missing_counts)

    # Balance class counts and label-encode target values.
    x_urls, y_labels = balance_dataset(mal_ds_cleaned)
    y, le = label_encoding(y_labels)

    # Split data and transform URLs into model features.
    x_train, x_test, y_train, y_test = split_train_test(x_urls, y)
    balanced_train_test_split_test(y_train, y_test, x_train, x_test, le)

    x_train_df, x_test_df = apply_features_to_df(x_train, x_test)
    apply_feature_to_df_test(x_train_df, x_test_df)

    # Train all configured models on extracted features.
    models = train_models(x_train_df, y_train)

    # Evaluate each model on the held-out test set.
    for model_name, model in models.items():
        print(f"\n{'=' * 30}")
        print(f"Evaluating: {model_name}")
        print(f"{'=' * 30}")

        y_prediction = model_predict(model, x_test_df)
        model_eval(y_test, y_prediction)
        classification_report_plot(y_test, y_prediction, le)

        if SHOW_PLOTS:
            print(confusion_matrix_plot(y_test, y_prediction, le))

    # Launch the URL checker
    if SHOW_UI:
        random_forest_model = models.get("random_forest")
        run_url_checker(random_forest_model,le)


if __name__ == "__main__":
    main()