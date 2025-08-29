import requests
import time
from functools import lru_cache
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@lru_cache(maxsize=100)  # Cache up to 100 most recent food items
def get_nutrition_details(api_key, food_name):
    try:
        url = "https://api.nal.usda.gov/fdc/v1/foods/search"
        params = {
            "query": food_name,
            "api_key": api_key,
            "pageSize": 1  # Limit to 1 result to reduce response size
        }
        
        # Add timeout to prevent hanging
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()

        if 'foods' in data and len(data['foods']) > 0:
            food_item = data['foods'][0]
            nutrition_details = {
                "Name": food_item['description'],
                "Nutrients": {}  # Dictionary to store all nutrients
            }

            # Only get essential nutrients to reduce processing time
            essential_nutrients = ['Energy', 'Protein', 'Total lipid (fat)', 'Carbohydrate, by difference', 
                                 'Fiber, total dietary', 'Sugars, total', 'Calcium, Ca', 'Iron, Fe', 
                                 'Sodium, Na', 'Vitamin C, total ascorbic acid', 'Cholesterol']
            
            for nutrient in food_item['foodNutrients']:
                nutrient_name = nutrient['nutrientName']
                if nutrient_name in essential_nutrients:
                    nutrient_value = nutrient['value']
                    nutrient_unit = nutrient['unitName']
                    nutrition_details["Nutrients"][nutrient_name] = f"{nutrient_value} {nutrient_unit}"

            return nutrition_details
        else:
            logger.warning(f"No food items found for query: {food_name}")
            return None
            
    except requests.exceptions.Timeout:
        logger.error(f"Request timed out for food: {food_name}")
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching nutrition data for {food_name}: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error for {food_name}: {str(e)}")
        return None

def generate_text(nutrition_details):
    text_output = f"Nutrition Details for {nutrition_details['Name']}:\n"
    for nutrient_name, nutrient_value in nutrition_details["Nutrients"].items():
        text_output += f"{nutrient_name}: {nutrient_value}\n"
    return text_output

def main():
    api_key = "nQ4auDuHeDorC7u9hVZy7Rq0Tdgf4Ed0QBEhrmQT"
    food_name = input("Enter the food name: ")
    nutrition_details = get_nutrition_details(api_key, food_name)

    if nutrition_details:
        text_output = generate_text(nutrition_details)
        print(text_output)
    else:
        print("Food item not found.")

if __name__ == "__main__":
    main()
