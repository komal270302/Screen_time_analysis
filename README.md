# Screen Time Analysis using Python

## Overview
This project focuses on analyzing screen time data to determine the most frequently used apps over a specific period. It involves processing CSV data containing daily app rankings (Rank 1, Rank 2, Rank 3) and generating visualizations like bar charts and pie charts to provide insights into device usage patterns. This helps users evaluate if their time was spent productively, creatively, or otherwise.

## Motivation
Smartphone companies and users benefit from screen time reports to review activities on devices. This analysis highlights app usage trends, enabling better time management decisions. By examining data on how often apps appear in top ranks, the project reveals patterns such as dominant apps (e.g., WhatsApp, Instagram) and overall distribution.

## Features
1. Data Loading and Manipulation: Import CSV data, convert categorical ranks to dummy variables, and compute unique app lists using sets.
2. Usage Counting: Calculate the frequency of each app in ranks 1, 2, and 3, and aggregate total usage across all ranks.
3. Visualization: Create bar charts for individual rank counts and a pie chart for overall app usage distribution.
4. Data Cleaning: Drop irrelevant columns and sort results for clear insights.
5. Focus on Quality: Emphasizes efficient data processing and readability for sharing results.

## Technologies Used
1. Programming Language: Python
2. Data Processing: Pandas (for dataframes and manipulation), NumPy (for numerical operations)
3. Visualization: Plotly Express (interactive bar and pie charts), Seaborn, Matplotlib
4. Environment: Jupyter Notebook for development and experimentation
5. Data Source: CSV file with columns like Date, Rank 1, Rank 2, Rank 3

## Project Structure
The repository contains:
1. Screentime - App Ranking.csv: Sample dataset with dates and daily app ranks (e.g., WhatsApp, Instagram, Chrome).
2. screen_time_analysis.py: Main Python script for data import, processing, counting, and visualization.

## Setup and Installation
1. Clone the Repository: - git clone https://github.com/komal270302/Screen_time_analysis.git, 
                           cd Screen_time_analysis
2. Install Dependencies: Create a requirements.txt file with:
   pandas
   numpy
   plotly
   seaborn
   matplotlib
Then run : pip install -r requirements.txt
3. Configure Paths: Update the CSV file path in the script (e.g., pd.read_csv("path/to/Screentime - App Ranking.csv")).

## How to Run
Run the Analysis Script: Run python screen_time_analysis.py. This loads the CSV, computes app frequencies, and generates visualizations.
- Outputs: Console prints of counts, bar charts for each rank, and a pie chart for total usage.

Notes: The script uses Plotly for interactive plots; view them in a browser or Jupyter. For reproducibility, use the provided sample CSV or replace with your own screen time data.

## Results and Insights
1. App Frequencies: E.g., WhatsApp appears 22 times in Rank 1, Instagram 8 times in Rank 2.
2. Visuals: Bar charts show top apps per rank; pie chart displays overall distribution (e.g., WhatsApp ~30.9%, Instagram ~19.8%).
3. Example Output: Tables and charts reveal dominant apps like WhatsApp and social media trends.

## Contributor
Komal (komal202220@gmail.com) 
