# 导入所有必要的库
from tkinter import *

# 定义Tkinter实例
global score
try:
    with open("high_score.txt") as f:
        score=f.read()
except:
    score=0
win= Tk()
txt=StringVar()
txt.set("0")
def click():
    txt.set(str(int(txt.get())+1))
# 使用PhotoImage函数导入图像
click_btn= PhotoImage(file='a.png')

# 创建一个用于按钮事件的标签
label2= Label(win,font=(None,20),text="最高分数:"+score).pack()
label1= Label(win,font=(None,20),textvariable=txt).pack()

# 创建一个虚拟按钮并传递图像
button= Button(win, image=click_btn,command=click,
borderwidth=0)
button.pack()
win.mainloop()
with open("high_score.txt",'w') as f:
    if score < txt.get():
        f.write(txt.get())
    
