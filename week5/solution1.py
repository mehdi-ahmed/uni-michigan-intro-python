hrs = input("Enter Hours:")
rate = input("Enter Rate per hour:")
try:
    r = float(rate)
    h = float(hrs)
except:
    print("Error, please insert float Numbers!")
    quit()

gross_pay = 0
standard_hours = 40.0

if h > 40:
    gross_pay = (standard_hours * r) + ((h - standard_hours) * r * 1.5)
else:
    gross_pay = h * r

print(gross_pay)
