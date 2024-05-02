# For this task, you'll need to write a method that reverses a string. 
# Your method will receive one argument, a string, and be expected to output that string with its letters in reverse order.

# Ex. input = "hello"
# Ex. output = "olleh"

# Initial Solution – O(n^2)
# NOTE: Due to the complexity of concatenation, this isn't very efficient 
def reverse_string(string):
    reversedstringarr = []
    for char in string:
        reversedstringarr.insert(0, char)
    reversedstring = ""
    for i in reversedstringarr:
        reversedstring = reversedstring + i
    print(reversedstring)

reverse_string("hello")

# Better solution - use slicing - O(n)

def reverse_string_gooder(string):
    reversed_string = string[::-1]  # Use slicing to reverse the string directly
    print(reversed_string)

reverse_string_gooder("hello")