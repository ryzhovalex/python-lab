# kata: https://www.codewars.com/kata/5262119038c0985a5b00029f 

# TODO: optimize this function (too sloooow......)

def is_prime(num):
    if num <= 1:
        return False
    
    x = 2
    while x < num:
        if num % x == 0:
            return False
        x += 1
    return True

def main():
    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(9) == False
    assert is_prime(41) == True
    assert is_prime(45) == False


if __name__ == "__main__":
    main()