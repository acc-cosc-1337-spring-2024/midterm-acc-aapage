#write functions here, don't add input('') statements here!
def get_sum_of_evens(num):
    i = 1
    even_numbers = []
    sum_evens = 0
    while i <= num:
        if i % 2 == 0:
            even_numbers.append(i)
        i += 1

    for even in even_numbers:
        sum_evens += even
    return sum_evens
