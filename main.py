import numpy as np
print(np.__version__)

# my_list = [1, 2, 3, 4]

# my_list = my_list * 2

# print(my_list)

#Estos son arrays

# array = np.array([1, 2, 3, 4])
# array = array * 2
# print(array)
# print(type(array))

#Una matriz de dimension 0

array_a = np.array('A') #dimension 0

#Dimension 1
array_a = np.array(['A', 'B', 'C'])

#Dimension 2
array_a = np.array([['A', 'B', 'C'],
                   ['D', 'F', 'E'],
                   ['G', 'H', 'J']])

#Dimension 3
array_a = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
saludo = array_a[0, 2, 1] + array_a[1, 1, 2] + array_a[1, 0, 2] + array_a[0, 0, 0]
print(saludo)
print(array_a.ndim)
print(array_a.shape)