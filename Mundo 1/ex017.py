import math
catoposto= float(input('comprimento do cateto oposto '))
catadjacente= float(input('comprimento do cateto adjacente '))
hi = (catoposto **2 + catadjacente ** 2) ** (1/2)
hi1 = math.hypot(catoposto,catadjacente)
print(' matematicamente a hipotenusa medi {:.2f} '.format(hi))
print(' com importaçao a hipotenusa medi {:.2f} '.format(hi1))