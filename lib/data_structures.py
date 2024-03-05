import json

def get_names(spicy_foods):
    """
    Returns a list of names of each spicy food.
    """
    names = [food['name'] for food in spicy_foods]
    print("Names of spicy foods:")
    for name in names:
        print(name)
    return names

def get_spiciest_foods(spicy_foods):
    """
    Returns a list of dictionaries where the heat level > 5.
    """
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    print("Spiciest foods:")
    print_spicy_foods(spiciest_foods)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    """
    Prints each spicy food with its cuisine and heat level.
    """
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    return spicy_foods

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns a single dictionary for the spicy food of specified cuisine.
    """
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            print(f"Spicy food of cuisine {cuisine}: {food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """
    Prints only the spicy foods with heat level > 5.
    """
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    print("Spiciest foods:")
    print_spicy_foods(spiciest_foods)
    return spiciest_foods

def average_heat_level(spicy_foods):
    """
    Calculates the average heat level of all spicy foods.
    """
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    print(f"Average heat level of all spicy foods: {average_heat}")
    return average_heat

def create_spicy_food(spicy_foods, new_spicy_food):
    """
    Adds a new spicy food to the list.
    """
    spicy_foods.append(new_spicy_food)
    print(f"New spicy food added: {new_spicy_food}")
    return spicy_foods

def load_spicy_foods():
    """
    Loads spicy foods from JSON file.
    """
    with open('spicy_foods.json', 'r') as f:
        spicy_foods = json.load(f)
    return spicy_foods

def save_spicy_foods(spicy_foods):
    """
    Saves spicy foods to JSON file.
    """
    with open('spicy_foods.json', 'w') as f:
        json.dump(spicy_foods, f)
