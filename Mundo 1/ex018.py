import math
ang=float(input('digite um angulo '))

seno=math.sin(math.radians(ang))
cosseno=math.cos(math.radians(ang))
tangente=math.tan(math.radians(ang))

print('angulo {} seno corresponde {:.2f} '.format(ang,seno))
print('angulo {} cosseno corresponde {:.2f} '.format(ang,cosseno))
print('angulo {} tangente corresponde {:.2f} '.format(ang,tangente))
