#write functions here, don't add input('') statements here!
def is_prime(num):
    
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            bool_prime = False
            break
    else:
        bool_prime = True

    return bool_prime