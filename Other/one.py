import streamlit as st

import pandas as pd

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score


st.write('''
        # Breast Cancer Data Analysis

        From sklearn.datasets
''')


# print(load_breast_cancer())


feature_names = load_breast_cancer().get('feature_names')

data = pd.DataFrame(load_breast_cancer().get('data'), columns=feature_names)
target = pd.Series(load_breast_cancer().get('target'), name='Breast Cancer')
st.write(data.head(10), 'Data Dimensions', data.shape)
st.write('''

        ### Target Variable: Last ten
        1: Positive
        0: Negative

''')

st.write(target.tail(10))


st.write(' ## Exploratory Analysis')

st.write('Missing Values', data.isnull().sum())

st.write('Split the data: 70 - training, 30% - testing')

X = data 
y = target

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=.3, random_state=11)

st.write('X_train_sample: notice the random selection', X_train, type(X_train))


logistic_regression = LogisticRegression(random_state=11)


model = logistic_regression.fit(X_train, y_train)

st.write('Trained the model', model)

predictions = model.predict(X_valid)

acc_score = accuracy_score(y_valid, predictions)

st.write('Model Accuracy: ', acc_score)