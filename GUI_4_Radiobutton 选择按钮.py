import tkinter as tk

window = tk.Tk()               #设置窗口
window.title('my window')      #窗口标题
window.geometry('200x300')     #窗口长宽


var = tk.StringVar()                  #设置tk型字符串变量
#标签控件；可以显示文本和位图
label = tk.Label(window,
                 bg='yellow',            #设置背景色为黄色
                 width=30,               #宽度为30
                 text='')                #文本设置为空
label.pack()                             #将label放入窗口

def print_selection():
    label.config(text='you have select '+var.get())     #修改label中的text参数的值

#插入单选按钮控件；显示一个单选的按钮状态
radiobutton1 = tk.Radiobutton(window,      #作用与window窗口
               text='Option A',            #按钮显示Option A
               variable=var,               #点击按钮后作用于变量var
               value='A',                  #将value值传给var
               command=print_selection)    #点击按钮后执行print_selection操作
radiobutton1.pack()                        #显示按钮

radiobutton2 = tk.Radiobutton(window,
               text='Option B',            #按钮显示Option B
               variable=var,               #点击按钮后作用于变量var
               value='B',                  #将value值传给var
               command=print_selection)    #点击按钮后执行print_selection操作
radiobutton2.pack()                        #显示按钮

radiobutton3 = tk.Radiobutton(window,
               text='Option C',            #按钮显示Option C
               variable=var,               #点击按钮后作用于变量var
               value='C',                  #将value值传给var
               command=print_selection)    #点击按钮后执行print_selection操作

radiobutton3.pack()                        #显示按钮

window.mainloop()    #窗口更新


