from tkinter import Tk,Frame,Button

def print_tree(widget,indent=0):
    """print hierarch"y of Tk widgets"""
    print("{:<{}} * {!r}".format('',indent * 4, widget))
    for child in widget.winfo_children():
        print_tree(child,indent+1)

root = Tk()
f = Frame(master=root)
f.pack()
tree_button = Button(f)
tree_button['text'] = 'Print Widget tree'
tree_button['command'] = lambda: print_tree(f)
tree_button.pack({'side':'left'})

quit_button = Button(f)
quit_button['text'] = 'Quit'
quit_button['command'] = f.quit
quit_button.pack({'side':'left'})
f.mainloop()
root.destroy()
