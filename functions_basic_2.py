# def countdown (num):
#     new_list = []
#     for x in range (num,-1,-1):
#         new_list.append(x)
#     return new_list
# print(countdown(5))

# def print_and_return(list):
#     print (list[0])
#     return list[1]

# print(print_and_return([1,2]))

# def first_plus_length(list):
#     return list[0] + len(list)

# print(first_plus_length([5,8,12,14,6]))

# def values_greater_than_second(list):
#     if len(list) < 2:
#         return False
#     new_list =[]
#     for x in range(0,len(list)):
#         if list[x] > list[1]:
#             new_list.append(list[x])
#     print(len(new_list))
#     return new_list

# print(values_greater_than_second([4,5,6,7,8]))
# print(values_greater_than_second([5]))

def this_length_that_value(size,value):
    list = []
    for x in range(0,size):
        list.append(value)
    return list

print(this_length_that_value(3,6))