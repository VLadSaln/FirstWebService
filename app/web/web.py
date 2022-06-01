
from flask import render_template, request, redirect
from web import app
import os


name = "Unknown User"

app.config["VIDEO_UPLOADS"] = "/home/vladsal/FirstWebService/Yolov5_DeepSort_Pytorch/videos"

@app.route("/upload-video", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            video = request.files["video"]
            video.save(os.path.join(app.config["VIDEO_UPLOADS"], video.filename))
            print("Video saved")
            return redirect('/tracker')
    return render_template("upload_video.html")
@app.route("/tracker", methods=["GET", "POST"])
def tracking():
    if request.method == "POST":
        print('HELLO')
    return render_template("tracker.html")


