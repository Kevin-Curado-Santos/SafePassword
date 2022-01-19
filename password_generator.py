from random import sample

def random_password_generator(length, upper_enabled, digits_enabled, special_char_enabled):
    ''' Generates a random password with a length from 1 to 90 of characters
        type of password can be specified by enabeling upper case letters, digits and special characters'''

    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_char = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


    reference = lower_case
    
    if upper_enabled:
        reference += upper_case
    if digits_enabled:
        reference += digits
    if special_char_enabled:
        reference += special_char
    
    random_char_list = sample(reference, length)

    return ''.join(random_char_list)

