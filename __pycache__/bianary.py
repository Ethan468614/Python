# Prompt the user for input
decimal_num = float(input("Enter a non-negative decimal number: "))
remainders = []

# Handle the specific case for input 0
if decimal_num == 0:
    print("The binary equivalent is 0")
else:
    temp_num = decimal_num
    
    # Use a while loop to get remainders
    while temp_num > 0:
        digit = temp_num % 2
        remainders.append(digit) # Add remainder to the end of the list
        temp_num //= 2 # Integer division
        
    # The remainders need to be read in reverse order
    remainders.reverse()
    
    print(f"The binary equivalent of {decimal_num} is: ", end="")
    
    # Print the elements of the list without spaces
    for bit in remainders:
        print(bit, end="")
    print() # Add a final newline for clean output
