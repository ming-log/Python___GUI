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

def print_selection(var):
    label.config(text='you have select '+var)     #修改label中的text参数的值

#范围控件；显示一个数值刻度，为输出限定范围的数字区间
#默认会有一个传出值
scale = tk.Scale(window,
                 label='try me',         #范围控件上方显示的文字
                 from_=0,                #范围最小值
                 to=11,                  #范围最大值
                 orient=tk.HORIZONTAL,   #控件显示的方向tk.HORIZONTAL表示水平方向    tk.VERTICAL表示竖直方向
                 length=300,             #控件显示的长度（单位：像素）
                 showvalue=0,            #是否显示数值 0:不显示    1:显示
                 tickinterval=2,         #标签值的间隔
                 resolution=0.01,        #精度  eg: 0.01表示2位小数
                 command=print_selection)#将值传给print_selection
scale.pack()                             #显示控件


window.mainloop()    #窗口更新


