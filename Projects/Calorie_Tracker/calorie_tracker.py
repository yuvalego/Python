import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import os
data_file_name = 'Nutrient_Totals.csv'
image_file_name = 'Nutrient_Data_Summery.jpeg'
# system of logging data to the users computer with a csv
# find the correct file in the users computer or create a new one
def add_data(data_file_name, data):
    cwd = os.getcwd()
    files_in_cwd = list(os.walk(f'{cwd}/Nutrition_App_Data'))[0]

    if data_file_name not in files_in_cwd:
        pd.DataFrame(data).to_csv(data_file_name, index=False)

    else:
        current_data = pd.read_csv(data_file_name)
        current_data = pd.concat([current_data, data], ignore_index=True)
        current_data.to_csv(data_file_name)
# a way to display the collected data in an interactive way
def save_data_image(data_file_name, image_file_name):
    df = pd.read_csv(f'Nutrition_App_Data/{data_file_name}')
    df.index = range(1, df.shape[0] + 1)
    index = list(df.index)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 5), dpi=200)

    colors = {
        'blue': '#6699cc',
        'green': '#66cc66',
        'red': '#cc6666',
        'purple': '#cc66cc'
    }

    ax1.plot(index, df['Calories'], '-o', color=colors['blue'])
    ax1.tick_params(direction='in')
    ax1.grid(True, linestyle='--', alpha=0.45)
    ax1.set_ylabel('Calories (kcal)')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    ax2.plot(index, df['Proteins'], 'o-', color=colors['green'])
    ax2.tick_params(direction='in')
    ax2.grid(True, linestyle='--', alpha=0.45)
    ax2.set_ylabel('Protein (g)')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    ax3.plot(index, df['Carbohydrates'], 'o-', color=colors['red'])
    ax3.tick_params(direction='in')
    ax3.grid(True, linestyle='--', alpha=0.45)
    ax3.set_xlabel('Day')
    ax3.set_ylabel('Carbohydrates (g)')
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)

    ax4.plot(index, df['Fats'], 'o-', color=colors['purple'])
    ax4.tick_params(direction='in')
    ax4.grid(True, linestyle='--', alpha=0.45)
    ax4.set_xlabel('Day')
    ax4.set_ylabel('Fats (g)')
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(image_file_name, dpi=200)