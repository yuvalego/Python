import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
import os

def center_window(root):
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = root.winfo_width()
    window_height = root.winfo_height()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

def quit_program(root):
    root.quit()
    root.destroy()

def main_page():
    root = tk.Tk()
    root.title('Nutrition Tracker')

    show_data = tk.Button(
        root, 
        text='Show Data', 
        padx=10, pady=5, 
        command=lambda: photo_window(root))
    
    new_log = tk.Button(
        root, 
        text='New Entry', 
        padx=10, pady=5, 
        command=lambda: input_window(root))
    
    quit_button = tk.Button(
        root, 
        text='Close', 
        command=lambda: quit_program(root), 
        padx=85, pady=2)

    show_data.grid(column=1, row=1)
    new_log.grid(column=2, row=1)
    quit_button.grid(column=1, row=2, columnspan=2)

    center_window(root)

    root.mainloop() 

def back_to_main(window, parent_window):
    window.destroy()
    parent_window.deiconify()

def add_data(data_file_name, data):
    cwd = os.getcwd()
    files_in_cwd = list(os.walk(cwd))[0][2]
    data = pd.DataFrame(data)

    if data_file_name not in files_in_cwd:
        new_log = pd.DataFrame(data)
        new_log.to_csv(data_file_name, index=False)

    else:
        current_data = pd.read_csv(data_file_name)
        current_data = pd.concat([current_data, data], axis=0, ignore_index=True)
        current_data.to_csv(data_file_name, index=False)

def log(cal_entry, pro_entry, car_entry, fat_entry):
    nutrition_totals = {
        'Calories': [int(cal_entry.get())], 
        'Proteins': [int(pro_entry.get())], 
        'Carbohydrates': [int(car_entry.get())],
        'Fats': [int(fat_entry.get())]
        }
    cal_entry.delete(0, tk.END)
    pro_entry.delete(0, tk.END)
    car_entry.delete(0, tk.END)
    fat_entry.delete(0, tk.END)

    add_data('Nutrient_Totals.csv', nutrition_totals)

def input_window(root):
    root.withdraw()
    input_root = tk.Toplevel(root)
    input_root.title('Input Log')
    input_root.geometry('260x150')

    cal_lable = tk.Label(input_root, text='Calories: ')
    pro_lable = tk.Label(input_root, text='Protein:  ')
    car_lable = tk.Label(input_root, text='Carbs:    ')
    fat_lable = tk.Label(input_root, text='Fats:     ')

    cal_entry = tk.Entry(input_root, borderwidth=3)
    pro_entry = tk.Entry(input_root, borderwidth=3)
    car_entry = tk.Entry(input_root, borderwidth=3)
    fat_entry = tk.Entry(input_root, borderwidth=3)

    back_button = tk.Button(
        input_root, 
        text='<--', 
        padx=5, pady=1.5,
        command=lambda: back_to_main(input_root, root))
    
    add_button = tk.Button(input_root, 
                           text='Log', 
                           padx=69, pady=1.5, 
                           command=lambda: log(cal_entry, 
                                               pro_entry, 
                                               car_entry, 
                                               fat_entry))

    cal_lable.grid(column=1, row=1)
    pro_lable.grid(column=1, row=2)
    car_lable.grid(column=1, row=3)
    fat_lable.grid(column=1, row=4)

    cal_entry.grid(column=2, row=1, columnspan=2)
    pro_entry.grid(column=2, row=2, columnspan=2)
    car_entry.grid(column=2, row=3, columnspan=2)
    fat_entry.grid(column=2, row=4, columnspan=2)

    back_button.grid(column=1, row=5)
    add_button.grid(column=2, row=5, columnspan=2)

    center_window(input_root)
    input_root.protocol("WM_DELETE_WINDOW", lambda: back_to_main(input_root, root))

def save_data_image(data_file_name, image_file_name):
    df = pd.read_csv(data_file_name)
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

def photo_window(root):
    root.withdraw()
    photo_root = tk.Toplevel(root)
    photo_root.title('My Daily Stats')

    data_file_name = 'Nutrient_Totals.csv'
    image_name = 'Nutrient_Data_Summery.jpeg'
    save_data_image(data_file_name, image_name)
    image = Image.open(image_name)

    width, height = image.size
    image = image.resize((width//4, height//4), Image.BICUBIC)

    stats_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(photo_root, image=stats_image)
    image_label.image = stats_image
    image_label.pack()

    center_window(photo_root)
    photo_root.protocol("WM_DELETE_WINDOW", lambda: back_to_main(photo_root, root))

main_page()