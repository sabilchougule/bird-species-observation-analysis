import os
import sys
import sqlite3
import pandas as pd

# Step 2.1: Add 'src' folder to Python path so relative imports work seamlessly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_loader import load_raw_data

def clean_and_store_data():
    print("🔄 Cleaning data and loading into SQLite database...")

    # Step 2.2: Load raw forest and grassland datasets from Step 1
    df_forest, df_grassland = load_raw_data()

    # Step 2.3: Fix column name discrepancies between Forest and Grassland
    df_grassland.rename(columns={'TaxonCode': 'NPSTaxonCode'}, inplace=True)

    # Combine both ecosystem DataFrames into one master dataset
    df_combined = pd.concat([df_forest, df_grassland], ignore_index=True)

    # Step 2.4: Clean Data Types and Handle Missing Values
    df_combined['Date'] = pd.to_datetime(df_combined['Date'], errors='coerce')
    df_combined['Observation_Year'] = df_combined['Date'].dt.year
    df_combined['Observation_Month'] = df_combined['Date'].dt.month_name()

    # Fill missing values in text columns with standardized labels
    df_combined['Sex'] = df_combined['Sex'].fillna('Undetermined')
    df_combined['Distance'] = df_combined['Distance'].fillna('Unknown')
    df_combined['Common_Name'] = df_combined['Common_Name'].fillna('Unknown Species')
    df_combined['Sky'] = df_combined['Sky'].fillna('Not Recorded')
    df_combined['Wind'] = df_combined['Wind'].fillna('Not Recorded')
    df_combined['Disturbance'] = df_combined['Disturbance'].fillna('No effect')

    # Convert status indicator columns into clean Boolean values (True/False)
    df_combined['PIF_Watchlist_Status'] = df_combined['PIF_Watchlist_Status'].fillna(False).astype(bool)
    df_combined['Regional_Stewardship_Status'] = df_combined['Regional_Stewardship_Status'].fillna(False).astype(bool)
    df_combined['Flyover_Observed'] = df_combined['Flyover_Observed'].fillna(False).astype(bool)

    # Fill missing weather metrics (Temperature & Humidity) using median values by Admin Unit
    df_combined['Temperature'] = df_combined.groupby('Admin_Unit_Code')['Temperature'].transform(lambda x: x.fillna(x.median()))
    df_combined['Humidity'] = df_combined.groupby('Admin_Unit_Code')['Humidity'].transform(lambda x: x.fillna(x.median()))

    # Step 2.5: Save cleaned dataset into SQLite Database
    db_dir = os.path.join('database')
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, 'bird_monitoring.db')

    # Write cleaned master dataset to SQL table 'bird_observations'
    conn = sqlite3.connect(db_path)
    df_combined.to_sql('bird_observations', conn, if_exists='replace', index=False)
    conn.close()

    print("✅ Step 2 Complete!")
    print(f"Master Cleaned Dataset Shape: {df_combined.shape} (Rows, Columns)")
    print(f"Cleaned Database successfully created at: {db_path}")

if __name__ == "__main__":
    clean_and_store_data()