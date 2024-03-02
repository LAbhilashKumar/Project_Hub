from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# load the iris dataset
dataframe=load_iris()
# print(dataframe)
x=dataframe.data
y=dataframe.target

# split the dataset into training and testing sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# creating instance for RandomForestClassifier
rf_classifier=RandomForestClassifier(n_estimators=100,random_state=42)
# train the classifier
rf_classifier.fit(x_train,y_train)
# making predictions
y_prediction=rf_classifier.predict(x_test)
accuracy=accuracy_score(y_test, y_prediction)
print("accuracy :",accuracy)
# print(type(dataframe))