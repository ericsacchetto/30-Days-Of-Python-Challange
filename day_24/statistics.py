import numpy as np

print('numpy:', np.__version__)
# print(dir(np))

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)
print(type(two_dimensional_list))

# Numpy array
numpy_array = np.array(two_dimensional_list)
print(numpy_array)
print(type(numpy_array))
print('Shape ', numpy_array.shape)
print('Data type ', numpy_array.dtype)

python_list = [1, 2, 3, 4, 5]
numpy_float_array = np.array(python_list, dtype=float)
print(numpy_float_array)
print(type(numpy_array))
print('Shape ', numpy_float_array.shape)
print('Data type ', numpy_float_array.dtype)

python_booleans = [1, 0, 1, -1, 0, 0]
numpy_bool_array = np.array(python_booleans, dtype=bool)
print(numpy_bool_array)
print(type(numpy_bool_array))
print('Shape ', numpy_bool_array.shape)
print('Data type ', numpy_bool_array.dtype)

print(numpy_float_array.tolist())
print(type(numpy_float_array.tolist()))

python_tuple = (1, 2, 3, 4)
numpy_tuple_array = np.array(python_tuple)
print(numpy_tuple_array)
print(type(numpy_tuple_array))

# Math operations

numpy_float_array_ten = numpy_float_array + 10
print('Array + 10 ', numpy_float_array_ten)

numpy_byte_array = np.array([8, 9, 10, 11])
numpy_byte_array_times = numpy_byte_array * 2
print('Array times 2 ', numpy_byte_array_times)

# Two dimensional arrays
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(two_dimension_array)
print('First row\t ', two_dimension_array[0])
print('Second row\t ', two_dimension_array[1])
print('Third row\t ', two_dimension_array[2])
print('First column\t ', two_dimension_array[:, 0])
print('Second column\t ', two_dimension_array[:, 1])
print('Third column\t ', two_dimension_array[:, 2])

sliced_array = two_dimension_array[0:3, 0:2]  # rows x lines
print('Sliced Array ', sliced_array)

# Reversing array
reversed_two_dimension_array = two_dimension_array[::-1, ::-1]
print('Reversed array ', reversed_two_dimension_array)

# Zeroes and ones
numpy_zeroes = np.zeros((4, 4), dtype=int)
print(numpy_zeroes)

numpy_ones = np.ones((4, 4), dtype=int)
print(numpy_ones)

# Reshape flat
normal_array = np.array([[1, 2, 3], [4, 5, 6]])
print('Normal array ', normal_array)
reshaped_array = normal_array.reshape(3, 2)
print('Reshaped array ', reshaped_array)
print('Flattened array ', normal_array.flatten())

# Random numbers
random_int = np.random.randint(0, 11)
print('Random between 0 and 10: ', random_int)

random_array = np.random.randint(2, 11, size=(3, 3))
print('Random array: ', random_array)

# Statistic
from scipy import stats
import matplotlib.pyplot as plt
np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis, keepdims=True))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

