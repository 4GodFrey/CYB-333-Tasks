weight = input("what is your weight? ")
mes = input("kg or lbs: ")
kg = True
lbs = True

if kg:
    converted_weight = int(weight) * 2.205

if lbs:
    converted_weight = int(weight) / 2.205

print(f"your weight is {converted_weight}")
