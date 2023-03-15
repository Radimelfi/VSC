import math
Q2= 200
Q1 = 100
P2= 52
P1= 50

Cantidad = Q2 - Q1 /Q1
precio = P2 - P1 /P1 
EPD = Cantidad / precio 
print (round (EPD))


X = lambda Q2,Q1,P2,P1: (Q2-Q1/Q1) / (P2-P1/P1)
print(math.ceil(X(Q2=200,Q1=100,P2=52,P1=50)))


