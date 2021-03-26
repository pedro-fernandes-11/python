import numpy as np
from skimage import io
import matplotlib.pyplot as plt

list1 = [1, 2, 3]
list2 = [6, 7, 8]

array = np.array([list1, list2])
print(f"Size: {len(array)}")
print(f"Format/shape: {array.shape}")
print(f"Number of dimensons: {array.ndim}")
print(f"The array itself: {array}")

# Filling an array up with determinated values
array = np.arange(1, 15, 2)  # It's similar to the range() method
print(array)

array = np.linspace(1, 20, 8, endpoint=False)
print(array)

# Zeros and Ones
zeros = np.zeros((2, 3))
print(zeros)
ones = np.ones((2, 3))
print(ones)

# Eye and Diag
eye = np.eye(5)
print(eye)

diag = np.diag(np.array([1, 2, 3, 4, 5]))
print(diag)

# Array indexing
array = np.array([1, 2, 3, 4, 5])
print(array[0])
print(array[-1])

array2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array2d)
print(array2d[0][2])

random_array = np.random.rand(3, 3)
print(random_array)
print(random_array[1][0])

# Slicing an array
matrix = np.zeros((6, 6))
num = 0

for row in range(0, 6):
    for column in range(0, 6):
        matrix[row][column] = num
        num += 1
    num += 4

print(matrix)

slicing1 = matrix[0, 3:5]
slicing2 = matrix[:,2]
slicing3 = matrix[4:6, 4:6]
slicing4 = matrix[2::2, ::2]

print(slicing1)
print(slicing2)
print(slicing3)
print(slicing4)

# Showing Image

img = io.imread('numpy-logo.jpg') # Load the image
print(img)
print(img.shape)
sliced_img = img[0:200]

plt.ylabel('height')
plt.xlabel('width')
plt.imshow(sliced_img)
# plt.show()

