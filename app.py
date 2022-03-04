import pickle
import pandas as pd
from flask import (
        Flask, render_template, request
        )
app = Flask(__name__, template_folder='FrontEnd/templates')
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
 

@app.route('/', methods=('GET', 'POST'))
def main_page():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['your_sex'])
        chest_pain = int(request.form['chest_pain'])
        resting_bp = int(request.form['resting_bp'])
        cholesterol = int(request.form['cholesterol'])
        fasting_blood_sugar = int(request.form['fasting_blood_sugar']) 
        resting_ecg = int(request.form['resting_ecg'])
        max_heart_rate = int(request.form['max_heart_rate'])
        exercise_angina = int(request.form['exercise_angina'])
        oldpeak = int(request.form['oldpeak'])
        ST_slope = int(request.form['ST_slope'])
        # Model computation
        with open('saved-model.txt', 'rb') as open_file:
            model = pickle.load(open_file)
        #create data frame contain user input
        prediction_features = pd.DataFrame({
            'age':[age],
            'sex':[sex],
            'chest_pain':[chest_pain],
            'resting_bp':[resting_bp],
            'cholesterol': [cholesterol],
            'fasting_blood_sugar':[fasting_blood_sugar],
            'resting_ecg': [resting_ecg],
            'max_heart_rate':[max_heart_rate],
            'exercise_angina':[exercise_angina],
            'oldpeak':[oldpeak],
            'ST_slope':[ST_slope] 
        })
#pass data to predict function
#
        prediction = model.predict(prediction_features) [0]

        return render_template('predict.html', prediction = prediction)
    return render_template('index.html')
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
