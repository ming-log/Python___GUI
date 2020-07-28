import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.iconbitmap("./qcc.ico")  # 修改图标
window.title('my window')
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title='Hi', message='hahahaha')
    #ask 确定 return 'ok'  #提示信息对话窗

    tk.messagebox.showwarning(title='Hi', message='nononono')
    #ask 确定  # return 'ok'  #提出警告对话窗

    tk.messagebox.showerror(title='Hi', message='No!! never')
    #ask 确定  # return 'ok'   #提出错误对话窗

    print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))
    #ask 是 or 否  # return 'yes' , 'no'   #询问选择对话窗

    print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))
    #ask 是 or 否    return True, False

    print(tk.messagebox.askretrycancel(title='Hi', message='hahahaha'))
    #ask 重试 or 取消   # return True, False

    print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))
    #ask 确定 or 取消   # return True, False

    print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))
    #ask 是 or 否 or 取消    # return, True, False, None

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()