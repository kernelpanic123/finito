def tapis(n):
    for j in range(n):
        for i in range(n):
            if (j % 2 != 0 and i % 2 == 0) or (j % 2 == 0 and i % 2 != 0):
                print('0',end='')
            else:
                print('.',end='')
        print("")
                