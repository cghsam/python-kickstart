print("### Welcome to MyMusclePal! ###")
weight = input("What is your weight in kilograms (kg)? Type the number and press Enter: ")
protein = int(weight) * 2
calories = int(weight) * 30.8
print("Based on your weight of", str(weight) + "kg, you need", str(protein) + "kg of protein and", str(calories) + " calories per day.")