import os
import requests
import base64
from flask import Flask, render_template, request
from Nutridata import get_nutrition_details, generate_text

app = Flask(__name__)

from inference import get_flower_name

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        try:
            # Handle image upload
            if 'file' in request.files and request.files['file'].filename != '':
                file = request.files['file']
                image = file.read()
                encoded_image = base64.b64encode(image).decode('utf-8')
                food_name = get_flower_name(image_bytes=image)
                food_name = food_name.replace('_', ' ')

            # Handle text input
            elif 'food_name' in request.form and request.form['food_name']:
                food_name = request.form['food_name']
                encoded_image = None
            else:
                return render_template('index.html', error="Please provide either an image or food name")

            # Get nutrition details
            api_key = "nQ4auDuHeDorC7u9hVZy7Rq0Tdgf4Ed0QBEhrmQT"
            nutrition_details = get_nutrition_details(api_key, food_name)
            
            if nutrition_details:
                text_output = generate_text(nutrition_details)
                return render_template('result.html', 
                                    food=food_name, 
                                    nutrition_details=nutrition_details,
                                    text_output=text_output,
                                    image=encoded_image)
            else:
                return render_template('index.html', error="Food item not found. Please try again.")
                
        except Exception as e:
            print(f"Error: {str(e)}")
            return render_template('index.html', error="An error occurred. Please try again.")

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/architecture')
# def architecture():
#     return render_template('architecture.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
