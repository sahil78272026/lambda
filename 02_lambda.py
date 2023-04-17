
#not anonymous
square = lambda a: [i for i in range(a) if i%2==0]
print(square(100))

#output
#[0,2,4.... 98]

#anonymous
print((lambda a:[i for i in range(a) if i%2==0])(100))

#output
#[0,2,4.... 98]


# lambda function is used when we want to use function to return a value
func = lambda a:a+5
multiply = lambda a,b : a*b

print(func(10))
print(multiply(10,4))





