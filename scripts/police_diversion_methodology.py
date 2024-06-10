"""
This script recreates the methodology that the police used to analyze diversions in 2021. 
Changing the parameters will allow you to calculate the diversion rate methodology suggested by EPD based on different assumptions
to replicate the exact methodology of the original paper, specify your dataset and 0.74 for welfare_prop.
"""

import pandas as pd

def run_police_diversions(cleaned_data, welfare_prop, transport_prop=0, assist_prop=0, suicide_prop=0):
    # Filtering out the 'SELF' entries from the dataset
    data_filtered = cleaned_data[cleaned_data['Call_Source'] != 'SELF']

    # Dataset 1: ALL CAHOOTS ASSOCIATIONS
    cahoots_associations = data_filtered[data_filtered['Cahoots_related'] == 1]

    # Dataset 2: ALL CAHOOTS DISPATCHED CFS
    cahoots_dispatched = cahoots_associations.dropna(subset=['Call_First_Dispatched_Time'])
    cahoots_dispatched = cahoots_dispatched.drop_duplicates(subset='IncidentNumber', keep='first')
    
    # Dataset 4: ALL CAHOOTS ONLY ASSOCIATIONS
    cahoots_only_associations = cahoots_associations[(cahoots_associations['PrimaryUnitCallSign'] == "CAHOOT") & (cahoots_associations['IsPrimary'] == 1)]
    
    # Dataset 5: CAHOOTS ONLY ARRIVED CFS
    cahoots_only_arrived = cahoots_only_associations.dropna(subset=['Call_First_On_Scene'])
    cahoots_only_arrived = cahoots_only_arrived.drop_duplicates(subset='IncidentNumber', keep='first')
    
    # Dataset 6: Total CAHOOTS / EPD responses
    data_unique_incidents = data_filtered.drop_duplicates(subset='IncidentNumber', keep='first')
    combined_cahoots_epd_responses = data_unique_incidents[~(data_unique_incidents["Call_First_Dispatched_Time"].isna())] # Switch between dispatch and arrival
    
    # Calculate total calls
    total_calls = data_unique_incidents.shape[0]

    # Filter top 3 CAHOOTS CFS natures arrive
    top_3_natures = ['ASSIST PUBLIC- POLICE', 'CHECK WELFARE', 'TRANSPORT']
    top_3_cahoots_natures = cahoots_only_arrived[cahoots_only_arrived['InitialIncidentTypeDescription'].isin(top_3_natures)]
    top_3_cahoots_natures_count = top_3_cahoots_natures.shape[0]
    
    # Gross Divert Rates
    gross_divert_rate_1 = (cahoots_associations.shape[0] / total_calls) * 100
    gross_divert_rate_2 = (cahoots_dispatched.shape[0] / total_calls) * 100
    gross_divert_rate_3 = (cahoots_only_arrived.shape[0] / total_calls) * 100

    # Divert Rate without top 3 incident types 
    adjusted_cahoots_only_arrived = cahoots_only_arrived.shape[0] - top_3_cahoots_natures_count
    adjusted_divert_rate = (adjusted_cahoots_only_arrived / total_calls) * 100
    
    # Divert Rate without top 3 incident types Arrived only 
    adjusted_cahoots_police_arrived = ((cahoots_only_arrived.shape[0] - top_3_cahoots_natures_count) / 
                                          (combined_cahoots_epd_responses.shape[0] - top_3_cahoots_natures_count)) * 100

    # Applying 0.74 adjustment to Check Welfare calls
    likely_check_welfare_diverts_dispatch = (cahoots_dispatched[cahoots_dispatched["InitialIncidentTypeDescription"] == 'CHECK WELFARE'].shape[0]) * welfare_prop
    likely_transport_diverts_dispatch = (cahoots_dispatched[cahoots_dispatched["InitialIncidentTypeDescription"] == 'TRANSPORT'].shape[0]) * transport_prop
    likely_assist_diverts_dispatch = (cahoots_dispatched[cahoots_dispatched["InitialIncidentTypeDescription"] == 'ASSIST PUBLIC- POLICE'].shape[0]) * assist_prop
    likely_suicide_diverts = (cahoots_dispatched[cahoots_dispatched["InitialIncidentTypeDescription"] == 'SUICIDAL SUBJECT'].shape[0]) * suicide_prop
    
    
    likely_divert_sum = likely_check_welfare_diverts_dispatch + likely_transport_diverts_dispatch + likely_assist_diverts_dispatch + likely_suicide_diverts
    
    # low estimate
    adjusted_divert_rate_with_welfare = ((likely_divert_sum) / total_calls) * 100
    
    # High estimate
    adjusted_divert_rate_with_welfare_high = (likely_divert_sum / ((combined_cahoots_epd_responses.shape[0]) - (cahoots_dispatched.shape[0] - likely_divert_sum))) * 100
    
    # Final Results
    results = {
        "1a. Diversion Rate (Associations)": gross_divert_rate_1,
        "1b. Diversion Rate (Dispatches)": gross_divert_rate_2,
        "1c. Diversion Rate (CAHOOTS Only Arrivals)": gross_divert_rate_3,
        "2a. Diversion Rate (Removing CAHOOTS-Centric Calls)": adjusted_divert_rate,
        "2b. Diversion Rate (Removing CAHOOTS-Centric Calls, Dispatch only)": adjusted_cahoots_police_arrived,
        "3a. Diversion Rate (Adjusted for Check Welfare - All Calls)": adjusted_divert_rate_with_welfare,
        "3b. Diversion Rate (Adjusted for Check Welfare - Dispatched Calls)": adjusted_divert_rate_with_welfare_high
    }

    return {
        'cahoots_associations': cahoots_associations,
        'cahoots_dispatched': cahoots_dispatched,
        'cahoots_only_associations': cahoots_only_associations,
        'cahoots_only_arrived': cahoots_only_arrived,
        'total_cahoots_epd_responses': combined_cahoots_epd_responses,
        'results': results
    }

