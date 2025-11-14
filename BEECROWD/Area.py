variable=[float(x) for x in input().split()]
triangle=variable[0]*variable[2]/2
circle=(variable[2]**2)*3.14159
trapezium=(variable[0]+variable[1])*variable[2]/2
square=variable[1]**2
rectangle=variable[0]*variable[1]
print(f'TRIANGULO: {triangle:.3f}\nCIRCULO: {circle:.3f}\nTRAPEZIO: {trapezium:.3f}\nQUADRADO: {square:.3f}\nRETANGULO: {rectangle:.3f}')
