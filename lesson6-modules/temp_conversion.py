def c2f(value):
    return (value * 9/5) + 32

def f2c(value):
    return (value - 32) * 5/9

def c2k(value):
    return value + 273.15

def f2k(value):
    ctemp = f2c(value)
    return ctemp+273.15