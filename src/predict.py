from sklearn.metrics import (
accuracy_score,
confusion_matrix,
precision_score,
recall_score,
ConfusionMatrixDisplay,
classification_report)
import matplotlib.pyplot as plt   # For Plotting
from sklearn.preprocessing import LabelEncoder 

label_mapping = {
    0: 'Benign',
    1: 'Defacement',
    2: 'Malware',
    3: 'Phishing'
}

def model_predict(model,x_test_df):
    y_prediction = model.predict(x_test_df)
    return y_prediction


def model_eval(y_test,y_prediction):
    accuracy = accuracy_score(y_test,y_prediction)
    print(f"Model Accuracy: {accuracy:.2f}")
    #Showing classification report
    
    return accuracy


def classification_report_plot(y_test,y_prediction,le):
    print("\nClassification Report:\n")
    report_model_str = classification_report(y_test,y_prediction,target_names=le.classes_)  # for printing
    report_model_dict = classification_report(y_test,y_prediction,output_dict=True) # for heatmap - model comparision

    print(report_model_str)

    return report_model_str, report_model_dict
    

def confusion_matrix_plot(y_test,y_prediction,le):
    # Plotting a confusion matrix 
    confusion_matix_report = ConfusionMatrixDisplay.from_predictions(y_test, y_prediction, display_labels=le.classes_,cmap="Blues", normalize="true")
    plt.title("Confusion Matrix for Model 3 - Logistic Regression")
    plt.show()

    return confusion_matix_report

