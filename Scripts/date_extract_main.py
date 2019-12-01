"""
Import all required modules
"""
from typing import Dict, Any

import time
import os
import json
import operator
import collections
import pytesseract
from PIL import Image
import io
import regex as re
from flask import Blueprint
from flask import request
import __root__
import dir_path

from Scripts.Utils import utility
import dateparser
#from Scripts.Service.Project_Model import Model_Building

import pytesseract
# from PIL import Image

from dateparser.search import search_dates

try:
    from PIL import Image
except ImportError:
    import Image

import datefinder
api_main = Blueprint("api_main", __name__)

exception_message = '{"status": False, "message": "Server error, please contact your administrator"}'
exception_model_not_found = '{"status": False, "message": "Server error, Trained Doc2Vec Model is not found, please contact your administrator"}'
method_error_message = '{"status": False, "message": "Method not supported"}'


@api_main.route('/extract_date', methods=['GET', 'POST'])
def extract_date():
    """
    API for extracting  dates from receipts
    :return:
    """
    date = "no date present"
    if request.method == 'GET': ## No clarity about GET
        return(date)
    if request.method == 'POST':
        text = ""

        try:

            """  1. Data is already available in stored form probably in ./Assets/data/image -- name key of dictiony
             # json.loads(request.data)
                ### tesract will you image Content
            2. imageText -- value will / of this dictionary json.loads(request.data)
            """

            imageText = json.loads(request.data)

            if True:

                imageName = list(imageText.keys())[0]
                imageContent = list(imageText.values())[0]

                #### common image extension /.png /.jpg

                if imageName.endswith(".jpeg") or imageName.endswith(".png") or imageName.endswith(".jpg"):
                    try:

                        imagePath = "Assets/data/"
                        inputPath = os.path.join(imagePath, imageName)

                    # applying ocr using pytesseract
                    ### Have to Remove this on ubuntu machine at AWS
                        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                        text = pytesseract.image_to_string(inputPath, lang="eng")

                    except Exception as e:
                        text = imageContent

                #### if we already have the content
                elif len(imageContent) > 0:
                    text = imageContent

                imageTextTokens = text.split()
                for imageTextToken in imageTextTokens:

                    if (len(imageTextToken) >= 8 and len(imageTextToken) < 12):
                        regex = re.compile('[@_!#$%^&*()<>?\|}{~:]')
                        # Pass the string in search
                        # method of regex object.
                        if (regex.search(imageTextToken) != None):
                           continue

                        date_in_dt = list(datefinder.find_dates(imageTextToken))

                        if (len(date_in_dt) > 0):
                            date_in_dt = list(datefinder.find_dates(imageTextToken))[0]
                            date_in_string = date_in_dt.strftime("%Y-%m-%d")##Change this format DD-MM-YYYY
                            date = date_in_string
                            break
                            #return date

        except Exception as e:
            utility.logger.exception("Exception occurs in API module: " + str(e))
            print(e)


    return date
