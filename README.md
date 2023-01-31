# Detecting-Sybil-attacks
Note-All the data collected and submitted using ocean protocol

In building this lego i used the one class SVM algorithm.I used the climate grant votes in this example but the model can be applied on any features or any model by just changing the features in the X = data[["source_wallet", "destination_wallet"]] and the path to the data.

One-class Support Vector Machine (SVM) is a type of machine learning algorithm that is primarily used for unsupervised anomaly detection. In this case, only one class is used for training, with the goal being to identify samples that are different from the data used for training, i.e., outliers or anomalies.

One-class SVM is a suitable technique for Sybil attack detection as it allows for the training of a model with only normal samples (legitimate nodes in the network). The algorithm then uses this model to determine if a new node is different from the normal samples and is thus potentially a fake identity. By using a one-class SVM, the model can be trained on a smaller set of normal data, which makes it more suitable for large-scale networks with limited labeled data.

In summary, One-class SVM is useful in detecting Sybil attacks in networks as it provides a means of identifying nodes that are different from the normal samples, which is essential in maintaining the integrity of the system.

On running the program in the main.py file it will ask for the address of the project then it will print all the transactions to that project  it will contain one column where it will show -1 or 1 if majority of the transactions has the -1 it indicates the sybil attack.

<img width="599" alt="image" src="https://user-images.githubusercontent.com/119076200/215895913-d8a2ca1a-09e9-4996-a6e5-8f9daafce483.png">

it will also save a file called svm.csv which will contains the prediction column with the destination_wallet and sender_wallet like this 

<img width="407" alt="image" src="https://user-images.githubusercontent.com/119076200/215895623-e1f381ba-8d73-409f-a78a-0b7d43ab68be.png">

I applied the alogrithm on climate grant data and uploaded it on the ocean protocol u can access it from [here](www.google.com)
