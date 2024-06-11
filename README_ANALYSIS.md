## Analysis of Cahoots and EPD Data: Replicating and Extending the EPD's 2021 Evaluation

NOTE: `Analysis.ipynb` Includes all intermediate calculations that led to the conclusions presented in my final report. For a more polished view of my process, go to:

## https://nathan-m-burton.github.io/Cahoots-Impact-Assessment/


This Jupyter Notebook (`Analysis.ipynb`) replicates and extends the analysis conducted in the Eugene Police Department's (EPD) 2021 evaluation of Cahoots. It utilizes cleaned datasets created in `data_prep.ipynb`.

**Analysis Overview:**

1.  **Data Replication and Validation:**
    *   Reproduces the EPD's "Gross Diversion Rates" calculations to assess accuracy and identify methodological flaws.
    *   Investigates discrepancies between reported values and the underlying data.

2.  **Natural Experiment:**
    *   Conducts a natural experiment by analyzing welfare check data from 2016-2017 to estimate the true proportion of divertible calls.
    *   Compares the estimated diversion rates with the EPD's findings.

3.  **Overlapping Mandate Analysis:**
    *   Introduces the concept of the "Overlapping Mandate" to identify call types handled by both Cahoots and the police.
    *   Develops a composite scoring method to quantify the degree of overlap for each call type.
    *   Analyzes diversion rates within the overlapping mandate, highlighting potential areas for Cahoots expansion.

4.  **Temporal Analysis:**
    *   Examines the evolution of diversion rates over time (2017-2021) to identify trends and patterns.
    *   Explores potential reasons for fluctuations in diversion rates.

5.  **Call Type Breakdown:**
    *   Investigates diversion rates for specific call types within the overlapping mandate.
    *   Identifies opportunities and challenges for Cahoots expansion based on call type analysis.

**Dependencies:**

*   Python 3
*   pandas
*   matplotlib
*   squarify
*   numpy
*   hashlib

**To run this notebook:**

1.  Ensure the required dependencies are installed.
2.  Ensure the cleaned data files are present in the `data/cleaned_data` directory.
3.  Execute the notebook cells sequentially.

**Key Findings:**

*   The EPD's analysis contains methodological flaws, leading to an underestimation of Cahoots' diversion potential.
*   Our natural experiment suggests a much higher proportion of divertible calls than initially reported.
*   The concept of the "Overlapping Mandate" provides a more accurate framework for assessing Cahoots' impact.
*   Temporal and call type analysis reveal opportunities for Cahoots expansion and optimization of resource allocation.
