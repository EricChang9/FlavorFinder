# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hVvELnMCsYulC69ClL-YFan3mlXpDTBv
"""

#!pip install predictionguard
#!pip install langchain

import os
import google.generativeai as genai
from PIL import Image
import urllib.request
import json

import predictionguard as pg
from langchain.prompts import PromptTemplate
import numpy as np

def generate_food_text_from_image(image_url, api_key):
    """
    Generates text describing food in an image using the Gemini Pro Vision API.

    Args:
        image_url (str): The URL of the image to analyze.
        api_key (str): Your Google API key.

    Returns:
        str: The generated text describing the food in the image.
    """
    genai.configure(api_key=api_key)

    # Open the image
    image = Image.open("./images/image.png")

    # Create the Gemini model
    model = genai.GenerativeModel("gemini-pro-vision")

    # Generate text describing the food
    response = model.generate_content(
        ["""identify the food items present in the image, 
         then, list them in a numbered, 
         comma-separated style in descending order of likelihood, 
         excluding non-food items. Indent text after each ingredient and instruction.""", image],  # Prompt before image
        stream=False
    )
    response.resolve()

    result=response.text
    return result