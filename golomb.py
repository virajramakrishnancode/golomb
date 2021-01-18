import matplotlib.pyplot as plt

import numpy as np

import math

# golden ratio
phi = (math.sqrt(5) + 1)/2

# recursive function that eventually returns the golomb series up to a limit
def cycle(position, limit, result):
	if limit == 0:
		return result
	prev = len([num for num in result[:2] if num == position + 1])

	if result[position] - prev < 0:
		print('Teasing me huh? Naughty naughty!')
		return
	result.extend([position + 1] * (result[position] - prev))
	return cycle(position + 1, limit - 1, result)

# test golomb sequences up to starting number 5
test_num = 5

for x in range(0, test_num):
	for y in range(2, test_num):

		if y != x and cycle(0, 4, [x, y]):

			plt.plot(cycle(0, 130, [x, y]))


values = np.linspace(1, 2000, 200)

y = [phi**(2 - phi) * x**(phi - 1) for x in values]

z = [x**0.643 for x in values]

# graphing
plt.xlabel('n')
plt.ylabel('nth term of golomb sequence')

plt.plot(values, y, 'red', label='y = actual formula')
plt.plot(values, z, 'blue', label='y = x**0.643')


plt.legend(loc = 'upper left')
plt.show()



