import customtkinter as ctk
import tkinter as tk
import subprocess
from algorithm import algorithm_py
from obtain_data_for_c_file import read_data_for_c
import matplotlib.pyplot as plt
from tkinter import filedialog


def results_py_function():
   
   #Running the algorithm for computing data, write it to file, and show the chart
   algorithm_py()

   def read_file(file_path):
     """Read the content of a text file and return it as a string."""
     with open(file_path, 'r') as file:
        content = file.read()
     return content

   def load_file():
     """Load the content of 'output_py.txt' and display it in the Text widget."""
     file_path = 'output_py.txt'
     content = read_file(file_path)
     text_widget.delete(1.0, tk.END)  # Clear any existing content
     text_widget.insert(tk.END, content)  # Insert new content
   
   def download_file():
     """Download the file when the button is clicked."""
     file_path = 'output_py.txt'
     save_path = filedialog.asksaveasfilename(defaultextension=".txt")
     if save_path:  # Ensure the user selected a file to save
        with open(file_path, 'r') as file:
            content = file.read()
        with open(save_path, 'w') as file:
            file.write(content)

   # Set up the main application window
   root = tk.Tk()
   root.title("Output File Viewer")
   root.geometry("800x600")

   # Create a Text widget to display the file contents
   text_widget = tk.Text(root, wrap='word')
   text_widget.pack(expand=1, fill='both')

   # Create a menu to open the output_py.txt file
   menu = tk.Menu(root)
   root.config(menu=menu)
   file_menu = tk.Menu(menu, tearoff=0)
   menu.add_cascade(label="Open Output File", menu=file_menu)
   file_menu.add_command(label="Open 'output_py.txt'", command=load_file)

   download_button = tk.Button(root, text="Download 'output_py.txt'", command=download_file)
   download_button.pack()


   # Run the application
   root.mainloop()


def results_c_function():
   
   #First read data for the C file
   read_data_for_c()

   #Run the C file, write contents to output_c.txt
   # Compile the C program
   subprocess.run(['gcc' , 'algorithm.c' , '-o' , 'algorithm.exe'])
   subprocess.run("./algorithm.exe")

   #Show the charts
   # Function to read CPU times from output_c.txt file
   def read_cpu_times(filename):
    cpu_times = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "CPU time" in line:
                time_str = line.split(":")[-1].strip().split()[0]  # Extract the time value
                cpu_times.append(float(time_str))
    return cpu_times

   # Read CPU times from the file
   cpu_times = read_cpu_times("output_c.txt")

   # Plot the time complexity chart
   plt.figure(figsize=(10, 6))
   plt.plot(range(1, len(cpu_times) + 1), cpu_times, marker='o', linestyle='-', color='b')
   plt.xlabel('Test Case Number')
   plt.ylabel('Time (seconds)')
   plt.title('Time Complexity (C version)')
   plt.grid(True)

   # Annotate the times on the chart
   for i, time_value in enumerate(cpu_times):
    plt.text(i + 1, time_value, f'{time_value:.4f}', fontsize=9, ha='right')

   plt.show()

   def read_file(file_path):
     """Read the content of a text file and return it as a string."""
     with open(file_path, 'r') as file:
        content = file.read()
     return content

   def load_file():
     """Load the content of 'output_c.txt' and display it in the Text widget."""
     file_path = 'output_c.txt'
     content = read_file(file_path)
     text_widget.delete(1.0, tk.END)  # Clear any existing content
     text_widget.insert(tk.END, content)  # Insert new content
   
   def download_file():
     """Download the file when the button is clicked."""
     file_path = 'output_py.txt'
     save_path = filedialog.asksaveasfilename(defaultextension=".txt")
     if save_path:  # Ensure the user selected a file to save
        with open(file_path, 'r') as file:
            content = file.read()
        with open(save_path, 'w') as file:
            file.write(content)

   # Set up the main application window
   root = tk.Tk()
   root.title("Output File Viewer")
   root.geometry("800x600")

   # Create a Text widget to display the file contents
   text_widget = tk.Text(root, wrap='word')
   text_widget.pack(expand=1, fill='both')

   # Create a menu to open the output_py.txt file
   menu = tk.Menu(root)
   root.config(menu=menu)
   file_menu = tk.Menu(menu, tearoff=0)
   menu.add_cascade(label="Open Output File", menu=file_menu)
   file_menu.add_command(label="Open 'output_c.txt'", command=load_file)

   download_button = tk.Button(root, text="Download 'output_c.txt'", command=download_file)
   download_button.pack()

   # Run the application
   root.mainloop()


# this is the actual main window, with attributes of it, some buttons and their commands.
def results_window():
 
 main_window = tk.Tk()

 main_window.title("RESULTS")

 main_window.geometry("450x470")

 main_window.resizable(0, 0)

 label = ctk.CTkLabel(master=main_window , text="RESULTS WINDOW" , width=60 , text_color="black" , font=('Sans' , 14 , 'bold'))
 label.place(relx=0.3 , rely=0.05)

 python_results_btn = ctk.CTkButton(main_window , corner_radius=8 , text="Python Results" , border_width=0 , width = 200 , font=("Sans" , 14) , command=results_py_function)
 python_results_btn.place(relx=0.225 , rely=0.40)

 c_results_btn = ctk.CTkButton(main_window , corner_radius=8 , text="C Results" , border_width=0 , width = 200 , font=("Sans" , 14) , command=results_c_function)
 c_results_btn.place(relx=0.225 , rely=0.60)


 main_window.mainloop()