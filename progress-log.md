# Progress Log

A log of everything I learned about Python scripting throughout this project.

# Fundamentals (Core Python Scripting)

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

## 4. Password Generator

### 🛠️ What I Built

A random password generator that takes a password length from the user and generates a password using a pool of letters, numbers, and symbols.

### 🧠 What I Learned

- Worked with the `random` and `string` modules
- Used `string.ascii_letters`, `string.digits`, and `string.punctuation` to build a pool of characters
- Used `for _ in range` to repeat a task a specific number of times
- Using `random.choice()` to randomly select characters from a data pool
- Built a string iteratively by appending characters one at a time

## 5. Number Guessing Game

### 🛠️ What I Built

A replayable number guessing game that generates a random number (1-100) and gives the user 5 attempts to guess it, with feedback provided after each guess.

The game includes input validation, win/loss conditions, and replay functionality using nested loops and reuable game logic.

### 🧠 What I Learned

- Managing program state (`secret_number`, `guess`, and attempts)
- Using nested loops for both gameplay and replay functionality 
- Creating win/loss conditions with conditional logic
- Using `break` to exit loops when success conditions are met
- Asking for user input to control program flow (play again system)

# Intermediate (Data Handling & Automation Basics)

## 1. IP Ping Checker

### 🛠️ What I Built

An IP ping checker that takes a file path from the user, reads a list of IP addresses from the file, pings each one, and reports whether each host is online or offline.

### 🧠 What I Learned

- Using the `subprocess` library to run system commands and interact with the operating system
- Understanding how to use `subprocess.run()` to execute commands and capture results
- Using return codes to determine whether a command succeeded or failed
- Pinging IP addresses to check network connectivity
- Using `-c 1` to send a single ping packet on Linux/macOS systems
- Reading external data from a file and using it to drive automation

## 2. Log Parser

### 🛠️ What I Built

A log file parser that takes a file path from the user, reads the log entries line-by-line, filters out error messages, and extracts the timestamp and message from each error.

The script processes raw log text and transforms it into structured, readable output.

### 🧠 What I Learned

- Filtering text data using keyword matching (`"ERROR" in line`)
- Understanding how raw log data is structured
- Extracting specific fields (timestamp and message) from unstructured text
- Reconstructing meaningful output using `" ".join()`
- Transforming raw text data into structured, readable information

## 3. Web Scraper

### 🛠️ What I Built

A web scraper that takes a URL from the user, fetches the webpage content, parses the HTML using BeautifulSoup, and outputs all headings elements found on the page.

### 🧠 What I Learned

- Using the `requests` library to make HTTP requests and fetch web pages
- Understanding how web pages are returned as raw HTML
- Using `BeautifulSoup` to parse and structure HTML data
- Navigating HTML using DOM-style queries (e.g., selecting specific tags like `h1`)
- Working with unstructured web data and turning it into readable output

## 4. API Client

### 🛠️ What I Built

A simple REST API client that sends a request to a public API, receives JSON data, and extracts specific fields to display in a readable format.

### 🧠 What I Learned

- Understanding how REST APIs return structured JSON data
- Using `.json()` to convert API responses into Python dictionaries
- Accessing data using dictionary keys
- Working with structured remote data instead of raw text or HTML
- Extracting and displaying specific fields from an API response
