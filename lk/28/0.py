def check(a, b):

    temp = int()
    check = 0

    if a == b or a == b[:len(a)]:
        check = 1
        temp = 0
        print('one')

    else:
        for i in range(0, len(b) - len(a)):
            if b[i] == a[0] and len(b) - len(a) >= len(a):
                temp = i
                if i <= len(b) - len(a):
                    for j in range(len(a)):
                        if a[j] == b[i + j]:
                            check = 1
                        else:
                            break
                    if check == 1:
                        break
        if check == 0 and a == b[-len(a):]:
            check = 1
            temp = len(b) - len(a)
            print('three')

    if check == 1:
        print('ok', temp)
    else:
        print('bad')

check('issi', 'mississippi')
