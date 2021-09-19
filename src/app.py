from __future__ import unicode_literals
from flask import Flask, render_template, request
import threading, queue
import youtube_dl


q = queue.Queue()

def worker(status):

    def callable_hook(response):
        status = response['status']

    ydl_opts = {
        "progress_hooks": [callable_hook],
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]",
        "outtmpl": "/download/%(title)s.%(ext)s"
        }

    while True:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([q.get()])
        q.task_done()

output_str = ""
threading.Thread(target=worker, daemon=True, args=(output_str, )).start()

def get_output():
    return str(q.qsize()) + " items in queue.\nStatus: " + str(output_str)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get():
    return render_template("index.html", output=get_output())

@app.route("/", methods=['POST'])
def post():
    q.put(request.form['url'])
    return render_template("index.html", output=get_output())
