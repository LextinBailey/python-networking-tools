# Progress Log

A log of everything I learned about Python scripting throughout this project.

## 1. Tip Calculator

### 🛠️ What I Built

I created a simple Python CLI tip calculator that takes a bill amount and tip percentage from the user, validates the input, performs the calculation, and prints a formatted result with currency styling.

The script also introduces reusable logic through a function that separates calculation from user input handling.

### 🧠 What I Learned

This was my first real Python CLI script with structured input handling.

Key concepts I worked through:
- How Python handles user input using `input()` (always returns a string)
- Converting string input into numeric types using `float()`
- Handling invalid input using `try/except ValueError`
- Using loops (`while True`) to repeatedly prompt until valid input is given
- Adding logical validation with `if` statements (e.g., preventing negative values)
- Separating calculation logic into a reusable function using `def`
- Returning multiple values from a function
- Formatting output using f-strings
- Controlling decimal precision for display (`:.2f`)