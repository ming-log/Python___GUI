import tkinter as tk

window = tk.Tk()               #设置窗口
window.title('my window')      #窗口标题
window.geometry('200x300')     #窗口长宽


#标签控件；可以显示文本和位图
label = tk.Label(window,
                 bg='yellow',            #设置背景色为黄色
                 width=30,               #宽度为30
                 text='')                #文本设置为空
label.pack()                             #将label放入窗口

def print_selection():
    if var1.get() == 1 and var2.get() == 0:
        label.config(text='I only love Python')
    elif var1.get() == 0 and var2.get() == 1:
        label.config(text='I only love C++')
    elif var1.get() == 0 and var2.get() == 0:
        label.config(text='I do not love either')
    else:
        label.config(text='I love both')

var1 = tk.IntVar()                            #设置整数型变量
#多选框控件；用于在程序中提供多项选择框
checkbutton1 = tk.Checkbutton(window,
                    text='Python',            #选项内容设置为Python
                    variable=var1,            #设置作用变量
                    onvalue=1,                #如果被选择则将var1赋值为1
                    offvalue=0,               #如果未被选择则将var1赋值为0
                    command=print_selection)  #作用于print_selection
checkbutton1.pack()

var2 = tk.IntVar()                            #设置整数型变量
#多选框控件；用于在程序中提供多项选择框
checkbutton2 = tk.Checkbutton(window,
                    text='C++',               #选项内容设置为C++
                    variable=var2,            #设置作用变量
                    onvalue=1,                #如果被选择则将var2赋值为1
                    offvalue=0,               #如果未被选择则将var2赋值为0
                    command=print_selection)  #作用于print_selection
checkbutton2.pack()

window.mainloop()    #窗口更新


