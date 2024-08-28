import os
import pandas as pd

def load_weather_data(file_path: str) -> pd.DataFrame:
    """
    Load weather data from the CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the weather data.

    Returns:
    pd.DataFrame: A DataFrame containing the weather data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    return pd.read_csv(file_path)

def save_weather_data(df: pd.DataFrame, output_file_path: str) -> None:
    """
    Save weather data to a CSV file.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the weather data.
    output_file_path (str): The path where the CSV file will be saved.
    """
    df.to_csv(output_file_path, index=False)
    print(f"Data successfully saved to {output_file_path}")

# Load data (make sure the file path is correct)
df = load_weather_data('C:/Users/Jakob/Desktop/Python SoftDev/PythonSoftDev/Weather Test Data.csv')

# Print the first few lines to verify it works
print(df.head())

# Not sure if we need to do this but here is how to save data to a new CSV file.
output_file_path = 'C:/Users/Jakob/Desktop/Python SoftDev/PythonSoftDev/processed_weather_data.csv'
save_weather_data(df, output_file_path)

