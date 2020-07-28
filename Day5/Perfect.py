import math

for num in range(1, 10000):
	result = 0
	fac = []
	for factor in range(1, int(math.sqrt(num)) + 1):
		if num % factor == 0:
			result += factor
			fac.append(factor)
			if factor > 1 and num // factor != factor:
				result += num // factor
				fac.append(num // factor)
	if result == num:
		print(num, ' ', sorted(fac))