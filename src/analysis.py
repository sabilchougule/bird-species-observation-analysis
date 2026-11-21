import os
import sqlite3
import pandas as pd

def get_db_connection():
    # Helper function to establish connection to the SQLite database
    db_path = os.path.join('database', 'bird_monitoring.db')
    conn = sqlite3.connect(db_path)
    return conn

def get_species_richness_by_habitat():
    """SQL Query 1: Total observations and unique species count by Habitat"""
    conn = get_db_connection()
    query = """
        SELECT 
            Habitat_Type,
            COUNT(DISTINCT Common_Name) AS Unique_Species_Count,
            COUNT(*) AS Total_Observations
        FROM bird_observations
        GROUP BY Habitat_Type;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_top_observed_species(top_n=10):
    """SQL Query 2: Most frequently recorded bird species"""
    conn = get_db_connection()
    query = f"""
        SELECT 
            Common_Name,
            Scientific_Name,
            Habitat_Type,
            COUNT(*) AS Sighting_Count
        FROM bird_observations
        WHERE Common_Name != 'Unknown Species'
        GROUP BY Common_Name, Habitat_Type
        ORDER BY Sighting_Count DESC
        LIMIT {top_n};
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_at_risk_watchlist_species():
    """SQL Query 3: Species flagged on the PIF Watchlist (Conservation Priorities)"""
    conn = get_db_connection()
    query = """
        SELECT 
            Common_Name,
            Scientific_Name,
            Habitat_Type,
            COUNT(*) AS Total_Sightings
        FROM bird_observations
        WHERE PIF_Watchlist_Status = 1
        GROUP BY Common_Name, Habitat_Type
        ORDER BY Total_Sightings DESC;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_weather_impact_summary():
    """SQL Query 4: Average temperature & humidity during observations by Park"""
    conn = get_db_connection()
    query = """
        SELECT 
            Admin_Unit_Code,
            Habitat_Type,
            ROUND(AVG(Temperature), 2) AS Avg_Temperature,
            ROUND(AVG(Humidity), 2) AS Avg_Humidity,
            COUNT(*) AS Total_Observations
        FROM bird_observations
        GROUP BY Admin_Unit_Code, Habitat_Type
        ORDER BY Total_Observations DESC;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    print("📊 Executing SQL Analysis Queries...\n")
    
    print("--- 1. Species Richness by Habitat ---")
    print(get_species_richness_by_habitat())
    
    print("\n--- 2. Top Observed Species ---")
    print(get_top_observed_species(5))
    
    print("\n--- 3. Top At-Risk Watchlist Species ---")
    print(get_at_risk_watchlist_species().head(5))