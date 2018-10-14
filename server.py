#!/usr/bin/python


"""if __name__ == "__main__":
    print 'hi'
    
def __init__(self):
    main()"""
import argparse
import io
import re
from google.cloud import vision
from PIL import Image, ImageDraw

from flask import Flask, request, render_template
app = Flask(__name__)

def detect_text(uri):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = uri
    # [START vision_python_migration_text_detection]
    #with io.open(path, 'rb') as image_file:
        #content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts
    
@app.route("/script", methods = ['POST','GET'])
def script():
    input_img = request.form['data']
    
    text = detect_text(input_img)
    return texts
    #if request.method == 'POST':
        
        #input_img = request.files.get('imagefile', '')
        
    

    """
    Your script code here
    """

    #return render_template('test.html')
    #return render_template("index.html", things = 'hooray')

@app.route('/')
def static_page():
    return render_template('index.html')
    
    #input_img = request.files.get('imagefile', '')

if __name__ == "__main__":
    app.run()