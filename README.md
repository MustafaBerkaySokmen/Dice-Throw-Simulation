# Dice Throw Simulation

## Overview
The **Dice Throw Simulation** is a Python program designed to simulate 10,000 dice throws. It records the results of each throw, writes the outcomes to a file, and calculates the frequency distribution of the sums of dice rolls. The program provides insights into the probabilities of different outcomes.

## Features
- Simulates two dice throws for a specified number of iterations.
- Records and saves the results to a text file in a formatted manner.
- Calculates the frequency distribution for sums of dice rolls.
- Provides probabilities for each possible sum (2 through 12).

## Installation
To run this project, ensure you have **Python 3.x** installed on your system.

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/dice-throw-simulation.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd dice-throw-simulation
   ```
3. **Run the script:**
   ```bash
   python ThrowDice.py
   ```

## Usage
1. The program contains the following primary functions:
   - `throw_single_die()`: Simulates a single die throw (returns a random integer between 1 and 6).
   - `record_dice_throws(throws)`: Records the results of 10,000 dice throws in a dictionary.
   - `write_dict_to_file(throws_dict)`: Writes the results to a file named `diceresults.txt`.
   - `calculate_frequencies(throws_dict)`: Calculates and returns the probabilities for each sum (2 through 12).
2. Modify the number of throws in the `main()` function if needed.
3. Running the script prints the results and saves the output to a file.

## Example Output
```
Dice Throw Results:
{(1, 1): 277, (1, 2): 542, ..., (6, 6): 300}

Probabilities:
[(2, 0.0277), (3, 0.0554), (4, 0.0832), ..., (12, 0.03)]
```

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.

