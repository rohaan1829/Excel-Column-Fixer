# Excel Column Fixer

This project helps you clean and standardize country and region names in an Excel file column using Python and pandas. It scans a specified column for country names, regions, and US states, then extracts and lists them in a clean format.

## Features
- Reads an Excel file (`data.xlsx`) with a column containing country/region/state names.
- Identifies and extracts known country, region, and US state names from the column.
- Cleans the column by removing duplicates and extra text.
- Saves the cleaned data to a new Excel file (`data_fixed.xlsx`).

## How It Works
1. The script loads `data.xlsx` using pandas.
2. It scans the specified column (default: `Region`) for known country, region, and US state names.
3. Extracted names are listed in a comma-separated format.
4. The cleaned data is saved to `data_fixed.xlsx`.

## Usage
1. Place your Excel file as `data.xlsx` in the project folder.
2. Edit the `col` variable in `script.py` to match your target column name (default is `Region`).
3. Run the script:
   ```powershell
   # Activate your virtual environment if needed
   .\env\Scripts\Activate.ps1
   # Run the script
   python script.py
   ```
4. Find the cleaned file as `data_fixed.xlsx` in the same folder.

## Requirements
- Python 3.7+
- pandas
- openpyxl

Install dependencies (if not already installed):
```powershell
.\env\Scripts\Activate.ps1
pip install pandas openpyxl
```

## Customization
- Extend the `country_list` in `script.py` to include more countries or regions as needed.
- Change the column name by editing the `col` variable.

## Repository Structure
- `script.py` — Main script for cleaning the Excel column
- `data.xlsx` — Input Excel file
- `data_fixed.xlsx` — Output Excel file
- `.gitignore` — Excludes `env` and Python cache files
- `env/` — Python virtual environment (excluded from git)

## License
This project is open source and free to use.
