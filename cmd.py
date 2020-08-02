import os, editor, os.path, shutil, games
print('===Help===\n\nWARNING SPACES ARE NOT SUPPORTED\n\nhelp - Prints this message\necho - Prints everything after \'echo\'\nmakedir - Make a directory with the name of everything after the \'makedir\'\ndeldir - Like \'makdir\' Just deletes the directory\nchangedir - Changes the directory\nupdir - Goes up a directory\nmakefile - Makes a file with the name of everything after the \'makefile\'\ndelfile - The same thing as \'makefile\' but deletes the file\neditfile - Opens a tkinter editor for the filename given\nrun - Runs the given python file\nlist - Lists all files and folders in the current directory\ngame - Runs game.py\nquit - Quits the OS\n')
def lang(username, cdir):
    command = str(input(cdir + '/ ')).split(' ')
    command.append('')
    if command[0] != 'echo':
       command = ' '.join(command).replace('../', '').replace('/', '').split(' ')
    command.append(' ')
    if command[0] == 'help':
        if command[1] == '':
          print('===Help===\n\nWARNING SPACES ARE NOT SUPPORTED\n\nhelp - Prints this message\necho - Prints everything after \'echo\'\nmakedir mkdir - Make a directory with the name of everything after the \'makedir\'\ndeldir - Like \'makdir\' Just deletes the directory\nchangedir cd - Changes the directory\nupdir - Goes up a directory\nmakefile touch - Makes a file with the name of everything after the \'makefile\'\ndelfile - The same thing as \'makefile\' but deletes the file\neditfile vim vi - Opens a tkinter editor for the filename given\nrun - Runs the given python file\nlist - Lists all files and folders in the current directory\ngame - Runs game.py\nquit - Quits the OS\n')
    elif command[0] == 'echo':
        print(' '.join(command[1:-1]))
    elif command[0] == 'makedir' or command[0] == 'mkdir':
        os.mkdir(cdir + '/' + command[1])
    elif command[0] == 'deldir':
        if input('Are you sure you want to delete this folder? [Y/n]: ') in ['y', 'Y']:
            shutil.rmtree(cdir + '/' + command[1])
        else:
          print('', end='')
    elif command[0] == 'changedir' or command[0] == 'cd':
        if os.path.isdir(cdir + '/' + command[1]):
            cdir = cdir + '/' + command[1]
        else:
            print('Folder does not yet exist.')
    elif command[0] == 'updir':
        cdir = cdir.split('/')
        cdir.pop()
        cdir = '/'.join(cdir)
    elif command[0] == 'makefile' or command[0] == 'touch':
        open(cdir + '/' + command[1], 'x')
    elif command[0] == 'delfile':
        if input('Are you sure you want to delete this folder? [Y/n]: ') in ['y', 'Y']:
            os.remove(cdir + '/' + command[1])
        else:
          print('', end='')
    elif command[0] == 'editfile' or command[0] == 'vim' or command[0] == 'vi':
        editor.editor(cdir + '/' + command[1])
    elif command[0] == 'run':
        os.system('python3 ' + cdir + command[1])
    elif command[0] == 'list':
        print(' '.join(os.listdir(cdir)))
    elif command[0] == 'game':
        games.games()
    elif command[0] == 'quit':
        quit()
    else:
        print('command does not exist yet')
    print('')
    lang(username, cdir)