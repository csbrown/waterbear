import random

numbers = ['%08x' % random.randrange(16**8), '%04x' % random.randrange(16**4), '%04x' % random.randrange(16**4), '%04x' % random.randrange(16**4), '%012x' % random.randrange(16**12)]

ID = str(numbers[0])
for number in numbers[1:]:
    ID += '-' + str(number)

print ID
