def bubble_sort(arr):
    n_comp = 0
    n_perm = 0
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            n_comp += 1
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                n_perm += 1
    return n_comp, n_perm

def comb_sort(arr):
    n_comp = 0
    n_perm = 0
    size = len(arr)
    factor = 1.247
    gap_factor = size / factor
    while gap_factor > 1:
        gap = int(gap_factor)
        for i in range(0, size - gap, gap):
            n_comp += 1
            if arr[i] > arr[i + gap]:
                tmp = arr[i]
                arr[i] = arr[i + gap]
                arr[i + gap] = tmp
                n_perm += 1
        gap_factor /= factor
    return n_comp, n_perm

def alg_choice(arr):
    alg = input('Натисніть літеру, щоб вибрати алгоритм сортування. (бульбашкою - b, гребінцем - c): ')
    n_comp, n_perm = 0, 0
    if alg == 'b':
        n_comp, n_perm = bubble_sort(arr)
    elif alg == 'c':
        n_comp, n_perm = comb_sort(arr)
    else:
        print('Неправильна буква!')
    return n_comp, n_perm