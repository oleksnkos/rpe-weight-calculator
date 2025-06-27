# rpe-weight-calculator
CLI tool for calculating an ammount of weight you need to take to do a certain ammount of reps with a certain RPE. Calculations are based on Epley's formula and reversed Epley formula.

Logic of calculations:
  As mentioned in the description, Epley's formula and reversed Epley formula are being used together. 
  Epley's formula: W*(1+R/30), where W is the weight you used and R is the ammount of reps. In my case, R = original ammount of reps + 10 - RPE; RPE = from 1 to 10
  Reversed Epley's formula: W/(1+R/30), where W is a 1RM and R is a targeted ammount of reps. In my case, R = targeted ammount of reps + 10 - RPE; RPE = from 1 to 10

Input:
  - Weight you that you lift
  - Amount of reps you do with that weight
  - RPE you lift that weight for that amount of reps with
  - Amount of reps you want to do
  - RPE you want to that amount of reps with
Output:
  - Exact weight you can lift for that RPE and ammount of reps rounded up to the second decimal
  - Aproximated weight you can lift for that RPE and ammount of reps rounded up with the respect to the lightest plate of 0.25 kg (0.5 kg because 0.25 on both sides)
