#  Source: C2Plabs.com
#       https://c2plabs.com/blog/2019/06/22/dc-motor-control-using-tb6612fng-driver-and-raspberry-pi-gpiozero-lib/
#
# Modified slightly for testing
# Changed GPIO pins and removed console input reading for switching motor direction

from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

# GPIO 6 is used for Generating Software PWM
# GPIO 13 & GPIO 19 are used for Motor control pins as per schematic


PWM_PIN_MOT1 = 19
IN1_PIN_MOT1 = 27
IN2_PIN_MOT1 = 17

# PWMOutputDevice takes  BCM_PIN number
# Active High
# intial value
# PWM Frequency
# and Pin_factory which can be ignored

pwm_pin_mot1 = PWMOutputDevice (PWM_PIN_MOT1,True, 0, 1200)

# DigitalOutputDevice take
# Pin Nuumber
# Active High
#Initial Value

cw_pin_mot1 = DigitalOutputDevice (IN1_PIN_MOT1, True, 0)

ccw_pin_mot1 = DigitalOutputDevice (IN2_PIN_MOT1, True, 0)


def RotateMotorCW():
        print ('Clockwise')
        pwm_pin_mot1.value = 0.5
        cw_pin_mot1.value = 1
        ccw_pin_mot1.value = 0


def RotateMotorCCW():
        print ('Counterclockwise')
        pwm_pin_mot1.value = 0.5
        cw_pin_mot1.value = 0
        ccw_pin_mot1.value = 1


def StopMotor():
        cw_pin_mot1.value = 0
        ccw_pin_mot1.value = 0
        pwm_pin_mot1.value = 0

try:
    while True:
            RotateMotorCW()
            sleep(4)
            RotateMotorCCW()
            sleep(4)
except KeyboardInterrupt:
        print ('Interrupted')

StopMotor()
