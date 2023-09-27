
from calendar import c


def minTimeSpent(c_train, c_dur, d_train, d_dur):
    c_list = []
    for i in range(len(c_train)):
        c_list.append((c_train[i], c_dur[i]))

    d_list = []
    for i in range(len(d_train)):
        d_list.append((d_train[i], d_dur[i]))


    # c_list.sort()
    # d_list.sort()
    # print(c_list)
    # print(d_list)

    min_time = float('+inf')
    for i in range(len(c_list)):
        for j in range(len(d_list)):
            if c_list[i][0] < d_list[j][0]:
                time = c_list[i][0] + c_list[i][1]
                if d_list[j][0] < time:
                    continue
                else:
                    time = d_list[j][0] + d_list[j][1]
            elif c_list[i][0] > d_list[j][0]:
                time = d_list[j][0] + d_list[j][1]
                if c_list[i][0] < time:
                    continue
                else:
                    time = c_list[i][0] + c_list[i][1]
            else:
                continue
            print("c_list: ", c_list[i])
            print("d_list: ", d_list[j])
            min_time = min(min_time, time)
    return min_time


# print(minTimeSpent([1,4], [3,2], [5,2], [2,2]))
# print(minTimeSpent([1,2,3], [1,1,1], [1,2,3], [10,5,1]))
print(minTimeSpent([1,1], [1,1], [1,1,1], [1,1,1]))


        
