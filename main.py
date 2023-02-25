from tkinter import *

root = Tk()

root.configure(bg="blue", height=800,width=600)

#Canvases
exp_canvas = Canvas(root, width=450,height=350, bg='#3B95CC',bd=0, highlightthickness=0)
exp_canvas.pack()
inc_canvas = Canvas(root, width=450,height=350, bg='#3B95CC',bd=0, highlightthickness=0)
inc_canvas.pack()


#Labels
expense = Label(root,text='Expense',bg='black',fg='white')
expAmt = Label(root,text='Amount',bg='black',fg='white')
expWk = Label(root,text='Weekly',bg='black',fg='white')
expDly = Label(root,text='Daily',bg='black',fg='white')
expMnt = Label(root,text='Monthly',bg='black',fg='white')
expYr = Label(root,text='Yearly',bg='black',fg='white')

esW = exp_canvas.create_window(65,30,window=expense)
esA = exp_canvas.create_window(122,30,window=expAmt)
esWk = exp_canvas.create_window(175,30,window=expWk)
esD = exp_canvas.create_window(220,30,window=expDly)
esM = exp_canvas.create_window(270,30,window=expMnt)
esY = exp_canvas.create_window(320,30,window=expYr)


income = Label(root,text='Income',bg='black',fg='white')
incAmt = Label(root,text='Amount',bg='black',fg='white')
incWk = Label(root,text='Weekly',bg='black',fg='white')
incDly = Label(root,text='Daily',bg='black',fg='white')
incMnt = Label(root,text='Monthly',bg='black',fg='white')
incYr = Label(root,text='Yearly',bg='black',fg='white')

incW = inc_canvas.create_window(65,30,window=income)
incA = inc_canvas.create_window(122,30,window=incAmt)
incWk = inc_canvas.create_window(175,30,window=incWk)
incD = inc_canvas.create_window(220,30,window=incDly)
incM = inc_canvas.create_window(270,30,window=incMnt)
incY = inc_canvas.create_window(320,30,window=incYr)


#Inputs
expenseEnt = Entry(root)
expAmtEnt = Entry(root)
expWkEnt = Entry(root)
expDlyEnt = Entry(root)
expMntEnt = Entry(root)
expYrEnt = Entry(root)

esWEnt = exp_canvas.create_window(105,70,window=expenseEnt)
esAEnt = exp_canvas.create_window(162,70,window=expAmtEnt)
esWkEnt = exp_canvas.create_window(215,70,window=expWkEnt)
esDEnt = exp_canvas.create_window(260,70,window=expDlyEnt)
esMEnt = exp_canvas.create_window(310,70,window=expMntEnt)
esYEnt = exp_canvas.create_window(360,70,window=expYrEnt)

incomEnt = Entry(root)
incAmtEnt = Entry(root)
incWkEnt = Entry(root)
incDlyEnt = Entry(root)
incMntEnt = Entry(root)
incYrEnt = Entry(root)

incWEnt = inc_canvas.create_window(105,70,window=incomEnt)
incAEnt = inc_canvas.create_window(162,70,window=incAmtEnt)
incWkEnt = inc_canvas.create_window(215,70,window=incWkEnt)
incDEnt = inc_canvas.create_window(260,70,window=incDlyEnt)
incMEnt = inc_canvas.create_window(310,70,window=incMntEnt)
incYEnt = inc_canvas.create_window(360,70,window=incYrEnt)


#Buttons

root.mainloop()