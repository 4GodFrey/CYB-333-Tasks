def calculate_calories(protein, carbohydrates, fat):
    # 1 gram of protein contains 4 calories
    # 1 gram of carbohydrates contains 4 calories
    # 1 gram of fat contains 9 calories
    return (protein * 4) + (carbohydrates * 4) + (fat * 9)

if __name__ == '__main__':
    protein = float(input("Enter the amount of protein (in grams): "))
    carbohydrates = float(input("Enter the amount of carbohydrates (in grams): "))
    fat = float(input("Enter the amount of fat (in grams): "))
    calories = calculate_calories(protein, carbohydrates, fat)
    print("The food contains {} calories.".format(calories))
