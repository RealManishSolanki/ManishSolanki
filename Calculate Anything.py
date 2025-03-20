#Created By Manish Solanki

while True:
	try:
		print("1. Addition (+)\n2. Subtraction (-)\n3. Dividtion (÷)\n4. Multiplication (×)\n5. Get Avarage\n6. Multiplication Table\n7. Exit")
		ask = int(input("\nEnter: "))
		#Addition Calculator
		if ask == 1:
			num1 = eval(input("\nEnter Number One: "))
			num2 = eval(input("Enter Number Two: "))
			print(f"Answer: {num1+num2}\n")
		
		#Subtraction Calculator
		elif ask == 2:
			num1 = eval(input("\nEnter Number One: "))
			num2 = eval(input("Enter Number Two: "))
			print(f"Answer: {num1-num2}\n")
			
		#Dividtion Calculator
		elif ask == 3:
			num1 = eval(input("\nEnter Number One: "))
			num2 = eval(input("Enter Number Two: "))
			print(f"Answer: {num1/num2}\n")
			
		#Multiplication Calculator
		elif ask == 4:
			num1 = eval(input("\nEnter Number One: "))
			num2 = eval(input("Enter Number Two: "))
			print(f"Answer: {num1*num2}\n")
			
		#Avarage Calculator	
		elif ask == 5:
			print("\nEnter Values Using Spaces!")
			num = input("Enter Values: ").split()
			n = [eval(num1) for num1 in num]
			num_sum = sum(n)
			num_len = len(n)
			print(f"Answer: {num_sum/num_len}\n")
		
		#Multiplication Table Calculator
		elif ask == 6:
			num = eval(input("Enter Number: "))
			print("Answer:")
			for n in range(1,11):
				print(f"{num} × {n} = {num*n}")
			print()
		
		#Exit
		elif ask == 7:
			ask = input("Are You Sure? [Y/N] : ")
			if ask == "Y":
				print("\nThank you for Using Me!")
				break
			elif ask == "N":
				print("\nLet's Continue...\n")
				continue 
			else:
				print("Error, Invalid Value\n")
		
		else:
			print("\nInvalid Value! Error...\n")

	except ValueError:
		print("\nError Enter Value!\n")
	except NameError:
		print("\nError Not A Number! \n")
