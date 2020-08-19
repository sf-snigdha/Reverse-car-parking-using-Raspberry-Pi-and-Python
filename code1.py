"""
Self Parking Car
@author: AakashM
"""

import RPi.GPIO as io
import time

xc = True

m1_f = 15  # m1 is steering motor (right)
m1_r = 33  # (left)
m2_f = 35  # m2 is Driving motor
m2_r = 37
sl_t = 21  # sl means sonar_left
sl_e = 19
sb_t = 38  # sb means sonar_back
sb_e = 40
reset = 7

io.setwarnings(False)

io.setmode(io.BOARD)

io.setup(m1_f, io.OUT)
io.setup(m1_r, io.OUT)
io.setup(m2_f, io.OUT)
io.setup(m2_r, io.OUT)
io.setup(sl_t, io.OUT)
io.setup(sb_t, io.OUT)
io.setup(sl_e, io.IN)
io.setup(sb_e, io.IN)
io.setup(reset, io.IN, pull_up_down=io.PUD_DOWN)

M1_f = io.PWM(m1_f, 100)
M1_r = io.PWM(m1_r, 100)
M2_f = io.PWM(m2_f, 100)
M2_r = io.PWM(m2_r, 100)


def forward():
    M1_f.ChangeDutyCycle(0)
    M1_r.ChangeDutyCycle(0)
    M2_f.ChangeDutyCycle(70)
    M2_r.ChangeDutyCycle(0)


def stop():
    M1_f.ChangeDutyCycle(0)
    M1_r.ChangeDutyCycle(0)
    M2_f.ChangeDutyCycle(0)
    M2_r.ChangeDutyCycle(0)
    print("Stop")


def parkstop():
    global xc
    M1_f.ChangeDutyCycle(0)
    M1_r.ChangeDutyCycle(0)
    M2_f.ChangeDutyCycle(0)
    M2_r.ChangeDutyCycle(0)
    print("Parked---- Stop")
    xc = False


def distance(trig, echo):
    io.output(trig, True)
    time.sleep(0.00001)
    io.output(trig, False)
    Starttime = time.time()
    Stoptime = time.time()
    while io.input(echo) == 0:
        Starttime = time.time()
    while io.input(echo) == 1:
        Stoptime = time.time()
    diff = Stoptime - Starttime
    dis = (diff * 34300) / 2
    return dis


def park():
    stop()
    time.sleep(0.5)
    M1_r.ChangeDutyCycle(100)
    M2_r.ChangeDutyCycle(100)
    t_end = time.time() + 4.3
    while time.time() < t_end:  # calculation on parking
        dis_back = distance(sb_t, sb_e)
        time.sleep(0.05)
    time.sleep(0.1)
    parkstop()


if __name__ == '__main__':
    c = 0
    M1_f.start(0)
    M1_r.start(0)
    M2_f.start(0)
    M2_r.start(0)
    dis_back = distance(sb_t, sb_e)
    time.sleep(0.1)
    dis_left_ini = distance(sl_t, sl_e)
    time.sleep(0.5)
    while xc == True:
        forward()
        dis_left = distance(sl_t, sl_e)
        dis_back = distance(sb_t, sb_e)
        time.sleep(0.5)
        while dis_left > dis_left_ini + 2:  # distance checking
            time.sleep(2)
            dis_back = distance(sb_t, sb_e)
            dis_left_2 = distance(sl_t, sl_e)
            if dis_left_2 > dis_left_ini + 3:  # parking after spot detecting
                print("Parking available..!!")
                park()
                while xc == True:
                    print("While True")
                    time.sleep(0.1)
                    if io.input(reset) == 1:  # reset button
                        c = 1
                        print("done")
                        break
            else:
                print("No place to park...")
                break
            if xc == False:
                break
            if KeyboardInterrupt:
                stop()


