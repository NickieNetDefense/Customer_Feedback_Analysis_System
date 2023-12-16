import os
import pandas as pd
import datetime
import re

def load_data(directory_path):
    """
    Load data from a CSV file in the specified directory.
    :param directory_path: str - The path to the directory containing CSV files.
    :return: DataFrame - The loaded data.
    """
    # Get a list of CSV files in the directory
    csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]

    # Check if there are any CSV files in the directory
    if not csv_files:
        raise FileNotFoundError("No CSV files found in the specified directory.")

    # Select the most recent CSV file based on the file name
    most_recent_file = max(csv_files)

    # Load the selected CSV file into a DataFrame
    file_path = os.path.join(directory_path, most_recent_file)
    return pd.read_csv(file_path)

def prepare_data(df):
    """
    Perform data preparation on the DataFrame.
    :param df: DataFrame - The DataFrame to be prepared.
    :return: DataFrame - The prepared DataFrame.
    """
    # Additional data preparation steps can be added here

    return df

def save_prepared_data(df, output_directory):
    """
    Save the prepared data to a CSV file in the specified directory.
    :param df: DataFrame - The prepared DataFrame.
    :param output_directory: str - The directory where the prepared data should be saved.
    """
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    output_filename = os.path.join(output_directory, f'data_prepared_{current_date}.csv')
    df.to_csv(output_filename, index=False)
    print(f"Prepared data saved to: {output_filename}")

if __name__ == "__main__":
    directory_path = r'C:\Users\e_nic\Desktop\My Projects\customer feedback analysis system\Customer_Feedback_Analysis_System'
    data = load_data(directory_path)
    prepared_data = prepare_data(data)
    save_prepared_data(prepared_data, directory_path)
    print("Data preparation complete.")
