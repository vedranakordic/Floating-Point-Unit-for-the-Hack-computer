def isThereDot(x):

    operator = '+-*/&|<>='

    x = str(x)

    flag = 0
    line = None
    line2 = None
    
    for i in x:
        if i in operator:
            line = x.split(i)
            flag = 1
            break
        else:
            line2 = x

            flag = 0


    if flag == 1:
        for i in line:
            res = i.split('.')
            if len(res) == 2:
                return 1
            else:
                return 0
    else:
        res = line2.split('.')
        if len(res) == 2:
            return 1
        else:
            return 0

    

