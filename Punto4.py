#Número reales
l=[]
print ('Ingrese cuatro números reales')
n1=float(input('Ingrese el primer número: '))
l.append(n1)
n2=float(input('Ingrese el segundo número: '))
l.append(n2)
n3=float(input('Ingrese el tercer número: '))
l.append(n3)
n4=float(input('Ingrese el cuarto número: '))
l.append(n4)
n5=float(input('Ingrese el cuarto número: '))
l.append(n5)
print(l)

max_value=max(l)
min_value=min(l)
average=sum(l)/len(l)
print(f"El valor maximo es: {max_value}")
print(f"El valor minimo es: {min_value}")
print(f"El promedio es: {average}") 
