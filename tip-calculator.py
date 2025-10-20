print("Welcome to the tip Calculator")                                # Greet the user
bill = float(input("What was the total bill? R"))                     # Get the total bill amount from the user
tip = int(input("How much would yopu like to tip? 10%, 15%, 20% ? ")) # Get the tip percentage from the user
people = input("How many people to split the bill ?")                 # Get the number of people to split the bill
tip_as_percent = tip/100                                              # Convert tip percentage to a decimal
total_tip_amount = bill * tip_as_percent                              # Calculate the total tip amount
total_bill = bill + total_tip_amount                                  # Calculate the total bill including tip
bill_per_person = total_bill / int(people)                            # Calculate the amount each person should pay
final_amount = round(bill_per_person, 2)                              # Round the amount to 2 decimal places
print(f"Each person should pay: R{final_amount}")                     # Print the final amount each person should pay