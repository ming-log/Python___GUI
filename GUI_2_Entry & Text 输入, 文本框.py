import tkinter as tk

window = tk.Tk()               #设置窗口
window.title('my window')      #窗口标题
window.geometry('200x300')     #窗口长宽

e=tk.Entry(window,show='*')    #输入控件；用于显示简单的文本内容
                               #其中*表示将显示的值全部改为*
e.pack()

t = tk.Text(window,height = 2)       #文本控件；用于显示多行文本
t.pack()


def insert_point():
    var = e.get()              #获取用户输入
    t.insert("insert", var)    #将var的值插入在t表示的文本控件的光标处

def insert_end():
    var = e.get()
    t.insert("end", var)       #将var的值插入在t表示的文本控件的末尾
    #t.insert(1.1, var)          #将var的值插入在t表示的文本控件第一行的第二列

# 按钮
button1 = tk.Button(window,
                   text = 'insert point',    #按钮字体
                   width = 15,         #按钮宽度
                   height = 2,         #按钮高度
                   command = insert_point)   #点击按钮后执行的操作
button1.pack()                          #pack（包装）几何位置

button2 = tk.Button(window,
                   text = 'insert end',    #按钮字体
                   width = 15,         #按钮宽度
                   height = 2,         #按钮高度
                   command = insert_end)   #点击按钮后执行的操作
button2.pack()



window.mainloop()    #窗口更新


