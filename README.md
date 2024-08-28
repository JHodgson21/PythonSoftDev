# Weather Data Analysis

Weather Data Analysis is a Python project for loading, processing, and saving weather data from a CSV file.

## Installation

To get started, clone this repository and set up the virtual environment:

```bash
git clone https://github.com/yourusername/weather-analysis.git
cd weather-analysis
python -m venv venv

# On Windows
venv\Scripts\activate
# if you're on vs code and the env lights up green then it's already active. :)

# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```
# Usage

```python
import pandas as pd
from module1 import load_weather_data, save_weather_data

# Load the weather data
df = load_weather_data('C:/Users/Jakob/Desktop/Python SoftDev/PythonSoftDev/Weather Test Data.csv')

# Print the first few rows
print(df.head())

# Save the processed data
output_file_path = 'C:/Users/Jakob/Desktop/Python SoftDev/PythonSoftDev/processed_weather_data.csv'
save_weather_data(df, output_file_path)
```

# Documentation
Documentation is generated using pydoc and can be found in module1.html. To regenerate the documentation:
```bash
python -m pydoc -w module1
```