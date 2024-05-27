import customtkinter as ctk
import tkinter as tk
import os
from generate_data_GUI import generate_input_main_window
from open_github_repo import open_repository
from help import help_func
from technical_report_opener import open_technical_report
from results_GUI import results_window

#this is optional...
def delete_csv_contents(filename):
    #this is for deleting csv files contents, basically it writes a new empty file with that filename(that is why we put pass keyword,
    #just for using )
    with open(filename, 'w') as file:
        pass

#this will deletes all unnecesarry files with os modules when we close the app, we call the function into on_closing() function
#This function will raise an error, because the os file is not building correctly the path, however in the end is cleaning everything
#If you encounter any errors, it is because some cases for error handling are not taken into consideration by me, but the application is working 
#I mean if you input data corectly and used the app as it says in the README.md file from github or from HELP section(README.md file), then everything will be ok.

def delete_csv_files():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    files_to_delete = ["data_for_c.csv", "algorithm.exe", "read_data_from_csv_c.exe", "output_c.txt", "output_py.txt"]
    for filename in os.listdir(script_dir):
        if filename.endswith((".csv", ".txt", ".exe")):
                os.remove(os.path.join(script_dir, filename))

    # Delete specific files outside the loop
    for file_to_delete in files_to_delete:
            os.remove(os.path.join(script_dir, file_to_delete))

def on_closing():
  if tk.messagebox.askyesno("Quit", "Are you sure you want to quit?\nNOTE : All your stored data will be deleted! (csv files , executables etc.)"):
    delete_csv_files()
    main_window.destroy()


# this is the actual main window, with attributes of it, some buttons and their commands.
main_window = tk.Tk()

main_window.title("HOMEWORK")

main_window.geometry("450x470")

main_window.resizable(0, 0)

label = ctk.CTkLabel(master=main_window , text="ALGORITHM DESIGN HOMEWORK" , width=60 , text_color="black" , font=('Sans' , 14 , 'bold'))
label.place(relx=0.155 , rely=0.05)

generate_data_btn = ctk.CTkButton(main_window , corner_radius=8 , text="Generate Data" , border_width=0 , width = 200 , font=("Sans" , 14) , command=generate_input_main_window)
generate_data_btn.place(relx=0.225 , rely=0.25)

show_results_btn = ctk.CTkButton(main_window , corner_radius=8 , text="Results" , border_width=0 , width = 200 , font=("Sans" , 14) , command=results_window)
show_results_btn.place(relx=0.225 , rely=0.40)

report_btn = ctk.CTkButton(main_window , corner_radius=8 , text="Technical Report" , border_width=0 , width = 200 , font=("Sans" , 14) , command=open_technical_report)
report_btn.place(relx=0.225 , rely=0.55)

github_btn = ctk.CTkButton(main_window , corner_radius=8 , text="Github Repository" , border_width=0 , width = 200 , font=("Sans" , 14) , command=open_repository)
github_btn.place(relx=0.225 , rely=0.70)

help_btn = ctk.CTkButton(main_window , corner_radius=8 , text="HELP" , border_width=0 , width = 200 , font=("Sans" , 14) , text_color="black" , fg_color="#f0f0f0" , hover_color="#f0f0f0" , command=help_func)
help_btn.place(relx=0.225 , rely=0.90)


#here when we want to close the main window it will pop up on_closing just to be safe and sure it will not be closed when we don't want that
main_window.protocol("WM_DELETE_WINDOW", on_closing)

main_window.mainloop()
