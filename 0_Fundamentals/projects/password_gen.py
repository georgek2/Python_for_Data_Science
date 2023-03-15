import random

# for i in range(10):

#     print(random.random())

alphas = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 
        'g', 'G', 'r', 'R', 'p', 'P', 'q', 'Q', ]

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

password = ''

for i in range(11):

    password = password.join([random.choice(alphas), str(random.choice(nums))])


print(password)








