from flask import Flask , request , jsonify
import utility1

app = Flask(__name__)

@app.route('/get_location_names', methods = ['GET'])
def get_location_names():
    response = jsonify({
        'locations': utility1.get_locations_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': utility1.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__=="__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    utility1.load_saved_artifacts()
    app.run()