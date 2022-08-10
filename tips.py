import sys
print('1. Iterate with enumerate() instead of range(len())')

data = [1,2,-4,-3]
for i in range(len(data)):
    if data[i]<0:
        data[i] = 0
print(data)

# Nice way 
data = [1,2,-4,-3]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0
print(data)

print('2. Use list comprehension instead of raw for loops')

squares = []
for i in range(10):
    squares.append(i*i)
print(squares)

# Nice way  
squares = [i*i for i in range(10)]
print(squares)

print('3. Sort complex iterables with sorted()')

data = [3,5,1,10,9]
sorted_data = sorted(data)
sorted_reverse = sorted(data, reverse=True)
print(sorted_data)
print(sorted_reverse)

print('4. Store unique values with sets')

my_list = [1,2,3,3,4,5,5,6]
my_set = set(my_list)
print(my_set)

print('5. Save memory with generators')

my_listt = [i for i in range(10000)]
print(sum(my_listt))
print(sys.getsizeof(my_listt), 'bytes')

my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), 'bytes')
