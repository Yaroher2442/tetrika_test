def task(array):
    # list.index
    return list(array).index('0')


# Сложность O(n)

def task_1(array):
    # str.index
    return array.index('0')


# Сложность O(n)

def task_2(array):
    # my for
    for i in range(len(array)):
        if array[i] == '0':
            return i
        else:
            continue


# Сложность O(n)

def main():
    print(task("111111111111111111000000000000000000"))
    print(task_1("111111111111111111000000000000000000"))
    print(task_2("111111111111111111000000000000000000"))


if __name__ == '__main__':
    main()
