# User's input
print("Welcome to your several RM calculator!")
weight = float(input("Enter the weight you use: "))
reps_current = int(input("Enter the number of reps you do with this weight: "))
rpe_current = int(input("Enter the RPE of the set (from 1 to 10): "))
reps_needed = int(input("Enter the number of reps you want to do: "))
rpe_needed = int(input("Enter the targeted RPE (from 1 to 10): "))

# Checking if input values are valid
if reps_current > 0 and reps_needed > 0:
    if 1 <= rpe_current <= 10 and 1 <= rpe_needed <= 10:

        reps_current_total = reps_current + 10 - rpe_current
        reps_needed_total = reps_needed + 10 - rpe_needed
        
        # Calculating weight_needed with an Epley formula 
        if reps_needed == 1 and rpe_needed == 10:
            weight_needed = round((weight * (1 + reps_current_total / 30)), 2)
        else:
            weight_needed = round(((weight * (1 + reps_current_total / 30)) / (1 + reps_needed_total / 30)), 2)

        # Round to the smallest available plate (0.25 kg)
        weight_needed_aprox = round(weight_needed / 0.5) * 0.5

        # Added approximation with round() in case error with the decimal part occurs
        aprox_text =  f"or approximately {weight_needed_aprox}" if round((weight_needed % 0.5), 5) != 0 else ""
        print(f"To make {reps_needed} reps with RPE {rpe_needed} you need to take {weight_needed} {aprox_text}")
    else:
        print("Please, enter the correct RPE")
else:
    print("Please, enter the correct amount of reps")
