import math
import matplotlib.pyplot as plt

z=1
a=0.5291772083
res = [0]*30
for i in range(30):
    r=i/1
    res[i]=(z/a)**(3/2)*(2*math.exp((-z*r)/a))                                                                #R10
    res[i]=(z/(2*a))**(3/2)*(2*(1-(z*r/(2*a))))*math.exp((-z*r)/(2*a))                                        #R20
    res[i]=(z/(2*a))**(3/2)*(2/math.sqrt(3))*(z*r/2*a)*math.exp((-z*r)/2*a)                                   #R21
    res[i]=(z/(3*a))**(3/2)*2*(1-2*z*r/(3*a)+2/3*(z*r/(3*a))**2)*math.exp((-z*r)/(3*a))                       #R30
    res[i]=(z/(3*a))**(3/2)*(4*math.sqrt(2)/3)*((z*r)/(3*a))*(1-(1/2)*((z*r)/(3*a)))*math.exp((-z*r)/(3*a))   #R31
    res[i]=(z/(3*a))**(3/2)*(2*math.sqrt(2)/(3*math.sqrt(5)))*(((z*r)/(3*a))**2)*math.exp((-z*r)/(3*a))        #R32
    print(res[i])
plt.plot(res,label='result')
plt.show()