# Design an algorithm that takes in an integer
# that represents the lenght (defined as: n) of a string. 
# The string should print out n times numbers in a sequence.
# The following sequence starts:; 1, 2, 3, 6, 11, 20, 37,...

n = int(input("Enter the length of the sequence: ")) # Do not change this line
total_n = 0

while n > 0: # Here the input works as a counter 
  print(total_n)
  n = n - 1 # Ccounting down - defing the counter