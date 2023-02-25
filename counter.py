import time

time = 0


def count():
    global timer 
    while True:
        timer += 1
        l.configure(text=str(timer))
        window.update()
        time.slipe(1)


window = Tk()
window.title('счетчик')
window.geometry('300x300+500+300')
 
l = Lable(window, text=0, font=('',40, 'bold'))
l.pack(pady=100)
count()