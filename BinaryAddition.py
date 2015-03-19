"""
	In this problem, we study the simple task of summing multiple integers
	which are represented in their binary form.

	The first line contains an integer N; 2 <= N <= 1,000,000; represented
	in binary. Each of the next N lines contain a single binary number which
	are to be added together. All binary numbers of the inputs are
	guaranteed to be exactly 32 binary characters in length, therefore can
	be stored in a 32-bit integer, and will be positive.
"""
# test value at 4, but in the competition it will be 32, as per the specs above
bit_length = 32

def bit_string_to_integer(bit_string):
        """
		Convert a string representing a binary number
		to an integer to represent the bitString
	"""
        result = 0;
        bit_string = bit_string[::-1]
        for i in range(0, bit_length):
        	result += (int(bit_string[i]) * (2**i))
        return result

def integer_to_bit_string(integer):
	"""
		Convert the passed integer to a string
		representing that integer in binary form
	"""
	result = ""
	for i in range(0, bit_length):
		result = str(integer % 2) + result
		integer >>= 1
	return result

############################### MAIN ###########################################
total_input = 0
number_of_inputs = bit_string_to_integer(input("Enter the number of lines\n"))
for i in range(0, number_of_inputs):
	total_input += bit_string_to_integer(input("Enter a binary string\n"))
print(integer_to_bit_string(total_input))