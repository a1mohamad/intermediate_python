import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
import pymongo



def connecting_db():
    conn = pymongo.MongoClient(
            'localhost',
            27017
    )
    db = conn['houses']
    collection = db['berlin']
    return collection


def giving_training_datas(collection):
    elements= collection.find()
    x_train, y_train= [], []
    for element in elements:
        x_tmp= [0, 0]
        x_tmp[0]= element['size']
        x_tmp[1]= element['number of bedrooms']
        x_train.append(x_tmp)
        y_train.append(int(element['price']))
    return x_train, y_train



def arraying_data(x_train, y_train):
    X= np.zeros((len(x_train),2))
    y= np.zeros(len(y_train))
    for i in range(len(x_train)):
        X[i]= x_train[i]
        y[i]= y_train[i]
    X= X.reshape(-1, 2)
    return X, y



def linear_regression(X, y):
    
    scaler = StandardScaler()
    LR= LinearRegression()
    LR.fit(X, y)
    b = LR.intercept_
    w = LR.coef_
    print(f"model parameters:                   w: {w}, b:{b}")
    y_pred_lr = LR.predict(X)
    return LR, y_pred_lr



def predict_price(input_size, input_bedrooms, LR):
    features= np.zeros(2)
    features[0]= input_size 
    features[1]= input_bedrooms
    features= features.reshape(-1, 2)
    price= int(LR.predict(features)[0])
    return print(f'Your predicted price is : {price}')