import os, editor, shutil, games, hashlib
help_text = r"""===Help===

WARNING SPACES ARE NOT SUPPORTED

help - Prints this message
echo - Prints everything after 'echo'
makedir - Make a directory with the name of everything after the 'makedir'
deldir - Like 'makdir' Just deletes the directory
changedir - Changes the directory
updir - Goes up a directory
makefile - Makes a file with the name of everything after the 'makefile'
delfile - The same thing as 'makefile' but deletes the file
editfile - Opens a tkinter editor for the filename given
pyrun - Runs the given python file
list - Lists all files and folders in the current directory
game - Runs game.py
hash - For more help type 'help hash'
cat - Ecoes back the given files contents
quit - Quits the OS
"""
print(help_text)
def lang(username, cdir):
    while True:
        command = str(input(cdir + '/ ')).split(' ')
        command.append('')
        if command[0] != 'echo':
           command = ' '.join(command).replace('../', '').replace('/', '').split(' ')
        command.append(' ')
        if command[0] == 'help':
            if command[1] == '': print(help_text)
            elif command[1] == 'hash': print('===Hash===\n\nhash takes two arguments. The algorithm and the data.\nFor explample if I want to hash \'My dog goes Bork\' in sha512 then I type\'hash sha512 My dog goes Bork\'.\nThe supported algoritms are MD5, SHA1, SHA224, SHA256, and SHA512.')
        elif command[0] == 'echo': print(' '.join(command[1:-1]))
        elif command[0] == 'makedir' or command[0] == 'mkdir': os.mkdir(cdir + '/' + command[1])
        elif command[0] == 'deldir':
            if input('Are you sure you want to delete this folder? [Y/n]: ') in ['y', 'Y']: shutil.rmtree(cdir + '/' + command[1])
            else: print('', end='')
        elif command[0] == 'changedir' or command[0] == 'cd':
            if os.path.isdir(cdir + '/' + command[1]): cdir = cdir + '/' + command[1]
            else: print('Folder does not yet exist.')
        elif command[0] == 'updir':
            cdir = cdir.split('/')
            cdir.pop()
            cdir = '/'.join(cdir)
        elif command[0] == 'makefile' or command[0] == 'touch': open(cdir + '/' + command[1], 'x')
        elif command[0] == 'delfile':
            if input('Are you sure you want to delete this folder? [Y/n]: ') in ['y', 'Y']: os.remove(cdir + '/' + command[1])
            else: print('', end='')
        elif command[0] == 'editfile' or command[0] == 'vim' or command[0] == 'vi': editor.editor(cdir + '/' + command[1])
        elif command[0] == 'pyrun': os.system('python3 ' + cdir + command[1])
        elif command[0] == 'list': print(' '.join(os.listdir(cdir)))
        elif command[0] == 'game': games.games()
        elif command[0] == 'hash':
            if command[1] == 'md5': print(hashlib.md5(' '.join(command[2:-1]).encode('utf-8')).hexdigest())
            elif command[1] == 'sha1': print(hashlib.sha1(' '.join(command[2:-1]).encode('utf-8')).hexdigest())
            elif command[1] == 'sha224': print(hashlib.sha224(' '.join(command[2:-1]).encode('utf-8')).hexdigest())
            elif command[1] == 'sha256': print(hashlib.sha256(' '.join(command[2:-1]).encode('utf-8')).hexdigest())
            elif command[1] == 'sha512': print(hashlib.sha512(' '.join(command[2:-1]).encode('utf-8')).hexdigest())
        elif command[0] == 'cat': print(open(cdir + '/' + command[1]).read(), end='')
        elif command[0] == 'quit': quit()
        else: print('command does not exist yet')
        print('')