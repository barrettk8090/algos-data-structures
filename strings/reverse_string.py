# For this task, you'll need to write a method that reverses a string. 
# Your method will receive one argument, a string, and be expected to output that string with its letters in reverse order.

# Ex. input = "hello"
# Ex. output = "olleh"

def reverse_string(string):
    reversedstringarr = []
    for char in string:
        reversedstringarr.insert(0, char)
    reversedstring = ""
    for i in reversedstringarr:
        reversedstring = reversedstring + i
    print(reversedstringarr)
    print(reversedstring)

reverse_string("hello")