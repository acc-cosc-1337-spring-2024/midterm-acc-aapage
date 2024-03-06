#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_random_number():
    # I wasn't sure if the random module was allowed on the exam but I don't know another way
    # I have prior experience coding in Python and this is the only way I know how to get randomness to happen
    from random import randrange
    randnum = randrange(1, 6)
    return randnum