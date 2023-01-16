from tkinter import *
import tkinter.messagebox as msgbox
import datetime
import time
from threading import *  # 동시실행가능하게해줌
import random
import winsound as sd
import pygame




root = Tk()  #기본 오브젝트로 창을 하나 만듭니다. 메인 창으로 나타납니다.
root.title("운동루틴 프로그램")
root.geometry("700x500+500+200")  # 가로 *세로+ x좌표 + y좌표    640 480
root.resizable(False, False)  # x,y 값 변경 불가 (창 크기 변경 불가)

now = datetime.datetime.now()
now_day = (now.strftime('%Y-%m-%d'))

back = ["풀업", "랫풀다운", "시트디로우", "원암덤벨로우", "티바로우"]
chest = ["딥스", "클로스 그립 푸쉬업", "푸쉬업", "인클라인 푸쉬업", "디클라인 푸쉬업"]
leg = ["스쿼트", "런지"]
routine_exit = False
play = True



# 시작버튼
def start_btn():
    global routine_exit
    routine_exit = False
    if routine_exit == False:

        s = Thread(target=work)
        s.start()


#겁쟁이 버튼
def exit_btn():
    global routine_exit
    routine_exit = True
    pygame.mixer.music.stop()


   # 기본 오브젝트로 창을 하나 만듭니다. 메인 창으로 나타납니다.
    '''
    exit_root = Tk()
    exit_root.title("종료")
    exit_root.geometry("200x150+762+350")  # 가로 *세로+ x좌표 + y좌표    640 480
    exit_root.resizable(False, False)  # x,y 값 변경 불가 (창 크기 변경 불가)

    exit_label = Label(exit_root, text="도망가시겠습니까?", font=('bold',10))
    exit_label.place(x=45,y=30)

    exit_button1 = Button(exit_root, text="네", width=6, height=1, command = quit)
    exit_button2 = Button(exit_root, text="아니요", width=6, height=1, command = exit_root.)

    exit_button1.place(x=20,y=100)
    exit_button2.place(x=90,y=100)
    '''





#겁쟁이 버튼을 먼저 눌러버리면 routine_exit 값이 True가 되버려서 아무런 동작을 할 수 없음
# routine을 시작하려면 routine_exit가 False인 경우에만 실행 가능함






def routine(index, num):
    global main_text
    if routine_exit == False:

        main_time_title.config(text=index[num] + " 운동이 시작 예정입니다.")


        while True:
            btn_time = 10
            while btn_time >= 0:
                main_text = f"{btn_time}"
                time.sleep(1)
                main_time_num.config(text=main_text)
                btn_time = btn_time - 1
                if routine_exit == True:
                    main_time_num.config(text="종료 되었습니다.")
                    break
            if routine_exit == True:
                main_time_num.config(text="종료 되었습니다.")
                break
            sd.Beep(600, 1000)

            btn_time = 60
            main_time_title.config(text=index[num])
            while btn_time >= 0:
                main_text = f"{btn_time}"
                time.sleep(1)
                main_time_num.config(text=main_text)

                btn_time = btn_time - 1
                if routine_exit == True:
                    main_time_num.config(text="종료 되었습니다.")
                    break
            if routine_exit == True:
                main_time_num.config(text="종료 되었습니다.")
                break
            sd.Beep(600, 300)
            sd.Beep(600, 300)
            btn_time = 10
            main_time_title.config(text="종목 사이 쉬는시간 입니다.")
            while btn_time >= 0:
                main_text = f"{btn_time}"
                time.sleep(1)
                main_time_num.config(text=main_text)
                btn_time = btn_time - 1
                if routine_exit == True:
                    main_time_num.config(text="종료 되었습니다.")
                    break
            if routine_exit == True:
                main_time_num.config(text="종료 되었습니다.")
                break
            break


def work():
    global main_text

    if pysical_value.get() == 1:  # 등
        idx = 0
        while idx < 5:
            routine(back, 0)
            idx += 1
        idx = 0
        while idx < 5:
            routine(back, 1)
            idx += 1
        idx = 0
        while idx < 5:
            routine(back, 2)
            idx += 1

    elif pysical_value.get() == 2:   # 가슴

        random.shuffle(chest)
        idx = 0
        while idx < 5:
            routine(chest, 0)
            idx += 1
        idx = 0
        while idx < 5:
            routine(chest, 1)
            idx += 1
        idx = 0
        while idx < 5:
            routine(chest, 2)
            idx += 1
        idx = 0
        while idx < 5:
            routine(chest, 3)
            idx += 1
        idx = 0
        while idx < 5:
            routine(chest, 4)
            idx += 1

    elif pysical_value.get() == 3:    # 하체

        idx = 0
        user_set = int(input("몇 세트씩 할거임?: "))
        for i in range(0,user_set):
            while idx < 1:
                routine(leg, 0)
                idx += 1
            idx = 0

        while idx < 1:

            routine(leg, 1)
            idx += 1
    msgbox.showinfo("알림", "종료 되었습니다.")


#음악재생
def play_music():
    global play

    if play == False:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/wnsdu/Music/physical.mp3")
        pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()
    global play
    play =False


# 운동 종류
pysical_frame = Frame(root, relief="solid", bd=1)
pysical_frame_title = Label(pysical_frame, text="[운동 종류]")
pysical_frame.pack(side="top", pady=20)
pysical_frame_title.pack()
pysical_value = IntVar()   # int형으로 선언
pysical0 = Radiobutton(pysical_frame, text="등", value=1, variable=pysical_value)
pysical1 = Radiobutton(pysical_frame, text="가슴", value=2, variable=pysical_value)
pysical2 = Radiobutton(pysical_frame, text="하체", value=3, variable=pysical_value)
pysical0.pack(side="left")
pysical1.pack(side="left")
pysical2.pack(side="left")

# 운동 이름
main_time = Frame(root)
main_time_title = Label(main_time, font=("", 15, "bold"), text="운동시간")
main_time_num = Label(main_time, text="", font=("", 30))
main_time_title.pack(pady=3)
main_time_num.pack(pady=3)
main_time.pack(side="top")

# 실행버튼
button_frame = Frame(root)
button1 = Button(button_frame, text="실행", font=("", 15, "bold"), height=2, width=7, command=start_btn)
button_frame.pack(side="bottom", pady=3, padx=3, ipady=25)
button1.pack()

# 종료버튼
button_frame = Frame(root)
button1 = Button(button_frame, text="겁쟁이 버튼", font=("", 15, "bold"), height=2, width=8, command=exit_btn)
button_frame.pack(side="bottom", pady=3, padx=5)
button1.pack()

#음악플레이어버튼
button_frame =Frame(root)
button_music = Button(button_frame, text="재생", font=("", 15, "bold"), command = play_music)
button_frame.pack(side='left')
button_music.pack()

#d일시정지버튼
button_frame=Frame(root)
btn_pause = Button(button_frame, text="일시정지", font=("", 15, "bold"), command = pause_music)
button_frame.pack(side='left')
btn_pause.pack()

# my name
my_name_frame = Frame(root)
my_name_frame1 = Label(my_name_frame, text="만든이 : I_enable")
my_name_frame.place(relx=0.80, rely=0.93)
my_name_frame1.pack()

root.mainloop()
