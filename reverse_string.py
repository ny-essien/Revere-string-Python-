#write a function to reverse a string
#using stack data structure

def reverse_string(string : str) -> str:

    stack = []
    reverse_stack  = []
    rev_string = ""

    #appending each element of the string to the stack
    for i in string:
        stack.append(i)

    #appending the stack in a reverse order to the reverse_stack
    for x in range(len(stack)):
        reverse_stack.append(stack[-1])
        stack.pop()

    rev_string = "".join(reverse_stack)
    return rev_string

#reversing using deque

def reverse_string2(string : str) -> str:

    reverse_string =  ""
    from collections import deque

    stack = deque()

    for i in string:
        stack.appendleft(i)

    reverse_string = "".join(stack)

    for i in range(len(stack)):
        stack.popleft()

    return reverse_string

if __name__=="__main__":
    print(reverse_string("Welcome to turing"))
    print(reverse_string2('Welcome to turing'))
    

    