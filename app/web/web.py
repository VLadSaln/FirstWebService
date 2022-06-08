
from flask import render_template, request, redirect
from web import app
import os


name = "Unknown User"



@app.route("/upload-video", methods=["GET", "POST"])
def upload():
    
    return render_template("upload_video.html")



