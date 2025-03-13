def editing_data(number):
    final = ''
    datas = []
    for i in range(number):
        data = [str(x) for x in input().split('.')]
        datas.append(data)
    for every in datas:
        every[1] = every[1].capitalize()
    datas.sort()
    for every in datas:
        final += '%s %s %s\n' %(every[0], every[1], every[2])
    return print(final)
n = int(input())
database = editing_data(n)
    