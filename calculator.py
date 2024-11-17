num1 = int(input('enter num1 ->'))
num2 = int(input('enternum2 ->'))


 
 # Function to convert number into string
# Switcher is dictionary data type here
def calculate(argument):
    switcher = {
        '+': num1+num2,
        '-':num1-num2,
        '*':num1*num2,
        '/': 'divide by 0' if num2 == 0 else num1/num2
               
        
    }

  
    return switcher.get(argument, "wrong symbol")

# Driver program
if __name__ == "__main__":
    argument=input('enter the operation')

    print (calculate(argument))

