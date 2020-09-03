# Design an algorithm that takes in an integer
# that represents the lenght (defined as: n) of a string. 
# The string should print out n times numbers in a sequence.
# The following sequence starts:; 1, 2, 3, 6, 11, 20, 37,...

n = int(input("Enter the length of the sequence: ")) # Do not change this line
n_1 = 1
n_2 = 0
n_3 = 0
total_n = 0

while n > 0: # Here the input works as a counter 
  n_3 = n_2
  n_2 = n_1
  n_1 = total_n
  total_n = total_n + n_2 + n_3
  print(total_n)
  n = n - 1 # Ccounting down - defing the counter