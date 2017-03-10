
def reverse(input_string):
    if len(input_string) == 1:
        print(input_string[len(input_string) - 1])
        return input_string
    else:
        print (input_string[len(input_string) - 1])
        return input_string[len(input_string) - 1] + reverse(input_string[:len(input_string) - 1])

print ("Please enter the string you want to reverse: ")
initial_input = raw_input()

reverse(initial_input)
