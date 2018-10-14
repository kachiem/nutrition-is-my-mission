### HOW TO RUN
### $ python readtext.py image.jpeg


import argparse
import io
import re
from google.cloud import vision
from PIL import Image, ImageDraw

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import matplotlib.patches as patches

from spellchecker import SpellChecker
import sys
import argparse

from algoliasearch import algoliasearch

def main(filename):
    x1=0
    x2=0
    y1=0
    y2=0
    
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.') 

    args = parser.parse_args()
    
    algclient = algoliasearch.Client("4LPXVGEXST", 'f268aa460abc20703812137fae5079ba')
    index = algclient.init_index('food_ingredients')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    #filename="ingredients.jpeg"
    image = Image.open(args.detect_file)
    #image.show()
    arr = np.asarray(image)
    plt_image=plt.imshow(arr)
    rs=widgets.RectangleSelector(
        ax, onselect, drawtype='box',
        rectprops = dict(facecolor='red', edgecolor = 'black', alpha=0.4, fill=True))

    plt.show()

    text = detect_text('i.jpg')

    #print text
    text = re.sub('-\\n','',text)
    text = re.sub('\\n| AND | OR |AND\/OR|ANDIOR',' ',text)
    text = re.sub('MADE FROM|,AND |,OR |\(|\)|\[|\]|\.',',',text)
    #print text

    ingredients = text.split(',')
    #print ingredients

    ingredients2 = []
    for ing in ingredients:
        if len(ing) == 0:
            continue
        newIng = (re.sub(r'.+NTS:','',ing))
        newIng = newIng.strip(' ')
        if len(newIng) == 0:
            continue
        ingredients2.append(newIng)
    
    print (ingredients2,'\n\n\n\n')

    """for i in range(len(ingredients)):
        ingredients[i] = re.sub('\\n',' ',ingredients[i])"""
    
    """if __name__ == '__main__':
        get_bounds('chips.jpeg')
        detect_text('i.jpeg')"""
    




    """#add to allowed by importing FDA csv file
    with open('FoodSubstances.csv', mode='r') as infile:
        reader = csv.reader(infile)
        with open('FoodSubstances.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            more = dict((rows[1], rows[3]) for rows in reader)
        
    helper = more.copy()
    helper.update(ingTab)
    allowed = helper"""

    print("\n\n\n")
    for ing in ingredients2:
        print('====', ing , '=====')
        hit = index.search(ing)['hits']
        if len(hit) > 0:
            h = hit[0]['Used for (Technical Effect)']
            h = re.sub('<br \/>','',h)
            print(h)
        """if ing in allowed:
            print ing + ": " + allowed[ing]
        else:
            print ing + ": " + "***********"""
        print('\n\n\n')
    return("hi")

#rect = patches.Rectangle((0,0),0,0)

def rectangle(eclick,erelease):
    if eclick.ydata>erelease.ydata:
        eclick.ydata,erelease.ydata=erelease.ydata,eclick.ydata
    if eclick.xdata>erelease.xdata:
        eclick.xdata,erelease.xdata=erelease.xdata,eclick.xdata
    return [eclick.xdata,eclick.ydata,erelease.xdata,erelease.ydata]


def onselect(eclick, erelease):
    [x1,y1,x2,y2] = rectangle(eclick,erelease)
    #for a in ax.patches:
        #a.remove()
    #if eclick.ydata>erelease.ydata:
        #eclick.ydata,erelease.ydata=erelease.ydata,eclick.ydata
    #if eclick.xdata>erelease.xdata:
        #eclick.xdata,erelease.xdata=erelease.xdata,eclick.xdata
    x1 = eclick.xdata
    y1 = eclick.ydata
    x2 = erelease.xdata
    y2 = erelease.ydata
    
    
    #rect.remove()
    
    
    # Create a Rectangle patch
    #rect = patches.Rectangle((x1,y1),x2-x1,y2-y1,linewidth=1,edgecolor='r',facecolor='none')

    # Add the patch to the Axes
    #ax.add_patch(rect)
    #plt.show()
    fig.canvas.draw()
    #plt.close()
    #rs.set_visible(rs.visible)
    img2 = image.crop((x1,y1,x2,y2))
    img2.save('i.jpg')


def detect_text(path):    
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print texts[0].description
    #print('Texts:')


    #f = open('output.txt','w')
    
    """text = texts[0].description
    text = text.split('\n')
    p = False
    for t in text:
        if 'INGREDIENTS' in t:
            p == True
        if p == True:
            print t
        if '.' in t:
            return"""
        
    #print texts
    text = texts[0]
    print (text , '\n\n\n')
    #t = '"{}"'.format(text.description)
    t = text.description.encode('utf-8')
    #t = t.encode('utf-8')
    #ingredients = t.split(',')
    
    return t
    







    
    
#export GOOGLE_APPLICATION_CREDENTIALS="./My First Project-71a933f186a1.json"