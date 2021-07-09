from flask import Flask, request
import pandas as pd
from sklearn.metrics import  roc_auc_score

# import webbrowser
# webbrowser.open_new('http://127.0.0.1:5000/')

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def score():
    y_test2 = pd.read_csv('y_test2.csv')
    y_test2_predictions = pd.read_csv(request.files['file'])
    auc_score = roc_auc_score(y_test2, y_test2_predictions)
    auc_score = 'Mini-Kaggle Project -  Your score: ' + str(auc_score)
   

    return auc_score