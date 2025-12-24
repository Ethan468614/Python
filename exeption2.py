try:
    num1,num2 = eval(input ("Enter two numbers separated by a comma: "))

    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except SyntaxError:
    print("coma is missing between the two numbers")

except:
    print("wroung input")    