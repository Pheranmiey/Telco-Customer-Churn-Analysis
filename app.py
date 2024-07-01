from flask import Flask, request, render_template, redirect, url_for
import pickle
import numpy as np
import logging
from sklearn.preprocessing import LabelEncoder
from encoder import encode_data

logging.basicConfig(filename="churn.log", level=logging.INFO)
app = Flask(__name__)
# Load the necessary objects from pickle files
model = pickle.load(open("model/XGBclassifier.pkl", "rb"))

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict_datapoint', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Extracting data from form
            Gender = request.form.get('Gender')
            SeniorCitizen = request.form.get('SeniorCitizen')
            Partner = request.form.get('Partner')
            Dependents = request.form.get('Dependents')
            TenureMonths = float(request.form.get('TenureMonths'))
            PhoneService = request.form.get('PhoneService')
            MultipleLines = request.form.get('MultipleLines')
            InternetService = request.form.get('InternetService')
            OnlineSecurity = request.form.get('OnlineSecurity')
            OnlineBackup = request.form.get('OnlineBackup')
            DeviceProtection = request.form.get('DeviceProtection')
            TechSupport = request.form.get('TechSupport')
            StreamingTV = request.form.get('StreamingTV')
            StreamingMovies = request.form.get('StreamingMovies')
            Contract = request.form.get('Contract')
            PaperlessBilling = request.form.get('PaperlessBilling')
            PaymentMethod = request.form.get('PaymentMethod')
            MonthlyCharges = float(request.form.get('MonthlyCharges'))
            TotalCharges = float(request.form.get('TotalCharges'))


            Gender_ = len(Gender)
            SeniorCitizen_ = len(SeniorCitizen)
            Partner_ = len(Partner)
            Dependents_ = len(Dependents)
            PhoneService_ = len(PhoneService)
            MultipleLines_ = len(MultipleLines)
            InternetService_ = len(InternetService)
            OnlineSecurity_ = len(OnlineSecurity)
            OnlineBackup_ = len(OnlineBackup)
            DeviceProtection_ = len(DeviceProtection)
            TechSupport_ = len(TechSupport)
            StreamingTV_ = len(StreamingTV)
            StreamingMovies_ = len(StreamingMovies)
            Contract_ = len(Contract)
            PaperlessBilling_ = len(PaperlessBilling)
            PaymentMethod_ = len(PaymentMethod)

            data = [Gender_,SeniorCitizen_,Partner_,Dependents_,TenureMonths,PhoneService_,MultipleLines_,
                    InternetService_,
                    OnlineSecurity_,
                    OnlineBackup_,
                    DeviceProtection_,
                    TechSupport_,
                    StreamingTV_,
                    StreamingMovies_,
                    Contract_,
                    PaperlessBilling_,
                    PaymentMethod_,
                    MonthlyCharges,
                    TotalCharges ]
            # Predict using the loaded model
            data = np.array(data).reshape(1, -1)

            predict = model.predict(data)

            if predict[0] == 1:
                result = 'Churn detected!'
            else:
                result = 'No churn detected!'
            
            # Redirect to single_prediction page with the result
            return redirect(url_for('single_prediction', result=result))

        except Exception as e:
            logging.error(f"Error: {str(e)}")

    elif request.method == 'GET':
        # Handle GET requests here if needed
        return render_template('home.html')

    else:
        # Handle other request methods if needed
        return "Method not allowed", 405  # Return 405 Method Not Allowed status

@app.route('/single_prediction/<result>')
def single_prediction(result):
    return render_template('single_prediction.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
