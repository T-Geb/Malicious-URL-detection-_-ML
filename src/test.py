from features import get_url_length, count_digits, count_other_special_chars, equals_count, question_count, hyphen_count, count_suspicious, get_full_domain, domain_is_ip, count_nums_in_domain, get_suffix, suspicious_suffix
import pandas as pd  # For working with DataFrame


##Debug Tests

def feature_function_testing():
    test_urls = [
        "https://www.google.com",
        "https://www.alsothecrumbsplease.com/authentic-black-forest-cake",
        "http://sample.info/?drain=mine&direction=lock#cable",
        "http://bank-confirm.com/login",
        "https://www.sample.edu/?query.8"
    ]

    for url in test_urls:
        print(f"URL: {url}")
        print("URL Length:", get_url_length(url))
        print("Digit Count:", count_digits(url))
        print("Special char count:", count_other_special_chars(url))
        print("Equals sign count:", equals_count(url))
        print("Question mark count:", question_count(url))
        print("Hyphen count:", hyphen_count(url))
        print("Suspicious keyword count:", count_suspicious(url))
        print("get_domin:", get_full_domain(url))
        print("Domain is IP?:", domain_is_ip(url))
        print("is domain number:", count_nums_in_domain(url))
        print("Domain Suffix: ", get_suffix(url)) #nothing being returned
        print("Suspicious suffix :", suspicious_suffix(url))

        print("-" * 50)


def balanced_train_test_split_test(y_train, y_test,x_train, x_test,le):

    #replaced manual mapping dictionary with the le dictionary for test print
    le_dict = dict(enumerate(le.classes_))

    train_dist = pd.Series(y_train).value_counts().sort_index().rename(index=le_dict)
    test_dist = pd.Series(y_test).value_counts().sort_index().rename(index=le_dict)
    
    print("\nTrain set class distribution:\n")
    print(train_dist.to_string())
    
    print("\n\nTest set class distribution:\n")
    print(test_dist.to_string())
    
    print("\nTotal rows in train set:", len(x_train))
    print("Total rows in test set:", len(x_test))


def apply_feature_to_df_test(x_train_df, x_test_df):

    
    print("\nFirst 5 rows of the extracted features for x_train \n")
    print(x_train_df.head(5).to_string())

    print("\n\nFirst 5 rows of the extracted features for x_test \n")
    print(x_test_df.head(5).to_string())


    