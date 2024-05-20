```
## Data Preparation for Cahoots Analysis

This Jupyter Notebook (`data_prep.ipynb`) cleans and preprocesses two datasets for analyzing Cahoots' activities:

1. **CAD Data:** Data from the Computer-Aided Dispatch (CAD) system.
2. **Cahoots Data:** Data directly from the Cahoots organization. 

The notebook performs the following steps:

**1. Cleaning the CAD Data:**

   - Imports necessary libraries 
   - Loads CAD data from `"data/call_data_from_CAD.csv"`.
   - Selects relevant columns and converts call times to datetime objects.
   - Standardizes Cahoots identifiers in call sign columns.
   - Creates a binary column `Handled_by_Cahoots` indicating Cahoots involvement.
   - Removes irrelevant records based on 'Disposition' values (disregards, duplicates, cancellations, referrals, relays, and data from 2023).
   - Sorts data by `Call_Created_Time`.
   - Saves the cleaned CAD data to `"data/cleaned_data/cleaned_CAD_data.csv"`.

**2. Cleaning the Cahoots Data:**

   - Loads Cahoots data from `"data/call_data_from_CAHOOTS_2021_2022.xlsx"`.
   - Drops rows with missing "Reason for Dispatch".
   - Combines "Date" and "TimeOfCall" into a single "DateTime" column.
   - Filters data for calls from Eugene only to match the CAD data.
   - Selects only the "DateTime" and "Reason for Dispatch" columns.
   - Saves the cleaned Cahoots data to `"data/cleaned_data/cleaned_cahoots_data.csv"`.

**3. Creating the CAD Diversions Dataset:**

   - Identifies incident types and dispositions exclusively handled by either Cahoots or police.
   - Filters the cleaned CAD data to include only shared incident and disposition types.
   - Calculates the proportion of Cahoots and police involvement for each incident type.
   - **Computes a composite score for each incident type to identify "substantial" incident types, where there is significant overlap in response between both Cahoots and Police.** This is done using the following steps:
     - **Calculate the Harmonic Mean of Proportions:** The harmonic mean is used because it is sensitive to situations where either Cahoots or police handle a very low proportion of calls for a specific type. This highlights types where there is potential for greater diversion to Cahoots.
     - **Scale Call Counts:** To prevent incident types with very high call volumes from dominating the score, the raw call counts for both Cahoots and police are scaled using the square root.
     - **Combine Harmonic Mean and Scaled Counts:** The harmonic mean proportion is multiplied by the sum of the scaled Cahoots and police call counts to create the final composite score.
   - **Normalize Composite Scores:**  Z-score normalization is applied to the composite scores to standardize them and allow for comparisons across different incident types.
   - **Identify Substantial Incident Types:** Incident types with a normalized composite score greater than 0.5 are considered substantial, indicating significant shared responsibility between Cahoots and police. 
   - Creates a filtered CAD dataset containing only the substantial incident types.
   - Saves the filtered CAD data to `"data/cleaned_data/cleaned_CAD_diversions.csv"`.

**Dependencies:**

- Python 3
- pandas
- pathlib
- scipy

**To run this notebook:**

1. Ensure the required dependencies are installed.
2. Place the raw data files (`call_data_from_CAD.csv` and `call_data_from_CAHOOTS_2021_2022.xlsx`) in the `data` folder.
3. Execute the notebook cells sequentially. 

The cleaned datasets will be saved in the `data/cleaned_data` directory.
``` 
