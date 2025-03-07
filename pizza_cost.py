#!/usr/bin/env python3

# Created by: Reid MacLean
# Created on: March 6, 2025
# This program calculates and displays the cost of a pizza with user input


def calculate_pizza_cost(diameter_inch_d):
    # Constants for fixed costs
    HST = 0.13
    labour_cost = 2.00
    rental_cost = 2.25
    ingredients_cost_per_inch = 1.50

    # Step 1: Calculate the subtotal (cost before tax)
    subtotal = labour_cost + rental_cost + (ingredients_cost_per_inch * diameter_inch_d)

    # Step 2: Calculate the HST (tax)
    tax = subtotal * (HST)

    # Step 3: Calculate the total cost
    total_cost = subtotal + tax

    # Return the results
    return subtotal, tax, total_cost


def main():
    # Get user input for the diameter of the pizza and HST rate
    diameter = float(input("Enter the diameter of the pizza (in inches): "))

    # Call the function to calculate costs
    subtotal, tax, total_cost = calculate_pizza_cost(diameter)

    # Output the results
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
