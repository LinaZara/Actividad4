#Conversión de temperaturas
repetir='S'
while repetir=='S' or repetir=='s': 
	print('Ingrese la temperatura en Grados Celsius')
	c=float(input('Temperatura: '))
	print('Presione 1 si desea Grados Fahrenheit')
	print('Presione 2 si desea Grados Rankine')
	print('Presione 3 si desea Grados Kelvin')
	num=int(input('Ingrese la opción: '))

	if num==1:
		f=round(((9/5)*c) + 32,1)
		print(c,'Grados Celsius', 'es equivalente a', f,'Grados Fahrenheit')
	elif num==2:
		r=round(((c*1.8)+491.67),1)
		print(c,'Grados Celsius', 'es equivalente a', r,'Grados Rankine')
	elif num==3:
		k=round(c+273.15,1)
		print(c,'Grados Celsius', 'es equivalente a', k,'Grados Kelvin')
	else: 
		print('Número inválido. Ingrese un número válido')

	repetir=input('¿Desea continuar S/N?')

