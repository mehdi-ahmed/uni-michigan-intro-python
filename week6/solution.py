def compute_pay(h, r):
    if h > 40:
        gross_pay = (40 * r) + ((h - 40) * r * 1.5)
    else:
        gross_pay = h * r
    return gross_pay


try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except ValueError:
    print('Entry error. Please inset Numbers ')

p = compute_pay(hrs, rate)
print("Pay", p)
