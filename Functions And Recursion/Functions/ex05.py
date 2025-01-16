usd = int(input("Enter Dollar's to convert INR: "))

def converter(usd_value):
    inr_value = usd_value*86.60
    print(usd_value, "USD =", inr_value, "INR")

converter(usd)
