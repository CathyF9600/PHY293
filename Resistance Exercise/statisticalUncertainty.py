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

def find_delta(x,y):
    sum_of_sq_for_x = sum( [sq(x[0]), sq(x[1]), sq(x[2]), sq(x[3])] )
    delta=N*sum_of_sq_for_x - sq(sum(x))
    return delta

def find_m(x,y):
    m=( N*sum([ x[0]*y[0], x[1]*y[1], x[2]*y[2], x[3]*y[3]]) - sum(x)*sum(y))/delta
    return m

def find_b(x,y):
    b=(sum(y)-m*sum(x))/N
    return b

def find_variance(x,y):
    v = ( sq(y[0]-(b+m*x[0])) + sq(y[1]-(b+m*x[1])) + sq(y[2]-(b+m*x[2])) + sq(y[3]-(b+m*x[3])) ) / (N-2)
    return v

def find_sm(x,y):
    sm=(N*( sq(variance) / delta ))**0.5
    return sm

def find_sb(x,y):
    sb=( variance * sum_of_sq_for_x / delta )**0.5
    return sb

print("op1")
delta=find_delta(x,y) # N*sum of sq - sq of sum
print("delta:",delta)

m=find_m(x,y)
print("m:",m)

b=find_b(x,y)
print("b:",b)

variance=find_variance(x,y)
print("variance:",v)

sm=find_sm(x,y)
print("sm:", sm)

sb=find_sb(x,y)
print("sb:", sb)

x=[0.013946,
0.002414,
0.00024,
0.000062
]

y=[6.476,
6.497,
6.501,
6.501
]
N=4
print("\nop2")
delta=find_delta(x,y) # N*sum of sq - sq of sum
print("delta:",delta)

m=find_m(x,y)
print("m:",m)

b=find_b(x,y)
print("b:",b)

variance=find_variance(x,y)
print("variance:",v)

sm=find_sm(x,y)
print("sm:", sm)

sb=find_sb(x,y)
print("sb:", sb)

