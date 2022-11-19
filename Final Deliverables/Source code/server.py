import model
import pandas as pd 
import numpy as np 
from flask import Flask, request, render_template 

app = Flask(__name__,template_folder="templates")

# Default route set as 'home'
@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/classify',methods=['GET'])
def classify_type():
    try:
        age = request.args.get('Age') # Get parameters for sepal length
        sex = request.args.get('Sex') # Get parameters for sepal width
        chest_pair = request.args.get('Chest pain type') # Get parameters for petal length
        bp = request.args.get('BP') # Get parameters for petal width
        cholestrol = request.args.get('Cholesterol') 
        FBS_over_120 = request.args.get('FBS over 120') 
        EKG_results = request.args.get('EKG results') 
        Max_HR = request.args.get('Max HR') 
        Exercise_angina = request.args.get('Exercise angina') 
        ST_depression = request.args.get('ST depression') 
        Slope = request.args.get('Slope of ST') 
        Num = request.args.get('Number of vessels fluro') 
        Thallium = request.args.get('Thallium') 
        result=""
        # Get the output from the classification model
        variety = model.classify(age,sex,chest_pair,bp,cholestrol,FBS_over_120,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope,Num,Thallium)
        if variety == 'Presence':
            result+="Status: You have a heart diesease!!Consult your physician soon"
        else:
            result+="Status: You are healthy and free from heart diesease!!"
        # Render the output in new HTML page
        return render_template('output.html', variety=result)
    except:
        return 'Error'   

if(__name__=='__main__'):
    app.run(debug=True)