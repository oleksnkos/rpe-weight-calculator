# rpe-weight-calculator
CLI tool for calculating an amount of weight you need to take to do a certain number of reps with a certain RPE. Calculations are based on the Epley's formula and the reversed Epley formula.

Logic of calculations:
  - Epley's formula: RM = W*(1+R/30), where RM is a 1 rep maximum, W is the weight you used and R is the amount of reps you did with that weight. In my case, R = original amount of reps + 10 - RPE; RPE = from 1 to 10
  - Reversed Epley's formula: RT = RM/(1+R/30), where RT is a targeted ammount of reps, RM is a 1 rep maximum and R is a targeted amount of reps. In my case, R = targeted amount of reps + 10 - RPE; RPE = from 1 to 10
  - Formula used in the code: RT = (W*(1+R/30))/(1+R'/30), where RT is a targeted amount of reps, W is the weight you used, R is an amount of reps you did with original weight + 10 - RPE (RPE = from 1 to 10), and R' is a targeted amount of reps + 10 - RPE (RPE = from 1 to 10)
  An important detail is that formula for 1 rep with 10 RPE is differnt from the formula for other combinations and is actually just original Epley's formula with slighhtly changed R (as mentioned higher). It is done for the more precise result.

Other:
  - Variable approx_text in line 26 is made with a ternary operator
  - Aproximation with round() in line 26 was added to prevent some computation mistakes with decimal numbers (for example, 0.1 + 0.2 = 0.30000000000000004)

Input:
  - Weight you that you lift
  - Amount of reps you do with that weight
  - RPE you lift that weight for that amount of reps with
  - Amount of reps you want to do
  - RPE you want to that amount of reps with

Output:
  - Exact weight you can lift with that RPE and number of reps (rounded up to the second decimal)
  - Aproximated weight you can lift with that RPE and number of reps (rounded up with the respect to the lightest plate of 0.25 kg)

<pre>
Example:
<code>
Enter the weight you use: <b>105</b>
Enter the number of reps you do with this weight: <b>6</b>
Enter the RPE of the set (from 1 to 10): <b>7</b>
Enter the number of reps you want to do: <b>3</b>
Enter the targeted RPE (from 1 to 10): <b>9</b>

<b>To make 3 reps with RPE 9 you need to take 120.44 or approximately 120.5</b>
</code>
</pre>
