from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_TUPLE = ("Courier", 35,"bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_num  = None

window = Tk()

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer_num)
    canvas.itemconfig(timer, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def pomodoro():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    
    timer_countdown(work_sec)
    if(reps%8 == 0):
        timer_label.config(text= "Long Break", fg=RED)
        timer_countdown(long_break_secs)
    elif(reps%2 == 0):
        timer_label.config(text= "Short Break", fg=RED)
        timer_countdown(short_break_sec)
    else:
        timer_label.config(text= "Work", fg=GREEN)
        timer_countdown(work_sec)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

#Recursively calling window.after every second and passing in returned value to timer_countdown
def timer_countdown(count):
    
    mins = math.floor(count / 60)
    secs = count % 60
    print(mins)
    print(secs)
    
    if (secs < 10):
        secs = f'0{secs}'
    
    if count >= 0:
        canvas.itemconfig(timer, text=f"{mins}:{secs}")
        window.after(1000, timer_countdown, count-1)
    else:
        pomodoro()
        mark=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+= "✔"
        check_marks.config(text="marks")

# ---------------------------- UI SETUP ------------------------------- #

window.title(string="Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

#Labels
timer_label =Label(text="Timer", bg=YELLOW, font=FONT_TUPLE, highlightthickness=0, fg=GREEN)
timer_label.grid(row=0, column=1)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

#Buttons

start_button = Button(text="Start", command=pomodoro, bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW)
reset_button.grid(row=3, column=2)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer = canvas.create_text(100,130, text="25:00", fill="white", font=FONT_TUPLE)
canvas.grid(row=1, column=1)







window.mainloop()