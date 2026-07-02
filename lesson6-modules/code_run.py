from math_utils import square,cube

a = 6

print(f"The square of {a} is {square(a)}")
print(f"The cube of {a} is {cube(a)}")


from temp_conversion import c2f,f2c,c2k,f2k

input_temp_celsius = 25
input_temp_fahrenheit = 77

print(f"{input_temp_celsius}°C is {c2f(input_temp_celsius)}°F")
print(f"{input_temp_fahrenheit}°F is {f2c(input_temp_fahrenheit)}°C")
print(f"{input_temp_celsius}°C is {c2k(input_temp_celsius)}K")
print(f"{input_temp_fahrenheit}°F is {f2k(input_temp_fahrenheit)}K")
