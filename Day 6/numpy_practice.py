import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d)
print(arr_1d.shape, arr_1d.ndim, arr_1d.dtype)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
print(arr_2d.shape, arr_2d.ndim, arr_2d.size)

print(np.zeros((2, 4)))
print(np.ones((3, 3)))
print(np.arange(10, 30, 5))
print(np.linspace(0, 1, 5))
print(np.random.randint(1, 100, size=(2, 3)))

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[2])
print(arr[1:5])
print(arr[-3:])

matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(matrix[1, 2])
print(matrix[0, :])
print(matrix[:, 1])
print(matrix[0:2, 0:2])

scores = np.array([45, 88, 72, 95, 30, 64, 91])
print(scores[scores >= 70])

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a * 3)

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(np.dot(m1, m2))

stats_arr = np.array([15, 42, 88, 23, 94, 67, 51])
print(np.sum(stats_arr))
print(np.mean(stats_arr))
print(np.median(stats_arr))
print(np.std(stats_arr))
print(np.var(stats_arr))
print(np.max(stats_arr), np.argmax(stats_arr))
print(np.min(stats_arr), np.argmin(stats_arr))

grid = np.array([[80, 90, 85], [70, 75, 80], [95, 92, 98]])
print(np.sum(grid, axis=0))
print(np.mean(grid, axis=1))

flat = np.arange(1, 13)
r3x4 = flat.reshape(3, 4)
print(r3x4)
print(flat.reshape(2, 6))
print(r3x4.T)
print(r3x4.flatten())
