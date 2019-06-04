import zipfile

<<<<<<< HEAD
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
=======

# zFile = zipfile.ZipFile('evil.zip')
# passFile = open('dictionary.txt')
# for line in passFile.readlines():
#     password = line.strip('\n')
#     try:
#         zFile.extractall(pwd=password)
#         print '[+] Password = ' + password + '\n'
#         zFile.close()
#         exit(0)
#     except Exception as e:
#         pass


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        return


def main():
    zFile = zipfile.ZipFile('evil.zip')
    with open('dictionary.txt', 'rb') as f:
        for line in f.readlines():
            password = line.strip('\n')
            guess = extractFile(zFile, password)
            if guess:
                print '[+] Password = ' + password + '\n'
                zFile.close()
                exit(0)

    zFile.close()


if __name__ == '__main__':
    main()
>>>>>>> 18ae6e9410325983587f00f2d8fe745b4a1ace3b
