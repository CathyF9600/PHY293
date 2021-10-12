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
sum_of_sq_for_x = sum( [sq(x[0]), sq(x[1]), sq(x[2]), sq(x[3])] )
def sq(n):
    return n**2

def find_delta(x,y):
    sum_of_sq_for_x
    delta=N*sum_of_sq_for_x - sq(sum(x))
    return delta

def find_m(x,y):
    m=( N*sum([ x[0]*y[0], x[1]*y[1], x[2]*y[2], x[3]*y[3]]) - sum(x)*sum(y))/delta
    return m

def find_b(x,y):
    b=(sum(y)-m*sum(x))/N
    return b

def find_variance(x,y,m,b):
    v = ( sq(y[0]-(b+m*x[0])) + sq(y[1]-(b+m*x[1])) + sq(y[2]-(b+m*x[2])) + sq(y[3]-(b+m*x[3])) ) / (N-2)
    return v

def find_sm(x,y):
    sm=(N*( variance / delta ))**0.5
    return sm

def find_sb(x,y):
    sb=( variance * sum_of_sq_for_x / delta )**0.5
    return sb

def find_chi(x,y,m,b):
    y_expected=[]
    for el in x:
        expected=m*el+b
        y_expected.append(expected)
    chi=0
    for i in range(4):
        ele=sq(y[i]-y_expected[i]) / y_expected[i]
        chi+=ele

    return chi

print("op1")
delta=find_delta(x,y) # N*sum of sq - sq of sum
print("delta:",delta)

m1=find_m(x,y)
print("m:",m1)

b=find_b(x,y)
print("b:",b)

v=find_variance(x,y,m1,b)
print("variance:",v)

sm=find_sm(x,y)
print("sm:", sm)

sb=find_sb(x,y)
print("sb:", sb)

print("chi:",find_chi(x,y,m,b))

def find_RSQ(x,y,m,b):
    deno=0
    avgV = find_avg(y[0],y[1],y[2],y[3])
    for i in range(4):
        diff=sq(y[i]-avgV)
        deno+=diff
    variance = find_variance(x,y,m,b)
    return 1-((N-2)*variance)/deno

RSQ=find_RSQ(x,y,m1,b)
print("RSQ",RSQ)

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

z = [464.5,
2691.0,
27090.1,
98950.0
]
def find_Rv(I_a,V_v,R_l):
    return (I_a/V_v-1/R_l)**(-1)
N=4
print("\nop2")
delta=find_delta(x,y) # N*sum of sq - sq of sum
print("delta:",delta)

m2=find_m(x,y)
print("m:",m2)

b=find_b(x,y)
print("b:",b)

variance=find_variance(x,y,m2,b)
print("variance:",v)

sm=find_sm(x,y)
print("sm:", sm)

sb=find_sb(x,y)
print("sb:", sb)

print("chi:",find_chi(x,y,m,b))

RSQ=find_RSQ(x,y,m2,b)
print("RSQ",RSQ)

R_v=[]
for i in range(4):
    print("Rv:",find_Rv(x[i],y[i],z[i]))
    R_v.append(find_Rv(x[i],y[i],z[i]))
R_a=[-3.371,
1.751387181,
1.650,
2.041

]

def find_avg(a,b,c,d):
    return (a+b+c+d)/4
Rv=find_avg(R_v[0],R_v[1],R_v[2],R_v[3])
Ra=find_avg(R_a[0],R_a[1],R_a[2],R_a[3])
print("Rv avg:",Rv)
print("Ra avg:",Ra)

R1=(-Rv*m1)/(Rv+m1)
print("R1:",R1)
R2 = -Ra-m2
print("R2:",R2)







