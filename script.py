# Define a list of available pizzas
pizzas = ["Margherita", "Pepperoni", "Vegetarian", "Hawaiian", "Meat Lovers"]

# Define a dictionary of pizza prices
prices = {"Margherita": 10.00, "Pepperoni":12.00, "Vegetarian":15.00, "Hawaiian":11.50}

# Define an empty list to store the user's pizza order
order = []

# Function to display the available pizzas and their prices
def display_menu():
    print("Welcome to our pizza restaurant! Here are our available pizzas: ")
    for pizza in pizzas:
        print("- " + pizza + "")