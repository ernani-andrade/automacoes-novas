import tkinter as tk
from tkinter import filedialog

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

    # Call your file processing function here
    # Replace this with your own logic to process the files

    print("Input Folder:", input_folder)
    print("Output Folder:", output_folder)

root = tk.Tk()
root.title("Automação de Notas")

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

root.mainloop()
