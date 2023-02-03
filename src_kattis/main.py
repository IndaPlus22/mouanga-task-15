"""

Author: Anders Mouanga (salticecream)
Description: Solution to "Almost Union-Find" Kattis problem, in Python
Note: There is almost surely a more Pythonic way to solve this problem by using (more) built-in functions.
However, in what I believe to be the spirit of the course, I have decided to solve the problem my way.

"""







parents = [0]

# get total numbers and total commands
INITIAL_INPUT_LIST = tuple(input().split(" "))
TOTAL_NUMBERS, TOTAL_COMMANDS = INITIAL_INPUT_LIST
TOTAL_NUMBERS, TOTAL_COMMANDS = int(TOTAL_NUMBERS), int(TOTAL_COMMANDS)

# generate number list
for number in range(TOTAL_NUMBERS):
    parents.append(number + 1)

# find the parent of the given number in the union find structure
def find_parent(p):
    if parents[p] != p:
        return find_parent(parents[p])
    else:
        return p

# union the graphs with p and q in them
def fun1(p, q):
    # we make p's set a subset of q's set
    parents[find_parent(q)] = find_parent(p)
    print(parents)


# put p in the list containing q
def fun2(p, q):
    # we change p's parent to q's parent
    parents[p] = parents[find_parent(q)]
    print(parents)


# return the sum and amount of elements in p
# i didn't find a smart way to do this without going over the entire array
def fun3(p):
    parent = find_parent(p)
    print("My parent is", parent, "therefore I am going to look at the indices which are equal to", parent)
    sum = 0
    count = 0
    for index in range(len(parents)):
        if parents[index] == parent:
            count += 1
            sum += index
    
    print(count, sum, "and the list is", parents, sep=" ")


for _ in range(TOTAL_COMMANDS):
    new_inputs = tuple(input().split(" "))
    command, arg1 = int(new_inputs[0]), int(new_inputs[1])
    if len(new_inputs) == 3:
        arg2 = int(new_inputs[2])
    
    match command:
        case 1: fun1(arg1, arg2)
        case 2: fun2(arg1, arg2)
        case 3: fun3(arg1)





"""
Old solution

# we don't want empty lists in `LISTS`
def clean_list():
    for list_index in LISTS:
        if LISTS[list_index] == []:
            LISTS.pop(list_index)
    # Note that this only removes the first empty list, however we shouldn't ever get a situation where we have two empty lists at once


def get_indices(p, q):
    p_list_index = -1
    q_list_index = -1
    for list_index in range(len(LISTS)):
        if p in LISTS[list_index]:
            p_list_index = list_index
            break
        if q in LISTS[list_index]:
            q_list_index = list_index
            break
    return (p_list_index, q_list_index)


# function 1
""
Union the sets containing p and q. If p and q are already in the same set, ignore this command.
""
def fun1(p, q):
    p_list_index, q_list_index = get_indices(p, q)

    # terminate the function if any of these are true
    if(
    p_list_index == -1 or           # p was not in any of those lists
    q_list_index == -1 or           # q was not in any of those lists
    p_list_index == q_list_index    # p and q are in the same list
    ):
        return

    else:
        # add the list with q in it, to the list with p in it
        # then remove the list that originally had q in it
        LISTS[p_list_index] = LISTS[p_list_index] + LISTS[q_list_index]
        LISTS.pop(q_list_index)
        clean_list()
    
    


# function 2
""
Move p to the set containing q. If p and q are already in the same set, ignore this command
""
def fun2(p, q):
    p_list_index, q_list_index = get_indices(p, q)

    # terminate the function if any of these are true
    if(
    p_list_index == -1 or           # p was not in any of those lists
    q_list_index == -1 or           # q was not in any of those lists
    p_list_index == q_list_index    # p and q are in the same list
    ):
        return

    else:
        # find p within the list
        p_index = -1
        for number in range(len(LISTS[p_list_index])):
            if number == p:
                p_index = number
                break
        
        # move p from its list to the list with q in it
        LISTS[q_list_index].append(LISTS[p_list_index.pop(p_index)])
        clean_list()


# function 3
""
Return the number of elements and the sum of elements in the set containing p.
""
def fun3(p):
    sum = 0
    p_list_index = get_indices(p, "")[0]
    
    # find the sum
    for number in LISTS[p_list_index]:
        sum += number
    
    print(len(LISTS[p_list_index]), sum, sep=" ")

    
    



"""