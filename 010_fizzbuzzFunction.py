def fizzbuzz(num):
    res = ""
    if num % 3 == 0 and num % 5 == 0:
        res = "FizzBuzz"
    elif num % 3 == 0:
        res = "Fizz"
    elif num % 5 == 0:
        res = "Buzz"
    else:
        res = num
    return res
for i in range(1,101):
    print(fizzbuzz(i))
    
        




    
