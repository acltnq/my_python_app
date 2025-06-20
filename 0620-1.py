import tkinter as tk

def ex1():
    window = tk.Tk()

    #建立一個Label，設定的寬高單位是文字大小，width=30表示寬度相當於30個字
    greeting = tk.Label(text="Hello, Tkinter",foreground="#FF0000",background="#FFAA33",width=30,height=10)

    greeting.pack()#加入視窗

    #建立Entry文字欄位，若要使用多行文字，請用Text
    entry1 = tk.Entry(width =30,font=("微軟正黑體",20))
    entry2 = tk.Entry(width =30,font=("微軟正黑體",20))
    
    entry1.pack()
    entry2.pack()
    
    #定義事件處理函數
    def onClick(event):
        text1 = int(entry1.get())
        text2 = int(entry2.get())
        print(f"(text1+text2)",(text1+text2))
        print("The button was clicked!")

    #建立Button按鈕
    button = tk.Button(text="Click me",background="#33FFAA",width=20,height=2)

    #<Button-1>表示按下滑鼠左鍵的事件
    #<Button-2>表示按下滑鼠中鍵的事件
    #<Button-3>表示按下滑鼠右鍵的事件
    #bind是一個繫結方法，用來設定監聽的事件和綁定的處理函數

    button.bind("<Button-1>",onClick)
    button.pack()

    #練習1:請建立兩個文字欄位，讓使用者可以輸入兩個數字
    #常使用者按下送出按鈕後，可以得到兩數字相加的結果
def ex2():
    window = tk.Tk()
    window.geometry("300x50")
    textView1 = tk.Label(text="身高",width=4,height=2,font=("微軟正黑體",20))
    textView1.pack(anchor="w")#n正上 w左
    entry1 = tk.Entry(width =15,font=("微軟正黑體",20))
    entry1.pack(anchor="w",padx=10,fill="x")
    textView2 = tk.Label(text="體重",width=4,height=2,font=("微軟正黑體",20))
    textView2.pack(anchor="w")#n正上 w左
    entry2 = tk.Entry(width =15,font=("微軟正黑體",20))
    entry2.pack(anchor="w",padx=10,fill="x")
    def onClick(event):
        h = float(entry1.get())/100
        w = float(entry2.get())
        bmi = w/(h**2)
        tvResult["text"] = bmi
    button = tk.Button(text="計算BMI",font=("微軟正黑體",20))
    button.bind("<Button-1>",onClick)
    button.pack(anchor="w",padx=10,pady=10,fill="x")
    
    tvResult = tk.Label(text="BMI為",height=2,font=("微軟正黑體",20))
    tvResult.pack(anchor="w",padx=10)#n正上 w左
    window.mainloop()
ex2()
#練習2:請在最下面放入一個Label，長按計算按鈕，顯示BMI值
