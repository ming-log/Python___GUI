import tkinter as tk

window = tk.Tk()
window.geometry('1000x2000')

canvas = tk.Canvas(window, height=1500, width=5000)
canvas.grid(row=1, column=1)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

#Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织
#pack()    包装；
# tk.Label(window, text='1').pack(side='top') #上
# tk.Label(window, text='1').pack(side='bottom') #下
# tk.Label(window, text='1').pack(side='left')#左
# tk.Label(window, text='1').pack(side='right')#右


#grid()    网格
# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)
#以上的代码就是创建一个四行三列的表格，其实grid就是用表格的形式定位的。
#这里的参数 row为行，colum为列，padx就是单元格左右间距，pady就是单元格上下间距。


#place()   位置
# tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

window.mainloop()