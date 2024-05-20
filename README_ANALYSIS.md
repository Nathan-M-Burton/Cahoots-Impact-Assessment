```
## Analysis of Cahoots Data

This Jupyter Notebook (`Analysis.ipynb`) analyzes the cleaned datasets created in `data_prep.ipynb`.

**Analysis:**

1. **Proportion of Calls by Year:**
   - Calculates the proportion of calls handled by Cahoots vs. police each year.
   - Creates a stacked bar chart visualizing these proportions.
   - Labels the Cahoots portion of each bar with the percentage.

2. **Incident Type Visualization:**
   - Uses the `create_treemap` function to generate treemaps showing the distribution of:
     - Incident types handled by Cahoots.
     - Incident types handled by police.
   - The function allows customization:
     - `top_n`: Number of top categories to display.
     - `group_others`: Whether to group remaining categories as "Other".
     - `max_legend_entries`: Maximum entries in the legend.
     - `show_labels`: Whether to display labels on the treemap.
     - `color_list`: List of colors for visualization.
   - **`hash_to_index` function:**
      - This function ensures consistent color assignment for incident types across different treemaps. 
      - It takes the incident type label as input and generates a unique hash value using the SHA256 algorithm. 
      - This hash value is then converted to a color index within the provided `color_list`, ensuring each incident type is mapped to the same color whenever it appears.

3. **Calls with Overlapping Mandates:**
   - Filters out transports and counseling from the Cahoots dataset and arrests/transports from the CAD dataset.
   - Calculates and plots the proportion of calls with overlapping mandates handled by Cahoots vs. police each year.
   - Identifies and visualizes the top 5 incident types with overlapping mandates.
   - Generates treemaps for incident types with overlapping mandates handled by Cahoots and police.

**Dependencies:**

- Python 3
- pandas
- matplotlib
- squarify
- numpy
- hashlib

**To run this notebook:**

1. Ensure the required dependencies are installed.
2. Ensure the cleaned data files (`cleaned_CAD_data.csv`, `cleaned_cahoots_data.csv`, and `cleaned_CAD_diversions.csv`) are present in the `data/cleaned_data` directory.
3. Execute the notebook cells sequentially. 

```

