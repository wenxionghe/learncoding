def list_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
list_function(n)
print(n)