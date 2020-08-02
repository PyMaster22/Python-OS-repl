import os, editor, os.path, shutil
print('===Help===\n\nWARNING SPACES ARE NOT SUPPORTED\n\nhelp - Prints this message\necho - Prints everything after \'echo\'\nmakedir - Make a directory with the name of everything after the \'makedir\'\ndeldir - Like \'makdir\' Just deletes the directory\nchangedir - Changes the directory\nupdir - Goes up a directory\nmakefile - Makes a file with the name of everything after the \'makefile\'\ndelfile - The same thing as \'makefile\' but deletes the file\neditfile - Opens a tkinter editor for the filename given\nrun - Runs the given python file\nlist - Lists all files and folders in the current directory\nquit - Quits the OS\n')
def lang(username, cdir):
    command = input(cdir + '/ ').split(' ')
    if type(command) is str:
      tmp = command
      command = []
      command.append(tmp)
    if command[0] != 'echo':
       command = ' '.join(command).replace('../', '').replace('/', '').split(' ')
    command.append('')
    if command[0] == 'help':
        if command[1] == '':
          print('===Help===\n\nWARNING SPACES ARE NOT SUPPORTED\n\nhelp - Prints this message\necho - Prints everything after \'echo\'\nmakedir - Make a directory with the name of everything after the \'makedir\'\ndeldir - Like \'makdir\' Just deletes the directory\nchangedir - Changes the directory\nupdir - Goes up a directory\nmakefile - Makes a file with the name of everything after the \'makefile\'\ndelfile - The same thing as \'makefile\' but deletes the file\neditfile - Opens a tkinter editor for the filename given\nrun - Runs the given python file\nlist - Lists all files and folders in the current directory\nquit - Quits the OS\n')
    elif command[0] == 'echo':
        print(' '.join(command[1:-1]))
    elif command[0] == 'makedir':
        os.mkdir(cdir + '/' + command[1])
    elif command[0] == 'deldir':
        if input('Are you sure you want to delete this folder? [Y/n]: ') in ['y', 'Y']:
            shutil.rmtree(cdir + '/' + command[1])
        else:
          print('', end='')
    elif command[0] == 'changedir':
        if os.path.isdir(cdir + '/' + command[1]):
            cdir = cdir + '/' + command[1]
        else:
            print('Folder does not yet exist.')
    elif command[0] == 'updir':
        cdir = cdir.split('/')[0:-2]
    elif command[0] == 'makefile':
        open(cdir + '/' + command[1], 'x')
    elif command[0] == 'delfile':
        if input('Are you sure you want to delete this folder? [Y/n]: ') in ['y', 'Y']:
            os.remove(cdir + '/' + command[1])
        else:
          print('', end='')
    elif command[0] == 'editfile':
        editor.editor(cdir + '/' + command[1])
    elif command[0] == 'run':
        execfile(command[1])
    elif command[0] == 'list':
        print(' '.join(os.listdir(cdir)))
    elif command[0] == 'quit':
        quit()
    else:
        print('Command does not exist yet')
    print('')
    lang(username, cdir)