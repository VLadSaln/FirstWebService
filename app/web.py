
from flask import render_template, request, redirect
from app import app
import os
from config import Config
name = "Unknown User"



@app.route("/upload-video", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            video = request.files["video"]
            video.save(os.path.join(app.config["VIDEO_UPLOADS"], video.filename))
            print("Video saved")
            return redirect('/trecker')
    return render_template("upload_video.html")
@app.route("/trecker", methods=["GET", "POST"])
def trecking():
    return render_template("trecker.html")


