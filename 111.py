number_list = list(map(int, input('Введите любые целые числа через пробел: ').split()))
number = int(input(f'Введите любое целое число: '))


def merge_sort(number_list):
    if len(number_list) < 2:
        return number_list[:]
    else:
        middle = len(number_list) // 2
        left = merge_sort(number_list[:middle])
        right = merge_sort(number_list[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(f'Отсортированный список: {merge_sort(number_list)}')

array = merge_sort(number_list)


def binary_search_in(array, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == number:
        print(f'Номер позиции элемента, который меньше введенного пользователем числа: {middle - 1}')
        print(f'Номер позиции элемента, который равен введенному числу: {middle}')
    elif number < array[middle]:
        return binary_search_in(array, number, left, middle - 1)
    else:
        return binary_search_in(array, number, middle + 1, right)


if number < min(array) or max(array) < number:
    print('Числа нет в диапазоне')
elif number in array:
    binary_search_in(array, number, 0, len(array)-1)
elif number not in array:
    i = 0
    while i < len(array)-1:
        if array[i] >= number:
            break
        i += 1
    print(f'Номер позиции элемента, который меньше введенного пользователем числа: {i - 1}')
    print(f'Номер позиции элемента, который больше введенного числа: {i}')
