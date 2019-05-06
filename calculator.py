from tkinter import*
def btnclick(numbers):
	global operator
	operator=operator+str(numbers)
	text_input.set(operator)

#########################################################################################################
def btnclear():
	global operator
	operator=""
	text_input.set("")
#########################################################################################################

def btnequal():
	global operator
	sumup=str(eval(operator))
	text_input.set(sumup)
	operator=""
#########################################################################################################
cal=Tk()
cal.title("calculator")
operator=""
text_input=StringVar()
textDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd="40",insertwidth=4,bg="blue",justify='right')
textDisplay.grid(columnspan=4)
btn7=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="red",command=lambda:btnclick(7),font=('arial',20,'bold'),text="7")
btn7.grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="red",command=lambda:btnclick(8),font=('arial',20,'bold'),text="8")
btn8.grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="red",command=lambda:btnclick(9),font=('arial',20,'bold'),text="9")
btn9.grid(row=1,column=2)
addition=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="red",command=lambda:btnclick("+"),font=('arial',20,'bold'),text="+")
addition.grid(row=1,column=3)
# rrr=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="red",command=lambda:btnclick("sqr()"),font=('arial',20,'bold'),text="^")
# rrr.grid(row=1,column=4)

#########################################################################################################
btn4=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="green",command=lambda:btnclick(4),font=('arial',20,'bold'),text="4")
btn4.grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="green",command=lambda:btnclick(5),font=('arial',20,'bold'),text="5")
btn5.grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="green",command=lambda:btnclick(6),font=('arial',20,'bold'),text="6")
btn6.grid(row=2,column=2)
subtract=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="green",command=lambda:btnclick("-"),font=('arial',20,'bold'),text="-")
subtract.grid(row=2,column=3)
#########################################################################################################

btn1=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="yellow",command=lambda:btnclick(1),font=('arial',20,'bold'),text="1")
btn1.grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="yellow",command=lambda:btnclick(2),font=('arial',20,'bold'),text="2")
btn2.grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="yellow",command=lambda:btnclick(3),font=('arial',20,'bold'),text="3")
btn3.grid(row=3,column=2)
multi=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="yellow",command=lambda:btnclick("*"),font=('arial',20,'bold'),text="*")
multi.grid(row=3,column=3)
##########################################################################################################
btn0=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:btnclick(0),font=('arial',20,'bold'),text="0")
btn0.grid(row=4,column=0)
btnC=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:btnclear(),font=('arial',20,'bold'),text="C")
btnC.grid(row=4,column=1)
btneq=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:btnequal(),font=('arial',20,'bold'),text="=")
btneq.grid(row=4,column=2)
div=Button(cal,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:btnclick("/"),font=('arial',20,'bold'),text="/")
div.grid(row=4,column=3)
##########################################################################################################
cal.mainloop()
##########################################################################################################