def display():
    print("hello world")

def findSum(num1,num2):
    return num1+num2;

def finAverage(number):
    return number/2

def OutputFunction(firstNumber,secondNumber):
    sum = findSum(firstNumber,secondNumber)
    avg = finAverage(sum)
    return avg

solution = OutputFunction(4,5)
print(solution)
