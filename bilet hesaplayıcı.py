choice=input("for cinema(1),for theatre(2) key in :")
student=input("are you student(Y/N):")
fee=0

if choice=="1":
	fee=15
elif choice=="2":
	fee=20

if student=="Y" or student=="y":
	fee=fee/2

print(f"the amount you have to pay:{fee}")
