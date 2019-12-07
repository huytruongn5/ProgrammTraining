# python list == Java array

test_list = [] # or list()

test_list.append(1)

test_list.append(2)

test_list.append(3)

print(test_list)

pop = test_list.pop(0)

print(pop)

print(test_list)

print('length', len(test_list))


test_list.append(4)
test_list.append(5)
test_list.append(6)

print(test_list)

# for item in test_list:
#     print(item)

# count = 0
# while count <= len(test_list) - 1: # 5 
#     # 0 <= 5 -1 [0, 1, 2, 3, 4]
#     print(test_list[count])
#     count += 1

position = 0
while True:
    print('position', position)
    print('test_list', test_list[position])
    if test_list[position] == 4:
        print('result', test_list[position])
        break
    position += 1


array_2d = [[1,2],[2,3],[3,4]]

for row in array_2d:
    print(row)


# [print(i) for i in test_list]