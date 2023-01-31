from sklearn import svm
from sklearn.preprocessing import LabelEncoder
import pandas as pd

#input the project address
print("enter the project address")

project_address=input()


le = LabelEncoder()
# Load your data into a pandas dataframe
data = pd.read_csv("climate-grant-votes/climate_grant_votes.csv")
data
# Define the features you want to use for anomaly detection
X = data[["source_wallet", "destination_wallet"]]
X['source_wallet'] = le.fit_transform(X['source_wallet'])
X['destination_wallet'] = le.fit_transform(X['destination_wallet'])

# Create a One-Class SVM model
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma="scale")

# Fit the model to the data
clf.fit(X)

# Generate anomaly scores for each instance
anomaly_scores = clf.decision_function(X)

# Classify instances as anomalies or not
predictions = clf.predict(X)

# predictions
data["predictions"]=predictions

#printing the data about the project address u enter 
print(data[data["destination_wallet"] == project_address])

#saving the predictions about all the transactions
data.to_csv("svm.csv")
