import AES_Module, DES_Module, TripleDES_Module, tabulate, os, psutil


def AESEncryptionStats(password):

    key, nonce, encrypted_password, AES_encryption_time = AES_Module.encrypt(password)

    TripleDES_encryption_time = TripleDES_Module.encrypt(password)[-1]
    TripleDES_efficiency = (AES_encryption_time * 100) / TripleDES_encryption_time

    DES_encryption_time = DES_Module.encrypt(password)[-1]
    DES_efficiency = (AES_encryption_time * 100) / DES_encryption_time

    headers = ['Method', 'Time', 'Efficiency']
    stats_list = [  ['AES', str(round(AES_encryption_time, 6)) + 'ms', '100.00%'],
                    ['3DES', str(round(TripleDES_encryption_time, 6)) + 'ms', str(round(TripleDES_efficiency, 2)) + '%'],
                    ['DES', str(round(DES_encryption_time, 6)) + 'ms', str(round(DES_efficiency, 2)) + '%']  ]
   
    print('\n Stats:\n') 
    print('Your machine has ' + str(round(os.cpu_count()/2)) +' Cores and ' +str((round(psutil.virtual_memory().total / (1024 **3))))+ ' GB of RAM', end='\n')
    print(tabulate.tabulate(stats_list, headers, tablefmt = 'fancy_grid'))

    return key, nonce, encrypted_password


def TripleDESEncryptionStats(password):

    key, nonce, encrypted_password, TripleDES_encryption_time = TripleDES_Module.encrypt(password)

    AES_encryption_time = AES_Module.encrypt(password)[-1]
    AES_efficiency = (TripleDES_encryption_time * 100) / AES_encryption_time

    DES_encryption_time = DES_Module.encrypt(password)[-1]
    DES_efficiency = (TripleDES_encryption_time * 100) / DES_encryption_time

    headers =['Method', 'Time', 'Efficiency']
    stats_list = [  ['3DES', str(round(TripleDES_encryption_time, 6)) + 'ms', '100.00%'],
                    ['AES' , str(round(AES_encryption_time, 6)) + 'ms', str(round(AES_efficiency, 2)) + '%'],
                    ['DES', str(round(DES_encryption_time, 6)) + 'ms', str(round(DES_efficiency, 2)) + '%']   ]
    
    print('\nStats: \n')
    print('Your machine has ' + str(round(os.cpu_count()/2)) +' Cores and ' +str((round(psutil.virtual_memory().total / (1024 **3))))+ ' GB of RAM', end='\n')
    print(tabulate.tabulate(stats_list, headers, tablefmt = 'fancy_grid'))

    return key, nonce, encrypted_password

def DESEncryptionStats(password):

    key, nonce, encrypted_password, DES_encryption_time = DES_Module.encrypt(password)

    AES_encryption_time = AES_Module.encrypt(password)[-1]
    AES_efficiency = (DES_encryption_time * 100) / AES_encryption_time

    TripleDES_encryption_time = TripleDES_Module.encrypt(password)[-1]
    TripleDES_efficiency = (DES_encryption_time * 100) / TripleDES_encryption_time

    headers = ['Method', 'Time', 'Efficiency']
    stats_list = [  ['DES', str(round(DES_encryption_time, 6)) + 'ms', '100%'],
                    ['AES' , str(round(AES_encryption_time, 6)) + 'ms', str(round(AES_efficiency, 2)) + '%'],
                    ['3DES', str(round(TripleDES_encryption_time, 6)) + 'ms', str(round(TripleDES_efficiency, 2)) + '%']    ]
    
    print('\nStats: \n')
    print('Your machine has ' + str(round(os.cpu_count()/2)) +' Cores and ' +str((round(psutil.virtual_memory().total / (1024 **3))))+ ' GB of RAM', end='\n')
    print(tabulate.tabulate(stats_list, headers, tablefmt = 'fancy_grid'))

    return key, nonce, encrypted_password

def AESDecryptionStats(encrypted_password, key, nonce):

    decrypted_password, AES_decryption_time = AES_Module.decrypt(encrypted_password, key, nonce)
    
    TripleDES_decryption_time = TripleDES_Module.decrypt(encrypted_password, key, nonce)[-1]
    TripleDES_efficiency = (AES_decryption_time * 100) / TripleDES_decryption_time

    DES_decryption_time = DES_Module.decrypt(encrypted_password, key[:8], nonce)[-1]
    DES_efficiency = (AES_decryption_time * 100) / DES_decryption_time

    headers =['Method', 'Time', 'Efficiency']
    stats_list = [  ['AES', str(round(AES_decryption_time, 6)) + 'ms', '100.00%'],
                    ['3DES', str(round(TripleDES_decryption_time, 6)) + 'ms', str(round(TripleDES_efficiency, 2)) + '%'],
                    ['DES', str(round(DES_decryption_time, 6)) + 'ms', str(round(DES_efficiency, 2)) + '%']    ]

    print('\nStats: \n')
    print('Your machine has ' + str(round(os.cpu_count()/2)) +' Cores and ' +str((round(psutil.virtual_memory().total / (1024 **3))))+ ' GB of RAM', end='\n')
    print(tabulate.tabulate(stats_list, headers, tablefmt = 'fancy_grid'))

    return decrypted_password.decode('ISO-8859-1')

def TripleDESDecryptionStats(encrypted_password, key, nonce):

    decrypted_password, TripleDES_decryption_time = TripleDES_Module.decrypt(encrypted_password, key, nonce)

    AES_decryption_time = AES_Module.decrypt(encrypted_password, key[:16], nonce)[-1]
    AES_efficiency = (TripleDES_decryption_time * 100) / AES_decryption_time

    DES_decryption_time = DES_Module.decrypt(encrypted_password, key[:8], nonce)[-1]
    DES_efficiency = (TripleDES_decryption_time * 100) / DES_decryption_time

    headers =['Method', 'Time', 'Efficiency']
    stats_list = [  ['3DES', str(round(TripleDES_decryption_time, 6)) + 'ms', '100.00%'],
                    ['AES', str(round(AES_decryption_time, 6)) + 'ms', str(round(AES_efficiency, 2)) + '%'],
                    ['DES', str(round(DES_decryption_time, 6)) + 'ms', str(round(DES_efficiency, 2)) + '%']    ] 

    print('\nStats: \n')
    print('Your machine has ' + str(round(os.cpu_count()/2)) +' Cores and ' +str((round(psutil.virtual_memory().total / (1024 **3))))+ ' GB of RAM', end='\n')
    print(tabulate.tabulate(stats_list, headers, tablefmt = 'fancy_grid'))

    return decrypted_password.decode('ISO-8859-1')

def DESDecryptionStats(encrypted_password, key, nonce):

    decrypted_password, DES_decryption_time = DES_Module.decrypt(encrypted_password, key, nonce)

    AES_decryption_time = AES_Module.decrypt(encrypted_password, 2*key, nonce)[-1]
    AES_efficiency = (DES_decryption_time *100) / AES_decryption_time

    headers = ['Method', 'Time', 'Efficiency']
    stats_list = [  ['DES', str(round(DES_decryption_time, 6)) + 'ms', '100%'],
                    ['AES', str(round(AES_decryption_time, 6)) + 'ms', str(round(AES_efficiency, 2)) + '%'],
                    ['3DES', 'NaN', 'NaN']  ]

    print('\nStats: \n')
    print('Your machine has ' + str(round(os.cpu_count()/2)) +' Cores and ' +str((round(psutil.virtual_memory().total / (1024 **3))))+ ' GB of RAM', end='\n')
    print(tabulate.tabulate(stats_list, headers, tablefmt = 'fancy_grid'))

    return decrypted_password.decode('ISO-8859-1')


