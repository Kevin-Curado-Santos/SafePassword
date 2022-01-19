import tabulate, file_manager, Stats, pyperclip, password_generator

options = [['AES', '3DES', 'DES']]

def user_operation():

    print('To encrypt type: 1\n')
    print('To decrypt type: 2\n')
    print('To generate a random password type: 3')
    operation = int(input('\n'))
    while operation < 0 and operation > 4:
        print(f'{operation} is not an option! Try again.')
        operation = int(input())

    return operation


def user_option():

    print('\nWhat method would you like to use?')
    print(tabulate.tabulate(options, tablefmt='fancy_grid'), end = '\n')
    option = input()
    while option.upper() not in options[0]:
        print('Not an option! Try again.')
        option = input()

    return option

def option_getter(key):

    key_length = len(key)

    if key_length == 24:
        return '3DES'
    elif key_length == 16:
        return 'AES'
    else:
        return 'DES'

    

def main():

    print('Welcome to SafePassword\n')

    operation = user_operation()

    if operation == 1:
        option = user_option().lower()
        
        password = input('\nEnter a password you would like to be encrypted: \n')
        
        filename = input('\nEnter a name for a file where the password will be stored: \r\n')
        print(f'\nYour password was successfully stored in {filename}!')

        if option == 'aes':

            key, nonce, encrypted_password = Stats.AESEncryptionStats(password)
        elif option == '3des':

            key, nonce, encrypted_password = Stats.TripleDESEncryptionStats(password)
        else:
            
            key, nonce, encrypted_password = Stats.DESEncryptionStats(password)


        file_manager.save_information(key, nonce, encrypted_password, filename)

    elif operation == 2:

        filename = input('\nEnter the name of the file where the password is stored: \n')

        key, nonce, encrypted_password = file_manager.get_information(filename)

        option = option_getter(key)

        if option == 'AES':
            decrypted_password = Stats.AESDecryptionStats(encrypted_password, key, nonce)
        elif option == '3DES':
            decrypted_password = Stats.TripleDESDecryptionStats(encrypted_password, key, nonce)
        else:
            decrypted_password = Stats.DESDecryptionStats(encrypted_password, key, nonce)
        
        pyperclip.copy(decrypted_password)
        print('Your password was copied to your clipboard!')
    
    else:
        length =int(input('Input a number between 1-90 that will be the length of your password \n'))
        upper_case_enabled = input('Would you like your password to be composed of uppercased letter? Yes or No?\n')
        digits_enabled = input('Would you like your password to be composed of digits? Yes or No?\n')
        special_char_enabled = input('Would you like your password to be composed of special characters? Yes or No?\n')
        
        random_password = password_generator.random_password_generator(length, upper_case_enabled.lower() == 'yes',
                                                                              digits_enabled.lower() == 'yes',
                                                                              special_char_enabled.lower() == 'yes')
        print(f'Your password is {random_password}')
        clipboard = input('Would like it to be copied to your clipboar? Yes or No?\n')

        if clipboard.lower() == 'yes':
            pyperclip.copy(random_password)
            print('Your password was copied to your clipboard!')

if __name__ == '__main__':
    main()
