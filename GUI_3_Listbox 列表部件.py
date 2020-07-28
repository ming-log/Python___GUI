import tkinter as tk

window = tk.Tk()               #设置窗口
window.title('my window')      #窗口标题
window.geometry('200x300')     #窗口长宽


var1 = tk.StringVar()                  #设置tk型字符串变量
#标签控件；可以显示文本和位图
label = tk.Label(window,
                 bg='yellow',            #设置背景色为黄色
                 width=4,                #宽度为4
                 textvariable=var1)      #文本设置为var1
label.pack()                             #将label放入窗口

def print_selection():
    value = listbox.get(listbox.curselection())              #获取用户输入
    var1.set(value)    #将var的值插入在t表示的文本控件的光标处

# 按钮
button1 = tk.Button(window,
                   text = 'print selection',    #按钮字体
                   width = 15,         #按钮宽度
                   height = 2,         #按钮高度
                   command = print_selection)   #点击按钮后执行的操作
button1.pack()                          #pack（包装）几何位置

var2 = tk.StringVar()                              #设置tk型字符串变量
var2.set((11,22,33,44))                            #赋值为(11,22,33,44)

#列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
#列表为var2=(11,22,33,44)
listbox = tk.Listbox(window, listvariable=var2)

list_items = [1,2,3,4]
for item in list_items:
    listbox.insert('end',item)                #循环在列表末尾插入list_items中的内容
listbox.insert(1,'first')                     #在列表第二行插入first
listbox.insert(2,'second')                    #在列表第三行插入second
listbox.delete(2)                             #删除列表第三行内容
listbox.pack()                                #打印列表框

window.mainloop()    #窗口更新


