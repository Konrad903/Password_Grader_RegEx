# Password Grader

A Python utility that evaluates the strength and security compliance of passwords using advanced Regular Expressions (`re`).

---

## Project Overview

The **Password Grader** script checks a list of test passwords against strict security criteria, ensuring they meet complexity requirements such as minimum length, uppercase letters, lowercase letters, numbers, and special characters[cite: 4].

---

## Features

* **Complex Regex Validation**: Employs a positive lookahead regex pattern (`r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'`) to enforce rigorous password policies[cite: 4].
* **Policy Enforcement**: Checks that each password contains at least one uppercase letter, one lowercase letter, one digit, one special character (`@#$%^&+=!`), and a minimum length of 8 characters[cite: 4].
* **Automated Batch Processing**: Iterates through a predefined array of sample passwords and prints out individual evaluation results[cite: 4].
* **Clean Terminal Feedback**: Clearly distinguishes between strong and weak passwords in the console output[cite: 4].

---

## Code Structure

* `pattern_check(password)`: Validates an individual password string against the security regex criteria[cite: 4].
* `result(pwd)`: Loops through a collection of passwords, runs the checker, and prints the corresponding status messages[cite: 4].
* `main()`: Sets up a list of sample passwords (both strong and weak) and initiates the validation routine[cite: 4].

---

## Requirements

* Python 3.x (Relies exclusively on Python's built-in `re` module; no external dependencies required)[cite: 4].

---

## Usage Instructions

1. Open your terminal or command prompt in the project folder.
2. Run the script using the command:
   ```bash
   python "Password Grader.py"
