
amount=int(input("enter amount"))
if amount > 1000:
    discount=20
    disc=amount*(discount/100)


elif amount > 500:
    discount=10
    disc=amount*(discount/100)


else:
    disc=0
    print("No Discount")

final_amount=amount-disc
print(f"discount is {disc}")
print(f"final amount is {final_amount}")