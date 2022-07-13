import tkinter as tk


#Window Box -----------------------
window = tk.Tk()
window.title('Temperature Conversion')

window.geometry('500x300')

#Text BG -----------------------
window_bg = '#F5EDDC'
button_bg = '#CFD2CF'

#Widget -----------------------
var = tk.StringVar()

# #Functions -----------------------

# def clear_button():
#     temperature_input.delete(0,tk.END)
#     return None

# def conversion():
#    temperature = temperature_input.get()
#    if drop_down == "Celsius":
#      f = float((float(temperature) * 9/5) + 32)
#      result_input.config(text="%f Fahrenheit" % f)



#Buttons -----------------------
convert_button = tk.Button(text="Convert", bg=button_bg)
convert_button.grid(row=20, column=1)

clear_button = tk.Button(text="Clear", bg=button_bg)
clear_button.grid(row=50, column=1)


#Dropdown Box -----------------------

options = ["Celsius", "Fahrenheit"]

drop_down = tk.OptionMenu(window, var, *options)
drop_down.grid(row = 0, column = 2)


#Text Label -----------------------
temperature_label = tk.Label(text="Enter Temperature", bg=window_bg)
temperature_label.grid(row = 0, column = 0)


#User input -----------------------
temperature_input = tk.Entry()
temperature_input.grid(row=0, column=1)

result_input = tk.Entry()
result_input.grid(row=1, column=1)

window.mainloop()