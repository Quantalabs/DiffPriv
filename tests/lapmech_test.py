from DiffPriv import private

file = open('test-data.csv', 'r')

def avg(arr):

    sum = 0
    for i in arr: sum += i
    return sum / len(arr)

private.lapmech(file,'test-privatized-data.csv',3.14,avg)
