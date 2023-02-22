import random
import time
user_m = int(input('1st dimension = '))
user_n = int(input('2nd dimension = '))
user_min_limit = int(input('min = '))
user_max_limit = int(input('max = '))
mass=[]
for i in range(user_m):
    mass.append([])
    for j in range(user_n):
        mass[i].append('')
for i in range(user_m):
    for j in range(user_n):
        mass[i][j] = random.randint(user_min_limit, user_max_limit)
print(*mass)