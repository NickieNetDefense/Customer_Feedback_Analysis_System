import pandas as pd
import datetime

def load_data(file_path):
    """
    Load data from a CSV file into a DataFrame.
    :param file_path: str - The path to the CSV file.
    :return: DataFrame - The loaded data.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Perform basic data cleaning on the DataFrame.
    :param df: DataFrame - The DataFrame to be cleaned.
    :return: DataFrame - The cleaned DataFrame.
    """
    # Handling missing values
    df = df.dropna()

    # Removing duplicate entries
    df = df.drop_duplicates()

    # Additional cleaning steps can be added here

    return df

def save_cleaned_data(df, file_path):
    """
    Save the cleaned data to a CSV file.
    :param df: DataFrame - The DataFrame to be saved.
    :param file_path: str - The path to the output CSV file.
    """
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    input_file = r'C:\Users\e_nic\Desktop\My Projects\customer feedback analysis system\Customer_Feedback_Analysis_System\google_places_raw_20231215.csv'
    current_date = datetime.datetime.now().strftime("%Y%m%d")  # Format: YYYYMMDD
    output_file = r'C:\Users\e_nic\Desktop\My Projects\customer feedback analysis system\Customer_Feedback_Analysis_System\google_clean_data_{}.csv'.format(current_date)

    data = load_data(input_file)
    cleaned_data = clean_data(data)
    save_cleaned_data(cleaned_data, output_file)
    print("Data cleaning complete. Cleaned data saved to:", output_file)
