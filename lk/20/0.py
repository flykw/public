def f(s):
    #s_open = {}
    # for i in range(0, len(s)):
    # for i in s:
        # if i in "({[":
            # s_open.addend(i)
            # print('ok')
    stack = ''
    base_dict = {'(':')', '{':'}', '[':']'}

    if len(s) > 1 and len(s) % 2 == 0 and s[0] in base_dict.keys() and s[len(s) - 1] in base_dict.values():

        for i in range(0, len(s)):
            now = s[i]
            if stack == '':
                if now in base_dict.keys(): 
                    stack += now
                else:
                    return False
            #fix
            elif stack != '':
                if now in base_dict.values():
                    if base_dict[stack[-1:]] == now:
                        stack = stack[:-1]
                    else:
                        return False
                else:
                    stack += now
            else:
                return False
            print('stack', stack)
        
        if stack == '':
            return True
        else:
            return False
    else:
        return False

#print(f('([}}])'))
print(f('()))'))

