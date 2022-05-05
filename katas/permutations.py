# kata: https://www.codewars.com/kata/5254ca2719453dcc0b00027d

# TODO: code below working very slow, for test i picked original attempt's word "mgpelxy" to perform permutations with it...
# but on codewars it's timed out...
# need to find a way to speed up the code

import time
from math import factorial


def permutations(string):
    if len(string) == 0 or len(string) == 1: return string
    res = [string]
    res_max_len = factorial(len(string))
    query = [string]
    i = 1
    while i < res_max_len:
        # print(i)
        # print(res)
        # print(query)
        try:
            traversed_list = traverse_string(query.pop())
        except IndexError:
            break
            
        for combination in traversed_list:
            if combination not in res:
                res.append(combination)
                query.append(combination)
                i += 1
    return res
    
def traverse_string(string: str) -> list:
    retlist = [string]
    for x in range(len(string)):
        a = string[x]
        if x < len(string) - 1:
            # switch neighbour elements
            b = string[x+1]
            try:
                appstr = string[:x] + b + a + string[x+2:]
            except IndexError:
                appstr = string[:x] + b + a
        elif x == len(string) - 1:
            # switch last with first element
            b = string[0]
            appstr = a + string[1:x] + b
        retlist.append(appstr)
    return retlist

def main():
    string = "mgpelxy"
    start_time = time.time()
    result = permutations(string)
    total_time = time.time() - start_time
    print(len(result), factorial(len(string)))
    print(total_time)


if __name__ == "__main__":
    main()