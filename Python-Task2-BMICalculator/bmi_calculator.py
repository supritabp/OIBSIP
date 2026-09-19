def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than zero. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def main():
    print("=" * 45)
    print("        BODY MASS INDEX (BMI) CALCULATOR     ")
    print("=" * 45)
    
    while True:
        weight = get_positive_float("\nEnter your weight in kilograms (kg): ")
        height = get_positive_float("Enter your height in meters (m): ")
        
        bmi = weight / (height ** 2)
        category = get_bmi_category(bmi)
        
        print("\n" + "-" * 35)
        print(f"Calculated BMI : {bmi:.2f}")
        print(f"Category       : {category}")
        print("-" * 35)
        
        choice = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("\nThank you for using the BMI Calculator! Stay healthy.")
            break

if __name__ == "__main__":
    main()
