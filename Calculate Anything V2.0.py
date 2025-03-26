#Created By Manish Solanki it is a Second Version Of Calculate Anything (V2.0).

while True:
	try:
		print("1. Addition (+)\n2. Subtraction (-)\n3. Dividtion (÷)\n4. Multiplication (×)\n5. Get Avarage\n6. Multiplication Table\n7. Exit")
		
		ask = int(input("\nEnter: "))
		
		#Addition Calculator
		if ask == 1:
			print("\nEnter Values Using Spaces! e.g. 50 40 68 52 45 etc.")
			num = input("Enter Values: ").split()
			n = [eval(num1) for num1 in num]
			print(f"Answer: {sum(n)}\n")
		
		#Subtraction Calculator
		elif ask == 2:
			print("\nEnter Values Using Spaces! e.g. 50 40 68 52 45 etc.")
			num = input("Enter Values: ").split()
			n = [eval(num1) for num1 in num]
			if len(n) > 0:
				result = n[0]
				for num in n[1:]:
					result -= num
			else:
				print("Error Please Enter Value!\n")  	
			
			print(f"Answer: {result}\n")
			
		#Dividtion Calculator
		elif ask == 3:
			print("\nEnter Values Using Spaces! e.g. 50 40 68 52 45 etc.")
			num = input("Enter Values: ").split()
			n = [eval(num1) for num1 in num]
			if len(n) > 0:
				result = n[0]
				for num in n[1:]:
					result /= num
			else:
				print("Error Please Enter Value!\n")  	
			
			print(f"Answer: {result}\n")
		
		#Multiplication Calculator
		elif ask == 4:
			print("\nEnter Values Using Spaces! e.g. 50 40 68 52 45 etc.")
			num = input("Enter Values: ").split()
			n = [eval(num1) for num1 in num]
			if len(n) > 0:
				result = n[0]
				for num in n[1:]:
					result *= num
			else:
				print("Error Please Enter Value!\n")  	
			
			print(f"Answer: {result}\n")
		
		#Avarage Calculator		
		elif ask == 5:
			print("\nEnter Values Using Spaces! e.g. 50 40 68 52 45 etc.")
			num = input("Enter Values: ").split()
			n = [eval(num1) for num1 in num]
			num_sum = sum(n)
			num_len = len(n)
			answer = num_sum/num_len
			print(f"Answer: {answer}\n")
		
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
	
	except ValueError:
		print("\nError Enter Value!\n")
	except NameError:
		print("\nError Not A Number! \n")