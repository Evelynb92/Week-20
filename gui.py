import tkinter as tk
#from main import conversion


def gui():
    #Window Box -----------------------
    window = tk.Tk()
    window.title('Temperature Conversion')

    window.geometry('500x300')

    #Text BG -----------------------
    window_bg = '#F5EDDC'
    button_bg = '#CFD2CF'

    #Widget -----------------------
    #var = tk.StringVar()
    temperature = tk.StringVar()

    #Buttons -----------------------
    convert_button = tk.Button(text="Convert", bg=button_bg)
    convert_button.grid(row=20, column=1)
    # convert_button.configure(command=conversion())

    clear_button = tk.Button(text="Clear", bg=button_bg,)
    clear_button.grid(row=50, column=1)


    #Dropdown Box -----------------------

    options = ["Celsius", "Fahrenheit"]

    drop_down = tk.OptionMenu(window, temperature, *options)
    drop_down.grid(row=0, column=2)


    #Text Label -----------------------
    temperature_label = tk.Label(text="Enter Temperature", bg=window_bg)
    temperature_label.grid(row=0, column=0)


    #User entry -----------------------

    temperature_entry = tk.Entry()
    temperature_entry.grid(row=0, column=1)

    result_entry = tk.Entry()
    result_entry.grid(row=1, column=1)

    window.mainloop()