import time
startTime = time.time()
# Calculate the product of the first 1,000,000,000 numbers.
product = 1
for i in range(1, 100000):
    product = product * i
endTime = time.time()
print('The result is %s digits long.' % (len(str(product))))
print('Took %s seconds to calculate.' % (endTime - startTime))
