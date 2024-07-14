from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
from mlProject.pipeline.Prediction_pipeline import PredictionPipeline


app = Flask(__name__) # initialize flask app

@app.route('/',methods=['GET']) # route homepage

def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET']) # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!"

@app.route('/predict', methods=['POST', 'GET']) # route to show the predictions in results.html
def index():
    if request.method == 'POST':
        try:
            # Reading the inputs given by the user
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
       
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            # Convert prediction to a float and format it to two decimal places
            formatted_prediction = "{:.2f}/10".format(float(predict[0]))

            return render_template('results.html', prediction=formatted_prediction)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)