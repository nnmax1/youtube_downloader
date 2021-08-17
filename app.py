from flask import Flask, render_template, request, jsonify, send_file
from download import  downloadVideo
import glob
import os

downloadStatus =1

app = Flask(__name__, template_folder='templates') 

@app.route('/')
def homePage():
    return render_template('index.html')



@app.route('/', methods = ['POST', 'GET'])
def downloadUrl():
    msg = ''''''
    links =["https://www.youtube.com/", "https://youtube.com", "https://youtu.be" ]
    if request.method == 'POST':
        url = request.form['url']
        if links[0] in url or links[1] in url or links[2] in url:
            r = downloadVideo(url)   
        else:
            msg = url+" is not a valid youtube url"
            return render_template('index.html', downloadingMsg=msg)
    
    return render_template('index.html', downloadingMsg="Finished Downloading")

@app.route("/downloadedfiles")
def getfiles():
    files =[]
    for i in glob.glob("*.mp4"):
        files.append(i)
    return jsonify({"data":files})

@app.route("/deleteData")
def deleteBtn():
    for i in glob.glob("*.mp4"):
        os.remove(i)
    for i in glob.glob("*.part"):
        os.remove(i)
    return jsonify({"status": "deleted"})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
