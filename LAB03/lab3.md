def function1(value, number):
	if (number == 0): # 1
		return 1      # 1
	elif (number == 1): # 1
		return value # 1
	else:
		return value * function1(value, number-1) # 1n

#T(n) = 1 + 1 + 1 + 1 + 1 + 1n
#= 5 + 1n
#T(n) = O(n)

def recursive_function2(mystring,a, b):
	if(a >= b ):  # 1
		return True # 1
	else:
		if(mystring[a] != mystring[b]): # 1
			return False # 1
		else:
			return recursive_function2(mystring,a+1,b-1) # 4(n/2) 1 for call 1 for return 1 for + 1 for - /2 because reducing size of array a to b by 2 each loop
 
def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1) # 4 does return and call count as 2 operators or just 1 I keep getting different answers when searching?

#T(n) = 1 + 1 + 1 + 1 + 4(n/2) + 3
#= 7 + 2n
#T(n) = O(n)


Reflection 1. Identifiy base case, indentify recursive case, make sure it doesn't infinite loop with base case

2. Counting operators is the same but I'm unsure of return calling the function. Check how recursive functions reduce problem size such as question 2 reducing characters in string by 2 per recursion resulting in half the checks
