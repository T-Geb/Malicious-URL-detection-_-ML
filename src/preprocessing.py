from sklearn import preprocessing  #To label encode y(dependent variable)

import pandas as pd  # For working with DataFrame

def load_dataset(dataset_url):
    mal_ds = pd.read_csv(dataset_url)

    print("First 5 URLs and their corresponding labels:")
    print(mal_ds['url'][:5])
    print(mal_ds['type'][:5])

    return mal_ds



def duplicate_url_check(mal_ds):
    # Checking for duplicated rows in column 1 - URL list
    duplicate_urls = mal_ds[mal_ds.duplicated(subset=mal_ds.columns[0])]
    total_duplicates = duplicate_urls.shape[0]
    print("\n Total row count before duplicate clean-up:\n", mal_ds.shape[0])
    print("\nTotal number of duplicate URLs:", total_duplicates)

    print("\nClass distribution of duplicated URLs:\n")
    print(duplicate_urls['type'].value_counts())

    return total_duplicates


def remove_if_duplicate(mal_ds,total_dupes):

    if total_dupes > 0:
        # Deleting Duplicated rows based on identified duplicates of the first column - URLs
        print("\nDeleting duplicate rows....\n")
        cleaned = mal_ds.drop_duplicates(subset=mal_ds.columns[0], keep='first')
        #Checking the number of URLs before and after dropping duplicate URLs
        print("\nTotal row count after duplicate clean-up:\n", cleaned.shape[0])
    else:
        return mal_ds

    return cleaned

def check_for_missing_vals(mal_ds):
    #Checking for missing values
    count_missing_values = mal_ds.isnull().sum()
    print("Missing values per column:")
    print(count_missing_values)

    return count_missing_values


def drop_missing_val_rows(mal_ds,count_missing_values):
    
    if count_missing_values.sum() > 0:   #.sum converts the series into a single number
        #Drop any rows with any missing values
        cleaned = mal_ds.dropna()
        # Verifying no missing values remain
        print(f"\nAfter cleaning missing values: {cleaned.isnull().sum().sum()}")
        print(f"Final dataset size: {cleaned.shape[0]} rows")

        return cleaned
    else:
        return mal_ds
    


def balance_dataset(mal_ds):
    # Balancing the dataset
    benign = mal_ds[mal_ds['type'] == 'benign'].sample(n=23000)
    defacement = mal_ds[mal_ds['type'] == 'defacement'].sample(n=23000)
    phishing = mal_ds[mal_ds['type'] == 'phishing'].sample(n=23000)
    malware = mal_ds[mal_ds['type'] == 'malware'].sample(n=23000)

    balanced_df = pd.concat([benign, defacement, phishing, malware])
    X = balanced_df.iloc[:,0]  #getting all rows from the first column - urls: the independent variable
    Y = balanced_df.iloc[:,1] # getting all rows from the second column - types : the dependent variable
    print("Total Sample Size:",balanced_df.shape[0])
    print("\nSamples per type:")
    print(balanced_df['type'].value_counts())
    
    return X, Y


def label_encoding(Y):
        # Label Encoding - Dependent Variable, Y - Classifications
    le = preprocessing.LabelEncoder()
    le.fit(Y)  # Assigning labels to numbers

    #le.classes_ - stores the internal mapping
    # # le.transform - This maps the labels to the assigned values

    numeric_value = le.transform(le.classes_)
    class_label = le.classes_

    print("\nShowing Label Mapping:\n")
    for i in range(len(numeric_value)):
        print(f"{class_label[i]}: {numeric_value[i]}")

    y = le.transform(Y)

    return y, le

