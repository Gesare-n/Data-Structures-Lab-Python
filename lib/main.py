import json
import data_structures

def main():
    # Load spicy foods from JSON file
    spicy_foods = data_structures.load_spicy_foods()

    # Print the names of the spicy foods
    data_structures.get_names(spicy_foods)

    # Add a new spicy food to the list
    new_spicy_food = {
        "name": "Spicy Tuna Roll",
        "cuisine": "Japanese",
        "heat_level": 4
    }
    spicy_foods = data_structures.create_spicy_food(spicy_foods, new_spicy_food)

    # Save the updated list of spicy foods to JSON file
    data_structures.save_spicy_foods(spicy_foods)

if __name__ == "__main__":
    main()
