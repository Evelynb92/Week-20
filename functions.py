def conversion(temperature_entry, degree_selection):
    if degree_selection == "Celsius":
        celsius = float((float(temperature_entry) * 9/5) + 32)
        round(celsius,2)
        #print('cel')
        return celsius
    elif degree_selection == "Fahrenheit":
        fahrenheit = float((float(temperature_entry) - 32) * 5 / 9)
        round(fahrenheit, 2)
        return fahrenheit
        #print('fah')

