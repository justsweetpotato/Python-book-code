import zipfile

zFile = zipfile.ZipFile('evil.zip')
passFile = open('dictionary.txt')
for line in passFile.readlines():
    password = line.strip('\n')
    # print('Try password: ' + password + '.', end="\n")
    try:
        zFile.extractall(pwd=password.encode())
        print('[+] Password = ' + password + '\n')
        zFile.close()
        exit(0)
    except Exception as e:
        pass
