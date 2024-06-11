## Data Preparation for Cahoots Analysis

This Jupyter Notebook (`data_prep.ipynb`) cleans and preprocesses two datasets for analyzing Cahoots' activities:

1. **CAD Replication Data:** Data from the Computer-Aided Dispatch (CAD) system.
2. **CAD Diversions Data:** Data from the Computer-Aided Dispatch (CAD) system.

The notebook performs the following steps:

**Dataset 1: Replication Data** (data_prep.ipynb)

1.  **Import and Load:**
    *   Import necessary libraries.
    *   Load CAD data from `data/call_data_from_CAD.csv`.

2.  **Preprocess and Clean:**
    *   Convert call times to datetime objects and add a year column.
    *   Standardize Cahoots identifiers in call sign columns.
    *   Create a binary column `Cahoots_Related` indicating Cahoots involvement.
    *   Drop irrelevant columns.
    *   Sort data by `Call_Created_Time`.

3.  **Create Subset and Save:**
    *   Create a 2021-only dataset for replication purposes.
    *   Save both datasets to `data/cleaned_data/`. 


**2. Creating the CAD Diversions Dataset:**

1.  **Load and Prepare:**
    *   Load relevant columns from `data/call_data_from_CAD.csv`.
    *   Convert datetime objects.
    *   Filter for the years 2017-2021.
    *   Remove Disregards, duplicates, referrals, and cancellations.

2.  **Identify Exclusive Types:**
    *   Identify incident types and dispositions handled exclusively by either Cahoots or police.

3.  **Filter for Shared Types:**
    *   Filter the cleaned CAD data to include only shared incident and disposition types.

4.  **Calculate Proportions:**
    *   Calculate the proportion of Cahoots and police involvement for each incident type.

5.  **Identify "Substantial" Incident Types (Composite Score):**
    *   **Harmonic Mean of Proportions:** Calculate the harmonic mean to emphasize types with greater potential for diversion.
    *   **Scale Call Counts:** Apply a log transform to Cahoots and police call counts to prevent high-volume types from dominating.
    *   **Combine:** Multiply the harmonic mean by the sum of scaled call counts to obtain the composite score.
    *   **Normalize:** Apply Z-score normalization to the composite scores.
    *   **Threshold:** Incident types with a normalized score \> 1.5 are considered "substantial."

6.  **Filter and Save:**
    *   Create a filtered CAD dataset containing only substantial incident types.
    *   Save the filtered data to `"data/cleaned_data/cleaned_CAD_diversions.csv"`.

**Dependencies:**

- Python 3
- pandas
- pathlib
- scipy

**To run this notebook:**

1. Ensure the required dependencies are installed.
2. Place the raw data file (`call_data_from_CAD.csv`) in the `data` folder.
3. Execute the notebook cells sequentially. 

The cleaned datasets will be saved in the `data/cleaned_data` directory.
