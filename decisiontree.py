import pandas as pd
import numpy as np
from sklearn import tree

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# print(train.head())
# take a look at your training data
# print(train.describe())
# print(train["result"].value_counts(normalize=True))
# print(train["result"][train["AgeOfEstablishment"] >  20].value_counts(normalize=True))

# Step 1 -  data cleansing and feature engineering
train["result"][train["result"] == "Yes"] = 1
train["result"][train["result"] == "No"] = 0
# train["field"] = train["field"].fillna(0)
# train["AgeOfEstablishment"] = train["AgeOfEstablishment"].fillna(train["AgeOfEstablishment"].mean())


# Step 2 - choosing informative, discriminating and independent features for algorithms　特徴抽出
target = train["result"].values
features_one = train[["AgeOfEstablishment", "Sales", "ProfitRatio"]].values
# features_one = features_one.astype('int')
target = np.array(target, dtype=int)
# print(features_one)
# print(features_one.shape)

my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one, target) # model
# print(my_tree_one.feature_importances_)
# print(my_tree_one.score(features_one, target))


# Step 3 -  data cleansing and feature engineering(test data)
# test["field"] = test["field"].fillna(0)
# test["field"] = test["field"].fillna(test["field"].mean())

# Step 4 - get test data
test_one = test
test_one_features = test_one[["AgeOfEstablishment", "Sales", "ProfitRatio"]].values
test_one_target = test_one["result"].values
test_one_target = np.array(target, dtype=int)

# Step 4 - using model to predict test data
my_prediction = my_tree_one.predict(test_one_features)
# print(my_prediction)
Name =np.array(test["Name"])
Id = np.array(test["Id"]).astype('int')
my_solution = pd.DataFrame(Name, Id, columns=["Name"])
my_solution["result"] = my_prediction
# print(my_solution)



my_solution.to_csv("predict.csv")

