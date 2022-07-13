from gui import gui

gui()

def clear_button(temperature_input):
    temperature_input.delete(0,gui.END)
    return None

# def conversion():
#    temperature = temperature_input.get()
#    if drop_down == "Celsius":
#      f = float((float(temperature) * 9/5) + 32)
#      result_input.config(text="%f Fahrenheit" % f)

def conversion(drop_down, temperature_entry, result_entry):
    if drop_down == "Celsius":
        celsius = float((float(temperature_entry) * 9/5) + 32)
        result_entry.config(text="%f Celsius" % celsius)
        print('cel')

    if drop_down == "Fahrenheit":
        fahrenheit = float((float(temperature_entry) - 32) * 5 / 9)
        result_entry.config(text="%f Fahrenheit" % fahrenheit)
        return
        print('fah')