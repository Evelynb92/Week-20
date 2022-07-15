import tkinter as tk
from functions import conversion

def gui():

    #Window Box -----------------------
    window = tk.Tk()
    window.title('Temperature Conversion')

    window.geometry('400x200')

    #Text BG -----------------------
    window_bg = '#FFC18E'
    button_bg = '#FFC18E'

    window.config(bg='#CA4E79')

    #Widget -----------------------
    degree = tk.StringVar()

    def call_conversion():
        temp = temperature_entry.get()

        if temp.isnumeric():

            deg = degree.get()
            result_entry.delete(0,tk.END)
            result_entry.insert(0,conversion(temp, deg))

            if deg == "Celsius":
                    result_label.config(text='<--- Fahrenheit')

            elif deg == "Fahrenheit":
                    result_label.config(text='<--- Celsius')

        else:
            result_entry.insert(tk.END,"Invaild Characters")




    #Buttons -----------------------
    convert_button = tk.Button(text="Convert", bg=button_bg)
    convert_button.grid(row=20, column=2)
    convert_button.configure(command=call_conversion)

    def clear_button():
        temperature_entry.delete(0,tk.END)
        result_entry.delete(0, tk.END)
        return None

    clear_button = tk.Button(text="Clear", bg=button_bg, command=clear_button)
    clear_button.grid(row=100, column=2)

    #Dropdown Box -----------------------
    options = ["Celsius", "Fahrenheit"]

    drop_down = tk.OptionMenu(window, degree, *options)
    drop_down.config(bg=window_bg)
    drop_down["menu"].config(bg=window_bg)
    drop_down.grid(row=0, column=3)

    #Text Label -----------------------
    temperature_label = tk.Label(text="Enter Temperature", bg=window_bg)
    temperature_label.grid(row=0, column=0)

    output_label = tk.Label(text="Results", bg=window_bg)
    output_label.grid(row=1, column=0)

    result_label = tk.Label(text="",bg=window_bg)
    result_label.grid(row=1, column=3)

    #User entry -----------------------
    temperature_entry = tk.Entry()
    temperature_entry.grid(row=0, column=2)

    result_entry = tk.Entry(text="")
    result_entry.grid(row=1, column=2)

    window.mainloop()