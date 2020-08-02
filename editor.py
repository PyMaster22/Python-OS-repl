import tkinter
def editor(filename):
    root = tkinter.Tk()

    root.title(filename)

    T = tkinter.Text(root, height=30, width=60)
    T.pack()
    T.insert(tkinter.END, open(filename, 'r').read())

    S = tkinter.Button(root, text="Save", command=lambda:open(filename, 'w').write(T.get('0.0', tkinter.END))).pack()

    E = tkinter.Button(root, text="Exit", command=lambda:root.destroy()).pack()