History_file="History.txt"

def show_history():
    file=open("History.txt","r")
    lines=file.readlines()#read every full line and stored them in a list
    if(len(lines)==0):
        print("The file is empty")
    else:
        for line in reversed(lines):
            print(line.strip())#(.strip) khasai imp the xaina yo program ma but it is used to remove the whitespaces 
    file.close()

def clear_history():
    file=open("History.txt","w")#history ma stored vako record ma blank page overwrite hunxa delete hunxa vanne hudaina
    file.close()
    print("History cleared")

def save_to_history(equation,result):
    file=open("History.txt","a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if(len(parts)!=3):
        print("Invalid input. Use format: number operator number eg: 8 + 9")
        return

    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if (op=="+"):
        result=num1 + num2
    elif(op=="-"):
        result=num1 - num2
    elif(op=="*"):
         result=num1 * num2
    elif(op=="**"):
        result=num1 ** num2
    elif(op=="/"):
        if(num2==0):
            print("Cannot divide by number 0")
            return
        else:
            result=num1 / num2
    else:
        print("Invalid operator. Use only +,-,*,/ only")

    if int(result)==result: #Converting float result into integer
        result=int(result)
    print("Result: ", result)
    save_to_history(user_input,result)


def main():
    print("---Simple Calculator---")
    while True:
        user_input=input("Enter calculation(+ - * /) or command(history,clear,exit): ")
        if user_input=="exit":
            print("Thank you! Tata")
            break
        elif user_input=="history":
            show_history()
        elif user_input=="clear":
            clear_history()
        else:
            calculate(user_input)
main()

'''Important concepts to understand
- split() separates the input into parts, such as "8 + 9" into ["8", "+", "9"].
- strip() removes the newline character and whitespace from each history line.
- reversed() displays the newest history entry first.
- "a" appends new calculations to the history file.
- "w" clears the file's contents.
- break terminates the infinite loop when the user enters exit.
Note: Enter calculations with spaces, such as 8 + 9, because your program uses split() to separate the numbers and operator.'''







