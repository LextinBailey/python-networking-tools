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

## 2. Temperature Converter

### 🛠️ What I Built

I created a Python CLI temperature converter that takes a numeric temperature value and a unit (Celsius, Fahrenheit, or Kelvin) from the user, validates the input, and converts it into the other two temperature scales.

The script is structured to normalize user input, apply conversion logic based on the selected unit, and output all converted values in a clean, formatted way. The conversion logic was later refactored into a reusable function to separate processing from user interaction.

### 🧠 What I Learned

This script built on my understanding of CLI tools and introduced more structured logic flow and function-based design.

Key concepts I worked through:
- Using .lower() to normalize user input for consistent validation
- Applying conditional logic (if/elif) to handle multiple input states
- Understanding unit conversion formulas between Celsius, Fahrenheit, and Kelvin
- Introducing the concept of a “base unit” to simplify conversions
- Structuring logic around a pivot system (converting through a reference unit instead of direct mappings)
- Separating concerns between input handling, processing, and output formatting