"""
Power full Functions
"""

#NRO. 1 - LAMBDA FUNCTION 
lambda_cube = lambda x: x*x*x

print(lambda_cube(15))

'*************************'

#NRO. 2 - MAP FUNCTION = Para iterar numerosos elementos de una lista 
fruit = ['apple', 'grapes', 'orange', 'cherry', 'kiwi']

result = map(lambda x: x.title(), fruit)

for data in result:
    print(data, end=' ')
'*************************'

#NRO. 3 - FILTER FUNCTION = Función para filtrar de una lista 
fruit = ['Apple', 'Grapes', 'Orange', 'Cherry', 'Kiwi']

#using filter function 
result = filter(lambda x: len(x)<5, fruit)

for data in result:
    print(data)
'*************************'

#NRO. 4 - ZIP FUNCTION 
fruit = ['apple', 'grapes', 'orange', 'cherry', 'kiwi']
price = [100, 80, 40, 60, 30]

result = zip(fruit, price)
for info in result:
    print(info, end='')
'*************************'

#NRO. 5 - ENUMERATE FUNCTION = ayuda mantener el seguimiento de los elementos iterables
fruit = ['apple', 'grapes', 'orange', 'cherry', 'kiwi']

for i in range(len(fruit)):
    print(i, fruit[i])

for idx, name in enumerate(fruit):
    print(idx, name)
'*************************'
   


result = map(lambda x: x.title(), fruit)

for data in result:
    print(data, end=' ')