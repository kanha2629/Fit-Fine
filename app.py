from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('model1.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():

    Name=request.form.get('name')
    Gender=request.form.get('Gender')
    Age=request.form.get('Age')
    Height=request.form.get('Height')
    Weight=request.form.get('Weight')
    Duration=request.form.get('Duration')
    Heart_Rate=request.form.get('Heart_Rate')
    Body_Temp=request.form.get('Body_Temp')
    Heart_Rate=request.form.get('Heart_Rate')

    # cgpa = request.form.get('cgpa')
    # iq = request.form.get('iq')
    # profile_score = request.form.get('profile_score')

    input_query = np.array([[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]])

    result = model.predict(input_query)[0]

    return jsonify({'calories_burnt':str(result)})

if __name__ == '__main__':
    app.run(debug=True)