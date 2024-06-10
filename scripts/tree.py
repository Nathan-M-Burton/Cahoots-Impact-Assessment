import matplotlib.pyplot as plt
import squarify
import numpy as np
import pandas as pd
import hashlib

target = 'InitialIncidentTypeDescription'

def process_data(data, top_n, group_others, target):
    value_counts = data[target].value_counts()
    total = value_counts.sum()
    if group_others:
        top_categories = value_counts.nlargest(top_n)
        other_sum = value_counts.iloc[top_n:].sum()
        if other_sum > 0:
            top_categories['Other'] = other_sum
    else:
        top_categories = value_counts.nlargest(top_n)
    return top_categories, total

def hash_to_index(text, num_colors):
    # Generate a hash for the text and map it to an index
    hash_val = int(hashlib.sha256(text.encode('utf-8')).hexdigest(), 16)
    return hash_val % num_colors

def create_treemap(data, title, top_n, group_others, max_legend_entries, show_labels, color_list, min_label_area_ratio=0.005):
    num_colors = len(color_list)
    top_data, total = process_data(data, top_n, group_others, target)
    
    color_map = {}
    assigned_colors = set()
    for label in top_data.index:
        index = hash_to_index(label, num_colors)
        original_index = index  
        while color_list[index] in assigned_colors:
            index = (index + 1) % num_colors
            if index == original_index:
                break  
        color_map[label] = color_list[index]
        assigned_colors.add(color_list[index])
    
    fig, ax = plt.subplots(figsize=(15, 6))
    sizes = top_data.values
    colors = [color_map[label] if label in color_map else '#CCCCCC' for label in top_data.index]  # Default color for 'Other'
    labels = [f"{incident}\n({value / total * 100:.1f}%)" for incident, value in top_data.items()]
    
    squarify.plot(sizes=sizes, label=["" for _ in sizes], color=colors, alpha=0.8, pad=False, ec='black', text_kwargs={'fontsize': 'smaller'})
    plt.title(title)
    plt.axis('off')

    total_area = sum([rect.get_width() * rect.get_height() for rect in ax.patches])
    for text, rect in zip(labels, ax.patches):
        # Only show label if the area of the box is greater than a certain percentage of the total area
        area_ratio = (rect.get_width() * rect.get_height()) / total_area
        if area_ratio > min_label_area_ratio:
            ax.text(rect.get_x() + rect.get_width()/2, rect.get_y() + rect.get_height()/2, text, ha='center', va='center', fontsize=max(8, min(14, area_ratio * total_area / 100)))

    # Legend
    patches = [plt.Rectangle((0, 0), 1, 1, facecolor=color_map[incident]) for incident in top_data.index]
    legend_labels = [f"{incident} ({value / total * 100:.2f}%)" for incident, value in top_data.items()]
    #plt.legend(patches, legend_labels[:max_legend_entries], loc='upper left', bbox_to_anchor=(1, 1), title="Incident Types")

    plt.show()

