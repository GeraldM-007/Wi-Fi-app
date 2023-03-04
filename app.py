import math 
import speedtest
from flask import Flask, render_template

app = Flask(__name__)

def bytes_to_mbs(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes/ power, 2)
    return f"{size}"

def test_speed():
    wifi = speedtest.Speedtest()
    download_speed = wifi.download()
    upload_speed = wifi.upload()
    return bytes_to_mbs(download_speed), bytes_to_mbs(upload_speed)

@app.route('/')
def show_speed():
    
        download_speed, upload_speed = test_speed()

        return render_template('index.html', download_speed=download_speed, upload_speed=upload_speed)
@app.route("/app")
def speed():
        download_speed, upload_speed = test_speed()

        return render_template('flask.html', download_speed=download_speed, upload_speed=upload_speed)

if __name__ == '__main__':
    app.run(debug=True)
    