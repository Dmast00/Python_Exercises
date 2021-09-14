ipt = []

def sort_num(ipt):
    n = len(ipt)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if ipt[j] > ipt[j+1]:
                ipt[j], ipt[j+1] =ipt[j+1],ipt[j]

while True:
    result = input('value:')
    
    if result.isnumeric():
        ipt.append(result)

    elif result.isalpha:
        if result == 'done':
            sort_num(ipt)
            print(ipt)
        else:
            print('invalid input')
    else:
        break





