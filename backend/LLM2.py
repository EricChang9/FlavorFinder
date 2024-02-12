from calendar import c
import os
import json
from re import split

import predictionguard as pg
from langchain.prompts import PromptTemplate
import numpy as np

def generate_recipe_from_ingredients(food_text):
  """
  Generates a recipe from a list of ingredients using the Nous-Hermes-Llama2-13B model.

  Args:
      food_text (str): The list of ingredients to use in the recipe.

  Returns:
      str: The generated recipe.
  """
  os.environ['PREDICTIONGUARD_TOKEN'] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"

  template = """### Instruction: Read the context and then generate recepices for the food items
      that only use the ingredients given. The context will have a list of ingredients in [] that denoted by brackets.
      For each dish(dishes are denoted by the second []) output a recipe. Reponses should be followed by a dish. Generate a recipe for the dish. Follow the guidelines outlined in the question.

      ### Input:
      Context: {context}
      Question: {question}

      ### Response:
      """
  prompt1 = PromptTemplate(
      input_variables=["context", "question"],
      template=template,
    )

  context = f"{food_text},{food_text}"
  question = """Please generate only a recipe idea that could be made from these ingredients given in the context(Do not include the items found in the image).
  The main focus is on a good recipe and each recipe does not have to use all the ingredients.
  First, list the specific ingredients that you need for the recipe that you chose. Make sure only to list the ingredients that will be used for
  the recipe and only use ingredients that are in the context. However, you can assume the use of spices, stocks, butter, and sauces.
  and then list the instructions for making it. Format the text as javascript string that has (\n) after each ingredient and instruction."""

  completions = pg.Completion.create(
      model="Nous-Hermes-Llama2-13B",
      prompt=[
         prompt1.format(context=context, question=question),
        # prompt2.format(context=context, question=question)
      ],
      max_tokens= 1000,
      temperature=0.5
    )

  recipe_index=(completions['choices'][0]["text"]).find("Recipe")

  #Removes unneccesary Javascript code
  split_text = (completions['choices'][0]["text"])[recipe_index:] if recipe_index != -1 else (completions['choices'][0]["text"])
  
  return json.dumps(split_text)
