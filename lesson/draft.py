#from collections import deque

#temps = [20.6, 19.4, 19.0, 19.0, 22.1,
     #   22.5, 22.8, 24.1, 25.6, 27.0,
      #  27.0, 25.6, 26.8, 27.3, 22.5,
       # 25.4, 24.4, 23.7, 23.6, 22.6,
       # 20.4, 17.9, 17.3, 17.3, 18.1,
        #20.1, 22.2, 19.8, 21.3, 21.3,
        #21.9]
#days = deque(maxlen=7)
 
#for temp in temps:
    # Добавляем температуру в очередь
 #   days.append(temp)
    # Если длина очереди оказалась равной максимальной длине очереди (7),
    # печатаем среднюю температуру за последние 7 дней
  #  if len(days) == days.maxlen:
   #     print(round(sum(days) / len(days), 2), end='\n')
# Напечатаем пустую строку, чтобы завершить действие параметра
# end. Иначе следующая строка окажется напечатанной на предыдущей
#print("")

import numpy as np
np.random.seed(2021)
simple = np.random.rand()
print(simple)
randoms  = np.random.uniform(-150, 2021, size = 120)
print(randoms)
table = np.random.randint(1, 101, size=(3,2))
print (table)

even = np.arange(2, 17, 2)
print(even)
mix = even
print(np.random.shuffle(mix))
print(mix)
select = np.random.choice(even, size=3, replace=False)
print(select)
triplet = np.random.permutation(select)
print(triplet)

print(np.mean([19, 242, 14, 152, 142, 1000]))
import pandas as pd
print(pd.__version__)
print(pd.__name__)