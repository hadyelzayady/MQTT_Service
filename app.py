from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
import paho.mqtt.client as mqtt
app = Flask(__name__)

broker="broker.mqttdashboard.com"
@app.route('/')
def main():
    return render_template("base.html")

if __name__ == '__main__':
    app.run()
