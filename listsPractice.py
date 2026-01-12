spam = ["Volvo", "BMW", "Ford", "Mazda"]


def listReader(target):
    result = ''
    if target == []:
        print('List is empty :c')
    else:
        for i in target:
            if target.index(i) == len(target)-1:
                result += 'and ' + i
            else:
                result += i + ', '
    print(result)
    return


listReader(spam)