# User inputs his stats, ammount of reps he wants to do, current rpe, and rpe he needs with function input()
print("Welcove to your several RM calculator!")
weight = float(input("Enter the weight you do the exercise with: "))
reps_current = int(input("Enter the number of reps you do with this weight: "))
rpe_current = int(input("Enter the rpe of the set: "))
reps_needed = int(input("Enter the number of reps you want to do: "))
rpe_needed = int(input("Enter the needed rpe of the set (from 1 to 10): "))

# Checking weather the ammount of reps is correct or not
if reps_current > 0 and reps_needed > 0:

    # Checking weather rpe is correct or not
    if 1 <= rpe_current <= 10:

        # Calculating new variables for further clearer calculations
        reps_current_total = reps_current + 10 - rpe_current
        reps_needed_total = reps_needed + 10 - rpe_needed

        # Calculating weight_needed with an Eiply formula with the respect to current and needed rpe (look at the variables above); 
        # Using if else for different input (n=1 or n>1)
        if reps_needed == 1 and rpe_needed == 10:
            weight_needed = round((weight * (1 + reps_current_total / 30)), 2)
        else:
            weight_needed = round(((weight * (1 + reps_current_total / 30)) / (1 + reps_needed_total / 30)), 2)

        # Aproximating for available plates using round() function and arithmetics
        weight_needed_aprox = round(weight_needed / 0.125) * 0.125

        # Making approx_text with if-else inside, so it will write different things for different conditions;
        # Added round() in the condition checking to prevent computation misstakes (aka 83.75 = 83.7499999...)
        # Printing the result using the f-string and adding {approx_text} inside it
        aprox_text =  f"or aproximately {weight_needed_aprox}" if round((weight_needed % 0.125), 5) != 0 else ""
        print(f"To make {reps_needed} reps with rpe {rpe_needed} you need to take {weight_needed} {aprox_text}")
    else:
        print("Please, enter the correct rpe")
else:
    print("Please, enter the correct ammount of reps")