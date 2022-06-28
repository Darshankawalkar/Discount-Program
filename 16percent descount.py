#program to calculate the dicsosunt
#the discount of 16% offered to the customer on the purchases of >=Rs.10,000

discount,discount_amount=0.0,0.0  #0.0 because here divion Going to happen
purchases=float(input("Enter The value of purchases:Rs"))  #this is suite
if purchases>=10000:  #if header   from this line below called as if clause
    discount=16
    discount_amount=purchases*discount/100
    print(discount_amount)
total_bill=purchases-discout_amount
print('Total Bill Rs:%.2f'%(total_bill))


