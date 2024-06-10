import pandas as pd
import matplotlib.pyplot as plt
def calculate_prop(data_2016, data_2017, types):
    dict_2016 = data_2016[data_2016["InitialIncidentTypeDescription"].isin(types)]["InitialIncidentTypeDescription"].value_counts().to_dict()
    dict_2017 = data_2017[data_2017["InitialIncidentTypeDescription"].isin(types)]["InitialIncidentTypeDescription"].value_counts().to_dict()
    print(f"2016: {dict_2016}")
    print(f"2017: {dict_2017}")
    
    final_dict = {}
    for incident in dict_2016:
        final_dict[incident] = dict_2016[incident] / dict_2017[incident]
    return final_dict
        

def create_diversion_rate_chart(data, rate_key, low_estimate_key=None, 
                                 title=None, rate_label=None, low_estimate_label='Low Estimate'):
    """
    Creates a stacked bar chart showing diversion rates by year.

    Args:
        data (dict): A dictionary where keys are years and values are
                     dictionaries containing diversion rate information.
        rate_key (str): The key for the diversion rate to plot.
        low_estimate_key (str, optional): The key for the low-end estimate 
                                           to add as a line. If None, no line 
                                           is added. Defaults to None.
        title (str, optional): Title for the plot. If None, a default title is used.
        rate_label (str, optional): Label for the main rate in the legend. 
                                    If None, the `rate_key` is used as the label.
        low_estimate_label (str, optional): Label for the low estimate line 
                                            in the legend. Defaults to 'Low Estimate'.
    """

    years = list(data.keys())
    rates = list(data.values())

    selected_rates = [rate[rate_key] for rate in rates]

    plt.figure(figsize=(10, 6))

    plt.bar(years, selected_rates, label=rate_label if rate_label else rate_key, color='darkorange')
    plt.bar(years, [100 - r for r in selected_rates], bottom=selected_rates, label='Police', color='lightblue')

    if low_estimate_key:
        low_estimates = [rate[low_estimate_key] for rate in rates]
        low_end_lines = plt.hlines(
            low_estimates,
            xmin=[y - 0.4 for y in years],
            xmax=[y + 0.4 for y in years],
            color='black',
            linewidth=1,
        )

        plt.legend(handles=[low_end_lines] + plt.gca().get_legend_handles_labels()[0],
                   labels=[low_estimate_label] + plt.gca().get_legend_handles_labels()[1],
                   loc='upper left', bbox_to_anchor=(1, 1))
    else:
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.xlabel('Year')
    plt.ylabel('Diversion Rate (%)')
    plt.title(title if title else f'Diversion Rates Over Time ({rate_key})')
    plt.xticks(years)
    plt.ylim(0, 100)

    # Add percentage labels 
    for year, high, low in zip(years, selected_rates, low_estimates if low_estimate_key else [0]*len(years)):
        plt.text(year, 20, f'{high:.1f}%', ha='center', va='center', color='black')
        #plt.text(year, (low + 3), f'{low:.1f}%', ha='center', va='center', color='black') 

    plt.tight_layout()
    plt.show()
