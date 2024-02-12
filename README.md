<<<<<<< HEAD
# FoodPlanner
Hacklytics 2024
=======
# React + Vite

This template provides a minimal setup to get React working in **Vite** with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
>>>>>>> front-end
>>>>>>
During Hacklytics, our goal was to create a mobile application allowing users to upload JPEG and PNG images of refrigerator contents to track ingredients and suggest recipes.  This project was inspired to help people eat healthier and better with the food that they already have. Thus, we can keep people healthy while also reducing waste and helping people save money.
For the front end, we used **React** in order to create a webpage where people could upload their photos. This is the same webpage where the generated recipes would show. In order to store and send the photos to our back end, we utilized the **FireBase** server system. In order to generate recipes from this information, we first used the **Google Gemini Pro Vision** model’s object detection capabilities to detect the different types of food items in the images. With this information we were able to come up with a list of different ingredients that were in the picture. While Google’s model was able to generate possible dishes, we decided to use the **Nous-Hermes-Llama2-13B model** to generate the recipes. Finally, we used FireBase again in order to transport the generated recipes to the front end for the user to see. This is hosted on **AWS Amplify**.
We encountered many technical challenges along the way. For instance, this was the first time working with AI for everyone on the team. Additionally, we had no full stack development experience and had to learn everything on the fly. The biggest challenges were finding accurate image models. We tried many different solutions such as **GPT-4** or even training our own model. Lastly, a big challenge that we faced was linking our front end data with our back end data. 
	Given more time, we would love to keep working on this project to refine and improve it. Some obvious ways our project could be improved is through a cleaner front end as well as a more efficient data transmission process. In the long run we also hope to train our own model so that it will be more specified at food identification compared the ready to use models.


