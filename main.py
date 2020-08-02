import hashlib, os, time
if not os.path.exists('users/'): os.mkdir('users/')
if not os.path.exists('users/guest/'): os.mkdir('users/guest/')
if not os.path.exists('users/users.txt'): open('users/users.txt', 'w+').write('guest')
username = input('Username: ')
if username in open('users/users.txt', 'r').read().split('\n'):
    if username == 'guest':
        print('', end='')
    else:
        password = input('Password: ')
        for _ in range(0, 10):
            password = hashlib.sha512(password.encode('utf-8')).hexdigest()
            password = hashlib.sha256(password.encode('utf-8')).hexdigest() + hashlib.md5(password.encode('utf-8')).hexdigest()
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if password == open('users/' + username + '/password.txt', 'r').read():
            print('', end='')
        else:
            print('Wrong password.')
            time.sleep(2)
            quit()
else:
    register = input('Do you want to register? [Y/n]')
    if register == 'Y' or register == 'y':
        password = input('Password: ')
        for _ in range(0, 10):
            password = hashlib.sha512(password.encode('utf-8')).hexdigest()
            password = hashlib.sha256(password.encode('utf-8')).hexdigest() + hashlib.md5(password.encode('utf-8')).hexdigest()
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        os.mkdir('users/' + username)
        open('users/' + username + '/password.txt', 'w').write(password)
        tmp = open('users/users.txt', 'r').read()
        open('users/users.txt', 'w').write(tmp + '\n' + username)
    else:
        quit()
import cmd
cmd.lang(username, 'users/' + username)