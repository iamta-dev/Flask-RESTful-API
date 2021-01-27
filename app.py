from flask import Flask , render_template ,request, jsonify,redirect

app=Flask(__name__)
app.debug = True

import requests
class WeatherCity():
    def getWeatherCity(self):
        URL='http://localhost:5000/weather/'
        response=requests.get(URL)
        weather=response.json()
        return weather

wt = WeatherCity()

@app.route("/")
def viewIndex():
    return render_template('index3.html',weathers = wt.getWeatherCity())

if __name__=="__main__":
    app.run(debug=True, port=8080)