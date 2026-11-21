# 🦅 Bird Species Observation Analysis & Ecosystem Impact Analytics

An end-to-end data engineering and interactive analytics project analyzing bird species observations across **Forest** and **Grassland** ecosystems across 11 administrative park units. Built in **VS Code** using **Python, Pandas, SQLite, Plotly, and Streamlit**.

---

## 🌐 Live Streamlit Web App

* **Streamlit Cloud Portal**: [https://share.streamlit.io](https://share.streamlit.io)
* **Live App URL (after deploying on Streamlit Community Cloud)**: `https://<your-github-username>-bird-species-observation-analysis-app.streamlit.app/`
* **Local URL (when running locally)**: `http://localhost:8501`

---

## 📌 Project Overview

This project consolidates multi-sheet observational datasets from forest and grassland monitoring programs, cleans and standardizes observational and environmental attributes, stores the processed dataset in a local SQLite database (`database/bird_monitoring.db`), and delivers a **12-tab interactive Streamlit dashboard** equipped with real-time filters and business decision-support insights.

### Key Business Use Cases
* **Wildlife Conservation**: Identify at-risk species (PIF Watchlist) and critical habitats requiring targeted protection.
* **Land Management**: Compare forest vs. grassland species guilds to support sustainable land and agricultural buffer planning.
* **Eco-Tourism**: Highlight peak seasonal windows and high-sighting anchor species for guided bird-watching tours.
* **Survey & Operational Efficiency**: Evaluate detection speed, repeat visit yields, and disturbance effects to optimize field monitoring workflows.

---

## 🗂️ Project Structure

```text
bird_species_analysis/
├── data/
│   ├── Bird_Monitoring_Data_FOREST.XLSX
│   └── Bird_Monitoring_Data_GRASSLAND.XLSX
├── database/
│   └── bird_monitoring.db          # Generated SQLite database
├── src/
│   ├── __init__.py
│   ├── data_loader.py              # Reads & merges all sheets across Forest & Grassland workbooks
│   ├── data_cleaner.py             # Cleans schema/missing values & writes to SQLite
│   └── analysis.py                 # Standalone SQL queries & summary metrics
├── app.py                          # 12-dashboard Streamlit application
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Execution

### 1. Create and Activate Virtual Environment
```bash
python -m venv venv
```
* **Windows (PowerShell)**: `.\venv\Scripts\Activate.ps1`
* **Windows (CMD)**: `venv\Scripts\activate.bat`
* **Mac / Linux**: `source venv/bin/activate`

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Pipeline & Launch Dashboard
```bash
# Step 1: Test raw data loading
python src/data_loader.py

# Step 2: Clean data and populate SQLite database
python src/data_cleaner.py

# Step 3: Run standalone SQL analysis checks
python src/analysis.py

# Step 4: Launch the Streamlit dashboard
streamlit run app.py
```

---

## 📊 Dashboard Suite (12 Interactive Views)

1. **Species Abundance**: Top observed bird species with a dynamic slider.
2. **Conservation Risk**: PIF Watchlist species breakdown and at-risk sightings.
3. **Habitat Partitioning**: Forest vs. Grassland observation counts and park-level distributions.
4. **Seasonal Trends**: Yearly and monthly observation patterns across habitats.
5. **Biodiversity Matrix**: Park unit comparison of total sightings vs. unique species richness.
6. **Climate Correlation**: Temperature vs. humidity scatter analysis across habitats.
7. **Detection Modality**: Auditory (*Singing*, *Calling*) vs. visual (*Visualization*) identification breakdown.
8. **Human Disturbance**: Impact of disturbance levels on sighting counts.
9. **Initial 3-Min Rate**: Proportion of detections recorded within the initial three-minute interval.
10. **Site Repeat Visits**: Sighting volume across sequential visits (`Visit 1`, `Visit 2`, `Visit 3`).
11. **Observer Efficiency**: Observation volume distribution by field observer.
12. **Master Data Explorer**: Filterable table of cleaned observation records.