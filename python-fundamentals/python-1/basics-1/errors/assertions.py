def kelvinToFahrenheit(Temperature):
    assert(Temperature >= 0), "Colder than absolute zero"
    return ((Temperature-273)*1.8) + 32
print(kelvinToFahrenheit(273))
print(int(kelvinToFahrenheit(505.78)))
print(kelvinToFahrenheit(-5))