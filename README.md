# RTF Word Extractor Based on Characters

This repository contains a Python script to process RTF files, extract words containing specific characters, and output the results to a CSV file.

## Features

- Extracts words containing specific characters from RTF files.
- Tracks occurrences across multiple groups/files.
- Outputs results to a CSV file.

## Usage

1. Place your `.rtf` files in the working directory.
2. Update the file paths in the `main()` function if needed.
3. Run the script:
   ```bash
   python main.py
   ```
4. The output will be saved as word_bank.csv.

# CSV Format
- Word: The extracted word.
- Character: The first matching special character in the word.
- Groups: Columns corresponding to each processed group (e.g., "First File", "Second File").

# Notes
This project is not actively maintained.
Feel free to use the code for inspiration or as a base for your own projects.

# Contributing
This repository is not open for contributions. However, you are welcome to fork it and adapt it to your needs.
