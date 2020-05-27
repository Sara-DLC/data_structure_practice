# # my_math_func takes in a number = x and a function = f as parameters
# from random import randint


# def my_math_func(x, f):
#     return f(x)

# # lambda expressions help with being able to pass different options instead of writing multiple functions.


# # def x_cube(x):
# #     return x**3
# # print(my_math_func(3, x_cube))

# # does the same thing as the x_cube function, lambda expressions can be saved to a variable
# lambda x: x**3
# # pass the lambda expression as the second parameter
# # print(my_math_func(3, lambda x: x**3))


# my_letters = ["a", "b", "c", "d", "e"]
# print(list(map(str.capitalize, my_letters)))

# # with lambda expression
# print(list(map(lambda x: x.capitalize(), my_letters)))


# # printing random integers using list comprehension
# my_ints = [randint(1, 1000) for num in range(100)]
# print(my_ints)

# # with lambda expression, each number first then their cubed values
# print(list(map(lambda x: x+x**3, my_ints)))

my_lambda_func = (lambda x: x)
print(type(my_lambda_func))
