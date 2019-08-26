import itertools
import random
import numpy

# sum = 0
# for num,value in enumerate(itertools.permutations(base_list,9)):
#     if (value[2] == 1 and value[5] == 7)\
#      and (value[0] not in [1,7,3,5]) and (value[1] not in [1,7,5,2,3])\
#      and (value[4] not in [5,4,6,7]) and (value[3] not in [1,3,6,5,7])\
#      and (value[6] not in [1,4,7,5]) and (value[7] not in [3,4,1,7])\
#      and (value[2] not in [3,5,7]) and (value[5] not in [1,8,5,6]):
#         #print(num,value)
#         sum += 1
# print(sum)
#print(len())
#1.生成数独
#2.消掉数独
#3.填写数独
#4.验证数独

def judge(x, y, number, data):
    base_set = set(base_list)
    #判断行
    if number in data[x]:
        #print('hang')
        return False
    #判断列
    if number in [ data[i][y] for i in range(len(data[0])) ]:
        #print('lie')
        return False
    #判断九宫格
    for count  in range(y % 3 + x % 3 * 3):
        if number == data[ x // 3 * 3 + count // 3][ y // 3 * 3 + count % 3]:
            #print('jiu')
            return False
    return True

def fill(i,j):
    global data
    if i > 8:
        return True
    s = random.randint(1, 9)
    for k in range(9,1,-1):
        p = (s + k) % 9 + 1;
        if judge(i, j, p, data):
            data[i][j] = p;
            if j == 8:
                i += 1
                j = 0
            else:
                j += 1
            if fill(i, j):
                return True
    return False

if __name__ == "__main__":
    base_list = [1,2,3,4,5,6,7,8,9]
    random.shuffle(base_list)
    data = numpy.zeros(shape=(9,9))
    data[0] = base_list
    print(base_list)
    while True:
        if data[8][8]:
            break
        else:
            random.shuffle(base_list)
            data = numpy.zeros(shape=(9,9))
            data[0] = base_list
            result = fill(1,0)
    #result = judge(1, 0, base_list[3], data)
    print(data)