import tkinter as tk

window = tk.Tk()               #设置窗口
window.title('my window')      #窗口标题
window.geometry('200x300')     #窗口长宽

#画布控件；显示图形元素如线条或文本
canvas = tk.Canvas(window,bg='blue',height=200,width=200)           #定义一个200x200底色为蓝色的画布
image_file = tk.PhotoImage(file='timg.gif')                         #读取图片

image = canvas.create_image(10,10,anchor='nw',image=image_file)
#在画布中坐标位置为（10，10）的位置插入GIF插入图片，
#其中参数anchor表示坐标表示图片的哪个位置（上北下南左西右东）

x0,y0,x1,y1 = 50,50,80,80
line = canvas.create_line(x0,y0,x1,y1)
#以(x0,y0)为起点(x1,y1)为终点画一条线

oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
#在矩形框(x0,y0,x1,y1)中画一个内接圆

rect1 = canvas.create_rectangle(x0,y0,x1,y1)
#矩形框(x0,y0,x1,y1)

arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180)
#以坐标(x0+30,y0+30),(x1+30,y1+30)为端点画0-180度的扇形

rect = canvas.create_rectangle(100,30,100+20,30+20)
#矩形框(100,30,100+20,30+20)
canvas.pack()

def moveit():
    canvas.move(rect,-2,0)
    #在画布中移动rect表示的矩形，
    #横坐标+2，纵坐标+0(向右移动2个单位，向下移动0个单位)

button = tk.Button(window,
                   text='move',
                   command=moveit).pack()

window.mainloop()    #窗口更新
