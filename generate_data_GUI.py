import customtkinter as ctk
import tkinter as tk
from generate_entry_data import *

def generate_input_main_window():
    # Create the main window
    main_window = tk.Tk()
    main_window.title("Input Data")
    main_window.resizable(0, 0)
    main_window.geometry('600x650')

    # Add a main label
    label = ctk.CTkLabel(master=main_window, text="Input Data for CSV", width=60, text_color="black", font=('Sans', 18, 'bold'))
    label.place(relx=0.326, rely=0.05)

    # Add labels for the input fields
    lbl_no_of_tests = ctk.CTkLabel(main_window, text="No. of tests:", text_color="black", font=('Sans', 14))
    lbl_no_of_tests.place(relx=0.2, rely=0.2)

    lbl_no_of_lobsters = ctk.CTkLabel(main_window, text="No. of lobsters:", text_color="black", font=('Sans', 14))
    lbl_no_of_lobsters.place(relx=0.2, rely=0.3)

    lbl_maximum_range_value = ctk.CTkLabel(main_window, text="Maximum value for CSV:", text_color="black", font=('Sans', 14))
    lbl_maximum_range_value.place(relx=0.2, rely=0.4)

    lbl_fishnet_capacity = ctk.CTkLabel(main_window, text="Fishing net capacity:", text_color="black", font=('Sans', 14))
    lbl_fishnet_capacity.place(relx=0.2, rely=0.5)

    lbl_filename = ctk.CTkLabel(main_window, text="CSV filename:", text_color="black", font=('Sans', 14))
    lbl_filename.place(relx=0.2, rely=0.6)

    # Add entry fields for the input data
    entry_no_of_tests = ctk.CTkEntry(main_window, fg_color="lightgray", text_color="black")
    entry_no_of_tests.place(relx=0.4, rely=0.2)

    entry_no_of_lobsters = ctk.CTkEntry(main_window, fg_color="lightgray", text_color="black")
    entry_no_of_lobsters.place(relx=0.44, rely=0.3)

    entry_maximum_range_value = ctk.CTkEntry(main_window, fg_color="lightgray", text_color="black")
    entry_maximum_range_value.place(relx=0.555, rely=0.4)

    entry_fishing_net_capacity = ctk.CTkEntry(main_window, fg_color="lightgray", text_color="black")
    entry_fishing_net_capacity.place(relx=0.52, rely=0.5)

    entry_filename = ctk.CTkEntry(main_window, fg_color="lightgray", text_color="black")
    entry_filename.place(relx=0.45, rely=0.6)

    # Define the command to generate the CSV file
    def command_generate():
        try:
            load_to_csv(
                str(entry_filename.get()),
                int(entry_no_of_tests.get()),
                int(entry_no_of_lobsters.get()),
                int(entry_maximum_range_value.get()),
                int(entry_fishing_net_capacity.get())
            )
            # Show success message and close window
            if tk.messagebox.showinfo("Success", "CSV file created successfully."):
                main_window.destroy()
        except Exception as e:
            # Show error message if something goes wrong
            tk.messagebox.showerror("Error", f"Something went wrong: {e}")

    # Add a button to generate the CSV file
    generate_btn = ctk.CTkButton(main_window, corner_radius=8, text="Generate", border_width=0, width=200, font=("Sans", 14), command=command_generate)
    generate_btn.place(relx=0.3, rely=0.80)

    # Run the main loop
    main_window.mainloop()

# just for testing it ...
#generate_input_main_window()
