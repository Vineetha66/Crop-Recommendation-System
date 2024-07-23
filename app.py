from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

app = Flask(__name__, template_folder="templates", static_folder="static")
model = pickle.load(open("C:\\Users\\Vineetha Juttiga\\Dropbox\\PC\\Documents\\Crop-Recommendation-System-Using-Machine-Learning-main (2)\\Crop-Recommendation-System-Using-Machine-Learning-main\\croprecGNB.pkl", "rb"))
print("Model Loaded")

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        print(form_data)  # Print the entire form data dictionary for debugging

        N = float(form_data.get('N', 0))  # Use form_data.get to avoid KeyError
        P = float(form_data.get('P', 0))
        K = float(form_data.get('K', 0))
        temperature = float(form_data.get('temperature', 0))
        humidity = float(form_data.get('humidity', 0))
        ph = float(form_data.get('ph', 0))
        rainfall = float(form_data.get('rainfall', 0))

        input_lst = [[N, P, K, temperature, humidity, ph, rainfall]]
        pred = model.predict(input_lst)
        output = pred

        if output[0] == 'rice':
            return render_template("rice.html")
        elif output[0] == 'maize':
            return render_template("maize.html")
        elif output[0] == 'chickpea':
            return render_template("chickpea.html")
        elif output[0] == 'kidneybeans':
            return render_template("kidneybeans.html")
        elif output[0] == 'pigeonpeas':
            return render_template("pigeonpeas.html")
        elif output[0] == 'mothbeans':
            return render_template("mothbeans.html")
        elif output[0] == 'mungbean':
            return render_template("mungbean.html")
        elif output[0] == 'blackgram':
            return render_template("blackgram.html")
        elif output[0] == 'lentil':
            return render_template("lentil.html")
        elif output[0] == 'pomegranate':
            return render_template("promegranate.html")
        elif output[0] == 'banana':
            return render_template("banana.html")
        elif output[0] == 'mango':
            return render_template("mango.html")
        elif output[0] == 'grapes':
            return render_template("grapes.html")
        elif output[0] == 'watermelon':
            return render_template("watermelon.html")
        elif output[0] == 'muskmelon':
            return render_template("muskmelon.html")
        elif output[0] == 'apple':
            return render_template("apple.html")
        elif output[0] == 'orange':
            return render_template("orange.html")
        elif output[0] == 'papaya':
            return render_template("papaya.html")
        elif output[0] == 'coconut':
            return render_template("coconut.html")
        elif output[0] == 'cotton':
            return render_template("cotton.html")
        elif output == 'jute':
            return render_template("jute.html")
        else:
            return render_template("coffee.html")

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
