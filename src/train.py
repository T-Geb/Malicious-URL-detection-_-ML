import pandas as pd  # For working with DataFrame
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
from sklearn.model_selection import train_test_split  #To split data into train and test sets
from sklearn.preprocessing import StandardScaler # For scaling Logistic Regression features
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import HistGradientBoostingClassifier 


def split_train_test(x,y):

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2,random_state = 42,stratify=y)
    # label_mapping = {0: 'Benign', 1: 'Defacement', 2: 'Malware', 3: 'Phishing'}

    return x_train, x_test, y_train, y_test

def build_feature_row(url):  #adding build feature row to be used to apply features and also return extracted features
    return {
        'url_length':           get_url_length(url),
        'digit_counts':         count_digits(url),
        'equals_count':         equals_count(url),
        'question_count':       question_count(url),
        'hyphen_count':         hyphen_count(url),
        'count_special_chars':  count_other_special_chars(url),
        'https_check':          https_check(url),
        'count_nums_in_domain': count_nums_in_domain(url),
        'domain_is_ip':         domain_is_ip(url),
        'suspicious_suffix':    suspicious_suffix(url),
        'count_suspicious':     count_suspicious(url),
    }
    
def apply_features_to_df(x_train,x_test):
    #creating a data frame for x_train and x_test and adding the feature extractions as columns in the dataframe
    # Used the pandas library to create the dataframes and apply the methods.

    x_train_df = pd.DataFrame(x_train.apply(build_feature_row).tolist())
    x_test_df = pd.DataFrame(x_test.apply(build_feature_row).tolist())

    
    return x_train_df, x_test_df



def train_models(x_train_df, y_train):
    models = {
        "random_forest": RandomForestClassifier(random_state=42),
        "hist_gradient_boosting": HistGradientBoostingClassifier(random_state=42),
        "logistic_regression": Pipeline([
            ("scaler", StandardScaler()),  #scaling features to treat features equally with logistic regression
            ("model", LogisticRegression(random_state=42))
        ])
    }

    for model in models.values():
        model.fit(x_train_df, y_train)

    return models



