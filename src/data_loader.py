import os
import pandas as pd
import streamlit as st

# Step 1.1: Use Streamlit caching so raw data is loaded into memory only once
@st.cache_data
def load_raw_data():
    # Build file paths to source files inside the data/ directory
    forest_path = os.path.join('data', 'Bird_Monitoring_Data_FOREST.XLSX')
    grassland_path = os.path.join('data', 'Bird_Monitoring_Data_GRASSLAND.XLSX')

    # Step 1.2: Helper function to iterate through all park sheets inside an Excel workbook
    def merge_excel_sheets(file_path, habitat_name):
        excel_file = pd.ExcelFile(file_path)
        all_sheets = []

        for sheet in excel_file.sheet_names:
            # Read an individual park sheet into a DataFrame
            df_sheet = pd.read_excel(file_path, sheet_name=sheet)
            
            # Tag which habitat type this row belongs to
            df_sheet['Habitat_Type'] = habitat_name
            
            all_sheets.append(df_sheet)

        # Combine all sheet DataFrames into one consolidated dataset for this habitat
        return pd.concat(all_sheets, ignore_index=True)

    # Step 1.3: Execute reading for both Forest and Grassland files
    df_forest = merge_excel_sheets(forest_path, 'Forest')
    df_grassland = merge_excel_sheets(grassland_path, 'Grassland')

    return df_forest, df_grassland

if __name__ == "__main__":
    forest_df, grassland_df = load_raw_data()
    print("✅ Step 1 Complete!")
    print(f"Total Forest Records Loaded: {len(forest_df)}")
    print(f"Total Grassland Records Loaded: {len(grassland_df)}")