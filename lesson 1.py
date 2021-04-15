#1
a=20
b=32
c='24'
d='spam'
print(a,b,c,d)
#2
seconds = 720666 #время составляет 720666 секунды
hours = seconds // 3600
hours = hours % 24
minutes = seconds // 60
minutes = minutes % 60
seconds = seconds % 60
print(f"{hours}:{minutes}:{seconds}")
#3
n = 3
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print(comp)
#4
i = 349876
s = str(i)
ls = list(map(int, s))
r = max(ls)
print(r)
#5
proceeds = 750000000 # Выручка фирмы
costs = 250000 # Издержки фирмы
if proceeds > costs:
    print("Фирма работает с прибылью")
    income = proceeds - costs #Рентабельность фирмы
    print('Рентабельность фирмы {:%}'.format(income / proceeds))
    employees =  5 #Кол-во сотрудников
    print(f"{income / employees} ") #Прибыль на сотрудника
else:
    print('Фирма работает без окупаемости')
#6
start_distance = 2
target_distance = 3

distance_ = start_distance
day_counter = 1

while distance_ < target_distance:
    day_counter += 1
    distance_ *= 1.1

print(day_counter)




