# kata: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1 

# TODO: i can't find proper algorithm for this...
# need to think about solution

def snail(arr):
    res = []
    offset = 0
    distance = len(arr[0]) - 1
    print(snake_hor(arr, offset, distance, -1))

def snake_hor(arr, offset, distance, step):
    sub_arr = arr[offset*step][offset:distance:step]
    print(arr[offset*step])
    return sub_arr


def snake_ver(arr, offset, distance, step): 
    pass
            

if __name__ == "__main__":
    array = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    assert snail(array) == [1,2,3,6,9,8,7,4,5]
    array = [
        [1,2,3,1],
        [4,5,6,4],
        [7,8,9,7],
        [7,8,9,7]
    ]
    assert snail(array) == [1,2,3,4,5,6,7,8,9]
