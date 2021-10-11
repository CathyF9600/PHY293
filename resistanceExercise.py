y = [6.498,
6.499,
6.500,
6.501
]
x = [0.064510,
0.029268,
0.013944,
0.002414
]
N=4
def sum(x):
    s = 0
    for el in x:
        s += el
    return s
def sq(n):
    return n**2

sum_of_sq_for_x = sum( [sq(x[0]), sq(x[1]), sq(x[2]), sq(x[3])] )
delta=N*sum_of_sq_for_x - sq(sum(x)) # N*sum of sq - sq of sum
print("delta:",delta)

m=( N*sum([ x[0]*y[0], x[1]*y[1], x[2]*y[2], x[3]*y[3]]) - sum(x)*sum(y))/delta
print("m:",m)

b=(sum(y)-m*sum(x))/N
print("b:",b)

variance = ( sq(y[0]-(b+m*x[0])) + sq(y[1]-(b+m*x[1])) + sq(y[2]-(b+m*x[2])) + sq(y[3]-(b+m*x[3])) ) / (N-2)
print("variance:",variance)


sm=(N*( sq(variance) / delta ))**0.5
print("sm:", sm)
sb=( variance * sum_of_sq_for_x / delta )**0.5
print("sb:", sb)
