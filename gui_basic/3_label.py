from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+300") # 크기 지정 + x 위치 + y 위치
root.resizable(False, False) # x,y 창크기 변경 불가

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/image.png")
label2  = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 # 함수 내에서 label의 이미지 값을 바꾸기 위해서 전역 변수로 설정
    photo2 = PhotoImage(file="gui_basic/image2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()  # 창이 닫히지 않도록 해줌

