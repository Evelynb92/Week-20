def conversion(temperature_entry, degree_selection, result_label):
    if degree_selection == "Celsius":
        celsius = float((float(temperature_entry) * 9/5) + 32)
        #result_label.config(text='Fahrenheit')
        print('cel')
        return celsius
    elif degree_selection == "Fahrenheit":
        fahrenheit = float((float(temperature_entry) - 32) * 5 / 9)
        #result_label.config(text='Celsius')
        return fahrenheit
        print('fah')

