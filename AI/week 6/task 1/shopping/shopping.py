import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        1  - Administrative, an integer
        2  - Administrative_Duration, a floating point number
        3  - Informational, an integer
        4  - Informational_Duration, a floating point number
        5  - ProductRelated, an integer
        6  - ProductRelated_Duration, a floating point number
        7  - BounceRates, a floating point number
        8  - ExitRates, a floating point number
        9  - PageValues, a floating point number
        10 - SpecialDay, a floating point number
        11 - Month, an index from 0 (January) to 11 (December)
        12 - OperatingSystems, an integer
        13 - Browser, an integer
        14 - Region, an integer
        15 - TrafficType, an integer
        16 - VisitorType, an integer 0 (not returning) or 1 (returning)
        17 - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """    
    labels = []
    evidences = []
    csv_data = pd.read_csv(filename)
    
    for _, row in csv_data.iterrows():
        evidences.append(get_evidences(row))
        labels.append(get_label(row))
    
    return (evidences, labels)

def get_evidences(row :pd.Series):
    evidences = []
    evidences.append(row["Administrative"])
    evidences.append(row["Administrative_Duration"])
    evidences.append(row["Informational"])
    evidences.append(row["Informational_Duration"])
    evidences.append(row["ProductRelated"])
    evidences.append(row["ProductRelated_Duration"])
    evidences.append(row["BounceRates"])
    evidences.append(row["ExitRates"])
    evidences.append(row["PageValues"])
    evidences.append(row["SpecialDay"])

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    evidences.append(months.index(row["Month"]))
    evidences.append(row["OperatingSystems"])
    evidences.append(row["Browser"])
    evidences.append(row["Region"])
    evidences.append(row["TrafficType"])
    
    visitor_type = 1 if row["VisitorType"] == "Returning_Visitor" else 0
    evidences.append(visitor_type)
    evidences.append(int(row["Weekend"]))
    
    return evidences

def get_label(row :pd.Series):
    return int(row["Revenue"])
    

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neighbor_classifier = KNeighborsClassifier(n_neighbors=1)
    return neighbor_classifier.fit(evidence, labels)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    POSITIVE = 1
    NEGATIVE = 0
    
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    
    for label, predict in zip(labels, predictions):
        if label == POSITIVE and predict == POSITIVE:
            true_positive += 1
        elif label == NEGATIVE and predict == NEGATIVE:
            true_negative += 1
        elif label == POSITIVE and predict == NEGATIVE:
            false_negative += 1
        else:
            false_positive += 1
    
    sensitivity = true_positive / (true_positive + false_negative)
    specificity = true_negative / (true_negative + false_positive)
    
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
