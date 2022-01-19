def save_information(key, nonce, password,filename):

    with open(filename, 'wb') as f:
        f.write(key+b'\n')
        f.write(nonce+b'\n')
        f.write(password)

def get_information(filename):
   
    try:
        with open(filename, 'rb') as f:
            key = f.readline().strip(b'\n')
            nonce = f.readline().strip(b'\n')
            password = f.readline()

        return key, nonce, password
    except FileNotFoundError:
        print('File not found! Make sure the file exists and that it is in the correct folder')
        exit()
