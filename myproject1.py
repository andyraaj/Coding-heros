from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('300x500')
root.resizable(0,0)
root.configure(background='white')

result_label=Label(root,text=0,bg='white',fg='black')
result_label.grid(row=0,column=0,pady=(50,24))
result_label.config(font=('verdana',30,'bold'))   

btn7 = Button(root,text='7',bg='#CD661D',fg='white',width=5,height=3)
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',16))

btn8 = Button(root,text='8',bg='#CD661D',fg='white',width=5,height=3)
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',16))

btn9 = Button(root,text='9',bg='#CD661D',fg='white',width=5,height=3)
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',16))

btn_add = Button(root,text='+',bg='#CD661D',fg='white',width=5,height=3)
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',16))

btn4 = Button(root,text='4',bg='#CD661D',fg='white',width=5,height=3)
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',16))

btn5 = Button(root,text='5',bg='#CD661D',fg='white',width=5,height=3)
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',16))

btn6 = Button(root,text='6',bg='#CD661D',fg='white',width=5,height=3)
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',16))

btn_sub = Button(root,text='-',bg='#CD661D',fg='white',width=5,height=3)
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',16))

btn1 = Button(root,text='1',bg='#CD661D',fg='white',width=5,height=3)
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',16))

btn2 = Button(root,text='2',bg='#CD661D',fg='white',width=5,height=3)
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',16))

btn3 = Button(root,text='3',bg='#CD661D',fg='white',width=5,height=3)
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',16))

btn_mul = Button(root,text='*',bg='#CD661D',fg='white',width=5,height=3)
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',16))

root.mainloop()