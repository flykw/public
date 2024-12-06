def check():
    temp = ''
    check = 0

    for i in range(0, len(b[:len(a)])):
        if b[i] == a[0]:
            if i <= len(b) - len(a):
                for j in range(len(a)):
                    if a[j] != b[i + j]:
                        check = 1
    if a == b[len(a):]:
        check = 1

    if check == 1:
        print('ok')
    else:
        print('bad')




check()
