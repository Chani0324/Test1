from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+300") # 크기 지정 + x 위치 + y 위치
root.resizable(False, False) # x,y 창크기 변경 불가

listbox = Listbox(root, selectmode="single", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    #listbox.delete(END) # 맨 뒤 항목을 삭제

    # 갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 index, 끝 index)
    #print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인
    #print("선택된 항목 :", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()  # 창이 닫히지 않도록 해줌

