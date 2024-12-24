from fake_math import divide as fake #импорт из модуля fake_math
from true_mat import divide as true #импорт из модуля true_math

result1 = fake(69, 3) # вычисление по функции модуля fake_math
result2 = fake(3, 0) # вычисление по функции модуля fake_math
result3 = true(49, 7) # вычисление по функции модуля true_math
result4 = true(15, 0) # вычисление по функции модуля true_math

print(result1)
print(result2)
print(result3)
print(result4)
