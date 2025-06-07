def function1(number):
	total = 0 # 1 
 
	for i in range(number): # n for loop + 1 for range
		x = i + 1 # 2n for 2 operators and loop
		total += x * x # 3n for 3 operators and loop
 
	return total # 1

#T(n) = 1 + n + 1 + 2n + 3n + 1
#= 6n + 2
#T(n) = O(n)

def function2(number):
	return (number * (number + 1) * (2 * number + 1)) // 6 #6 operators

#T(n) = 1 + 1 + 1 + 1 + 1 + 1
#= 6
#T(n) = O(1)

def function3(list):
	n = len(list) #1 
	for i in range(n - 1): # n-1 for loop and + 1 for range
		for j in range(n - 1 - i): n(n-1)/2
			if list[j] > list[j+1]: # 1
				tmp = list[j] # 1 
				list[j] = list[j+1] # 1
				list[j + 1] = tmp # 1

#T(n) = 1 + (n-1) + 1 + n(n-1)/2 * (1 + 1 + 1 + 1)
#= 1 + n + n(n-1)/2 * 4
#= 1 + n + 2n(n-1)
#= 1 + n + 2n^2 - 2n
#= 1 - n + 2n^2
#T(n) = O(n^2)


def function4(number):
	total = 1 #1 
	for i in range(1, number): #n-1 for loop + 1 for range
		total *= i + 1 #3(n-1) for 3 operators in loop
	return total #1

#T(n) = 1 + (n-1) + 1 + 3(n-1) + 1
#= 4(n-1) + 3
#= 4n + 3 - 4
#= 4n - 1
#T(n) = O(n)


Reflection: I didn't get to complete lab 1 as it closed so I could no longer view the instructions so I will talk about this lab as I struggled a lot with question 3 and would like clarification on how the nested loops work with time complexity if you could provide feedback.