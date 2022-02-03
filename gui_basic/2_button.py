from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480+300+300") # 크기 지정 + x 위치 + y 위치
# root.resizable(False, False) # x,y 창크기 변경 불가

btn1 = Button(root, text = "버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root,  width=10, height=3, text="버튼4444444444444")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()  # 창이 닫히지 않도록 해줌

