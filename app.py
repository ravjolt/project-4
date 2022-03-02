from flask import (
        Flask, render_template, request
        )
app = Flask(__name__, template_folder='FrontEnd/templates')

@app.route('/', methods=('GET', 'POST'))
def main_page():
    if request.method == 'POST':
        blood_pressure = int(request.form['blood_pressure'])

        # Model computation
        if blood_pressure >= 150:
            prediction = "Oh no!"
        else:
            prediction = "No problem"

        return render_template('predict.html', prediction = prediction)
    return render_template('index.html')
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
