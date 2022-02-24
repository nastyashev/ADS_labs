from random import randint
from sort_algorithms import *

size = int(input('Введіть розмір масиву: '))
arr_best = [i for i in range(size)]
arr_worst = [size-1-i for i in range(size)]
arr_rand = [randint(0,size) for i in range(size)]

#print('\nНайкращий випадок')
#print('\nНайкращий випадок\n', arr_best)
#n_comp_b, n_perm_b = alg_choice(arr_best)
#print('Кількість порівнянь - ', str(n_comp_b))
#print('Кількість перестановок - ', str(n_perm_b))
#print('Відсортований масив\n', arr_best)

#print('\nНайгірший випадок')
#print('\nНайгірший випадок\n', arr_worst)
#n_comp_w, n_perm_w = alg_choice(arr_worst)
#print('Кількість порівнянь - ', str(n_comp_w))
#print('Кількість перестановок - ', str(n_perm_w))
#print('Відсортований масив\n', arr_worst)

print('\nВипадкове заповнення')
#print('\nВипадкове заповнення\n', arr_rand)
n_comp_r, n_perm_r = alg_choice(arr_rand)
print('Кількість порівнянь - ', str(n_comp_r))
print('Кількість перестановок - ', str(n_perm_r))
#print('Відсортований масив\n', arr_rand)
