# TxGRAFFITI

TxGRAFFITI is a Python-based program for mathematical conjecturing, especially tailored towards graphs. The program conjectures on various mathematical objects based on data provided. The conjecturing program is interactive and user-friendly.

## Version

1.0.0

## Author

Randy Davila, 2023

## Features

- Conjectures on various mathematical data.
- Can focus on single or multiple properties.
- Utilizes the Dalmatian function for conjecturing on data.

## Installation

Clone the repository to your local machine.

```bash
git clone https://github.com/RandyRDavila/TxGraffiti.git
```

Install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

The main interaction with the program is through the main.py file. Run this file using Python.

```bash
python main.py
```

Upon execution, you'll be prompted to input the name (`graphs` for graph conjectures) of the CSV file containing the data to conjecture on. The file should be placed in the `math_data/data/` directory and you only need to enter the name without the `.csv` extension.

After reading the file, the program presents a list of numerical invariants detected from the file. You'll then select one invariant to conjecture on.

Next, you can choose to focus the conjecture on a single property or consider multiple properties. If you choose a single property, the program will prompt you to select one from the list of Boolean properties.

Finally, you can choose to apply the Dalmatian function to the data, after which the program will generate and print out the conjectures based on your choices.

## Contributing

Contributions are welcome. Please fork the project and create a pull request with your changes.

## License

Copyright © 2023 Randy Davila
