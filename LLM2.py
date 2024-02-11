import os
import json

import predictionguard as pg
from langchain.prompts import PromptTemplate
import numpy as np


os.environ['PREDICTIONGUARD_TOKEN'] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"

dishes = ["omlette","beef bowl with cheese","grilled fish"]

for dish in dishes:
	template = """### Instruction: Read the context and then generate recepices for the food items
	that only use the ingredients given. The context will have a list of ingredients in [] that denoted by brackets.
	For each dish(dishes are denoted by the second []) output a recipe. Reponses shoul followedd by a dish. Generate a recipe for the dish. follow the guidelines outlined in the question.

	### Input:
	Context: {context}
	Question: {question}

	### Response:
	"""
	prompt1 = PromptTemplate(
		input_variables=["context", "question"],
		template=template,
	)


	context = f"[fish,ground beef, cheese. milk. apples, eggs],{dish}"
	question = """Please generate a recipe idea that could be made from these ingredients given in the context.
	The main focus is on a good recipe and each recipe does not have to use all the ingredients.
	First list the specific ingredients that you need for the recipe that you chose. Make sure only list the ingredients that will be used for
	the recipe and only use ingredients that are in the context. However, you can assume the use of spices, stocks, butter, and sauces.
	and then list the instructions for making it"""

	completions = pg.Completion.create(
			model="Nous-Hermes-Llama2-13B",
			prompt=[
				prompt1.format(context=context, question=question),
				# prompt2.format(context=context, question=question)
			],
			max_tokens= 1000,
			temperature=0.5
		)

	print(completions['choices'][0]["text"])
