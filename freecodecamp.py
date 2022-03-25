"""width = 15
height = 12.0
print(height/3)

x = int(input('Enter X value: '))
if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print('large')
print('all done')"""


#try:
hrs = float(input('enter hrs spent:'))
rate = float(input('enter your rate:'))
Wkly_reg_pay = hrs * rate
hrs_40 = 40 * rate
OT_hrs = hrs - 40
OT_rate = OT_hrs * 1.5
OT_pay = OT_hrs * OT_rate
print("Hrs spent: ", hrs)
#print('Regular Pay = ', Wkly_reg_pay)

if hrs <= 40:
    print("weekly pay", Wkly_reg_pay)

elif hrs > 40:
     print("overtime hrs spent", OT_hrs)
     print("Weekly pay with overtime", hrs_40 + OT_pay)
else:
    print('you work less than or equal to 40 hrs.')
#except Exception:
#    print("please provide a valid number")
