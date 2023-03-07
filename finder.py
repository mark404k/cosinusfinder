x = int(input("enter amount of degrees:   "))
y = 0.017452406

z = float(x) * float(y)

if x >= 0:
    print("Sin of", x, "° is", z)

if x <= 0:
    print("sinus of number can not equals 0 or be negative")

input()
