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
    if(filename):
        return 1
    else:
        return 0