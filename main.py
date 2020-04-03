from tkinter import *
import mapbase, ball, line
from math import cos, sin, radians

# 각도 비율 조정용 리스트 하나 작성. 길이 100 기준.
# 0,5,10,15....90도 까지
#0~37 인덱스 리스트. 0,1은 0도일때, 36,37은 90도일때.
angle=[]
for a in range(0, 95, 5):
    angle+=[round(100*cos(radians(a))), round(100*sin(radians(a)))]


# 윈도우설정

win1=Tk()
win1.title('공 쏘기 게임')
win1.geometry('700x400+100+100')
win1.resizable(False,False)

win2=Tk()
win2.title('설정')
win2.geometry('200x200+800+100')
win2.resizable(False,False)

#win2 라벨설치.

def g_set():
    global gravity
    gravity=int(gentry.get())
    text='중력 '+ str(gravity) + ', 바람 ' + str(wind)
    mainmap.write_text(text)
def w_set():
    global wind
    wind=int(wentry.get())
    text='중력 '+ str(gravity) + ', 바람 ' + str(wind)
    mainmap.write_text(text)
def x_set():
    target.set_pos(int(xentry.get()),target.y1)
    target.move()
def y_set():
    target.set_pos(target.x1,int(yentry.get()))
    target.move()

gentry=Entry(win2, width=10)
gentry.pack()
gbutton=Button(win2, text='중력설정', command=g_set)
gbutton.pack()
wentry=Entry(win2, width=10)
wentry.pack()
wbutton=Button(win2, text='바람설정', command=w_set)
wbutton.pack()

xentry=Entry(win2, width=10)
xentry.pack()
xbutton=Button(win2, text='목표x설정', command=x_set)
xbutton.pack()
yentry=Entry(win2, width=10)
yentry.pack()
ybutton=Button(win2, text='목표y설정', command=y_set)
ybutton.pack()




# 윈도우에 얹어주기, 시작세팅.

ball_r=10          #공 반지름
guide_length=3*ball_r
power_length=60
energy=0
target_r=20
target_x=650
target_y=200

gravity=1           #중력설정
wind=-0.2           #바람설정

mainmap=mapbase.Map(win1)
guide=line.Line(mainmap)
missile=ball.Ball(mainmap, r=ball_r)
power=line.Line(mainmap, x=50-(power_length/2), y=390)
target=ball.Ball(mainmap, color='brown', r=target_r, x=target_x, y=target_y)

guide.set_line(angle[0]*guide_length/100, -angle[1]*guide_length/100)
guide_level=0
text='중력 '+ str(gravity) + ', 바람 ' + str(wind)
mainmap.write_text(text)
power_flag=0


# 조작
def angle_up(n):
    global guide_level
    if guide_level!=36:
        guide_level+=2
        guide.set_line(angle[guide_level]*guide_length/100, -angle[guide_level+1]*guide_length/100)

def angle_down(n):
    global guide_level
    if guide_level!=0:
        guide_level-=2
        guide.set_line(angle[guide_level]*guide_length/100, -angle[guide_level+1]*guide_length/100)

def reset_missile(n):
    global power_flag
    power_flag=0
    missile.set_sp(0,0)
    missile.set_pos(50,350)

def zzzing(n):
    global energy, power_length, power_flag
    if power_flag==0:
        if energy<power_length:
            energy+=4
        power.set_line(energy, 0)

def shoot(n):
    global energy, power_flag
    if power_flag==0:
        power.set_line(0,0)
        missile.set_sp(angle[guide_level]*energy/100, -angle[guide_level+1]*energy/100)
        energy=0
        power_flag=1

win1.bind('<Up>', angle_up)
win1.bind('<Down>', angle_down)
win1.bind('r', reset_missile)
win1.bind('<KeyPress-space>', zzzing)
win1.bind('<KeyRelease-space>', shoot)









# 실행
collision_flag=0
collision_n=0
def collision():
    global collision_flag, collision_n
    
    if collision_flag==0:
        collision_flag=missile.collision_check(target)
        if collision_flag==1:
            missile.set_sp(0, 0)
            mainmap.write_message('miss')
        elif collision_flag==2:
            missile.set_sp(0, 0)
            mainmap.write_message('명중')
    else:
        missile.set_sp(0, 0)
        collision_n+=1
        if collision_n==20:
            collision_n=0
            collision_flag=0
            reset_missile(1)


def time_flow():
    if (missile.x_sp!=0) or (missile.y_sp!=0):    #중력과 바람
        missile.set_sp(missile.x_sp+wind, missile.y_sp+gravity)
    collision()
    missile.move()    #미사일 움직임
    win1.after(16, time_flow)

time_flow()


win1.mainloop()



















