"""
Self Parking Car
@author: AakashM
"""

import RPi.GPIO as io
import time

xc = True

m1_f = 15  # m1 is Steering motor (right)
m1_r = 33  # (left)
m2_f = 35  # m2 is Driving motor
m2_r = 37
sl_t = 21  # sl means sonar_left
sl_e = 19
sb_t = 38  # sb means sonar-back
sb_e = 40

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

M1_f = io.PWM(m1_f, 100)
M1_r = io.PWM(m1_r, 100)
M2_f = io.PWM(m2_f, 100)
M2_r = io.PWM(m2_r, 100)


def forward():
    print("forward()")
    M1_f.ChangeDutyCycle(0)
    M1_r.ChangeDutyCycle(0)
    M2_f.ChangeDutyCycle(60)
    M2_r.ChangeDutyCycle(0)


def stop():
    # ~ global xc
    M1_f.ChangeDutyCycle(0)
    M1_r.ChangeDutyCycle(0)
    M2_f.ChangeDutyCycle(0)
    M2_r.ChangeDutyCycle(0)
    print("Stop")
    # ~ xc=False


def parkstop():
    print("parkstop()")
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
    dis = (diff * 34300) / 2  # calculation
    return dis


def park():
    print("park()")
    parked = False
    stop()
    time.sleep(0.5)
    while (parked == False):
        dis_back = distance(sb_t, sb_e)
        M1_r.ChangeDutyCycle(100)  # taking left turn
        M2_r.ChangeDutyCycle(80)
        if (dis_back < 5):
            parked = True  # Stopping at after approx. 5cm or less distance
    parkstop()


if __name__ == '__main__':
    c = 0
    initial_state = True
    M1_f.start(0)
    M1_r.start(0)
    M2_f.start(0)
    M2_r.start(0)
    dis_back = distance(sb_t, sb_e)
    time.sleep(0.2)
    dis_left_ini = distance(sl_t, sl_e)
    time.sleep(0.2)
    print("Distance init: %f" % dis_left_ini)
    while xc == True:
        forward()
        dis_left = distance(sl_t, sl_e)
        print("Distance: %f" % dis_left)

        if dis_left < dis_left_ini + 5 and dis_left > dis_left_ini - 5 and initial_state == True:  # setting distance limit at initial stage and first_check
            print("init state move")
            forward()
            time.sleep(0.5)

        elif dis_left > dis_left_ini + 3:  # going forward after first_check
            print("forward while big distance ")
            initial_state = False
            forward()
            time.sleep(0.5)

        elif dis_left < dis_left_ini + 5 and dis_left > dis_left_ini - 5 and initial_state == False:  # stopping and parking
            print("prepare for parking")
            forward()
            time.sleep(1.5)
            park()

        elif xc == False:
            print("else statement")
            break
        elif KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
        else:
            parkstop()
            xc = False
            print("No place to park...")
            break

