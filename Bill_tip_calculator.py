Total_bill = int(input("Total amout of bill="))
Tip = int(input("How much percent should be the tip="))
Tip = (Tip * Total_bill) / 100
Member = int(input("How many the member:"))
Final_bill = (Tip + Total_bill)
Pay = Final_bill / Member
print(f"So it's {Pay} per head..")