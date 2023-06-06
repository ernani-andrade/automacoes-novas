import os
import tabula
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tabula.io import read_pdf

def select_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(tk.END, input_folder)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(tk.END, output_folder)

def process_files():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()

    # Create a loading screen
    loading_screen = tk.Toplevel(root)
    loading_screen.title("Loading")
    loading_label = tk.Label(loading_screen, text="Carregando Dados...")
    loading_label.pack()

    # Loop through all PDF files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            print(f'Processing file: {file_name}')
            pdf_path = os.path.join(input_folder, file_name)

            # Loop through the coordinates and extract the tables
            for coord in coordinates:
                pages = coord["pages"]
                area = coord["area"]

                # Extract the table using tabula
                dfs = read_pdf(pdf_path, pages=pages, area=area)

                if dfs:
                    combined_table = pd.concat(dfs)

                    # Generate output file name based on the PDF file name
                    output_file_name = f'Table_{os.path.splitext(file_name)[0]}.xlsx'
                    output_file_path = os.path.join(output_folder, output_file_name)

                    # Save the combined table as an Excel file
                    combined_table.to_excel(output_file_path, index=False)
                    print(f'Table extracted and saved: {output_file_path}')
                else:
                    print(f'No table found in page {pages} of the PDF file.')

            # Update the loading screen
            loading_label.config(text=f'Carregando Dados... {file_name}')
            loading_screen.update_idletasks()

    print("All PDF files processed!")

    # Close the loading screen after processing
    loading_screen.destroy()

root = tk.Tk()
root.title("PDF to Excel Tool")

# Input folder selection
input_folder_label = tk.Label(root, text="Input Folder:")
input_folder_label.pack()

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.pack()

input_folder_button = tk.Button(root, text="Select Input Folder", command=select_input_folder)
input_folder_button.pack()

# Output folder selection
output_folder_label = tk.Label(root, text="Output Folder:")
output_folder_label.pack()

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.pack()

output_folder_button = tk.Button(root, text="Select Output Folder", command=select_output_folder)
output_folder_button.pack()

# Process files button
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack()

# Define the coordinates for table extraction
coordinates = [
    {"pages": "all", "area": "52.001,32.006,214.138,560.812"},
    {"pages": "all", "area": "141.002,32.006,320.99,562.3"},
    {"pages": "all", "area": "450.006,32.006,746.018,560.812"},
    {"pages": "all", "area": "52.003,32.006,214.141,560.812"},
    {"pages": "all", "area": "225.728,34.213,279.278,561.531"},
    {"pages": "all", "area": "450.006,32.006,746.018,560.812"}
]

root.mainloop()
