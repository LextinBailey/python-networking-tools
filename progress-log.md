# Progress Log

A log of everything I learned about Python scripting throughout this project.

## 1. Tip Calculator

### 🛠️ What I Built

A tip calculator that takes a bill amount and tip percentage from the user, validates the input, performs the calculation, and prints a formatted result with currency styling.

### 🧠 What I Learned

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

A temperature converter that takes a numeric temperature value and a unit (Celsius, Fahrenheit, or Kelvin) from the user, validates the input, and converts it into the other two temperature scales.

### 🧠 What I Learned

- Using `.lower()` to normalize user input for consistent validation
- Applying conditional logic (`if/elif`) to handle multiple input states
- Understanding unit conversion formulas between Celsius, Fahrenheit, and Kelvin
- Introducing the concept of a “base unit” to simplify conversions
- Structuring logic around a pivot system (converting through a reference unit instead of direct mappings)
- Separating concerns between input handling, processing, and output formatting

## 3. CSV Reader

### 🛠️ What I Built

A CSV reader that takes a CSV file path from the user, reads it line-by-line, separates each line into data fields, and outputs a clean formatted version of the data.

### 🧠 What I Learned

- Using `open()` to open a file for reading
- Using `"r"` for read mode
- Using `with` to automatically close the file
- Processing files line-by-line with `readlines()`
- Removing whitespace and newlines characters using `strip()`
- Splitting lines into usable data fields using `split(",")`
- Understanding how raw text becomes structured data
- Using defensive programming to skip empty lines
- Handling incomplete or invalid rows safely instead of breaking the script
- Printing/logging invalid data instead of letting the program crash