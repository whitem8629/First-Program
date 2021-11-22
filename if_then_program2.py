#ask user for meal cost
meal= float (input("Enter meal price:"))
#ask user for tip cost
tip= float (input("Enter Tip:"))
if tip ==0 :
    print("Generating 20% tip")
    tip_amount= meal*0.20
else:
    tip_amount= meal*tip
    
total=meal+tip_amount

print("Total cost for meal $", total)
