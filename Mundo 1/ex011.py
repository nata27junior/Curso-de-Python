alt = float(input('altura parede : '))
lar = float(input('largura parede : '))
area = alt * lar
tinta = area / 2
print('dimensao {:.2f} X {:.2f}  area é {:.2f} m² vai precisar {:.2f} tinta'.format(alt,lar,area, tinta))
