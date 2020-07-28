import tkinter as tk

window = tk.Tk()               #设置窗口
window.title('my window')      #窗口标题
window.geometry('500x500')     #窗口长宽

var = tk.StringVar()                     #字符串变量
# 标签控件；可以显示文本和位图
label = tk.Label(window,
                 textvariable = var,     #文字内容
                 bg = 'yellow',           #背景色
                 font = ('Arial', 12),   #字体样式及大小
                 width = 15,             #宽度
                 height = 2,             #高度
                 )
label.pack()


on_hit = True
def hit_me():
    global on_hit
    if on_hit:
        var.set('you hit me')         #设置文本变量的内容
        on_hit = False
    else:
        var.set('')
        on_hit = True

# 按钮
button = tk.Button(window,
                   text = 'hit me',    #按钮字体
                   width = 15,         #按钮宽度
                   height = 2,         #按钮高度
                   command = hit_me)   #点击按钮后执行的操作
button.pack()                          #pack（包装）几何位置



window.mainloop()    #窗口更新


