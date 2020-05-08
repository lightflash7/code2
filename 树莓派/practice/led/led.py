import RPi.GPIO as GPIO
import time


# 选引脚编码类型
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)


#如果RPi.GPIO检测到引脚已被配置为默认（输入）以外的其他引脚，则在尝试配置脚本时会收到警告。要禁用这些警告
GPIO.setwarnings(False)


# 下面是led
# 选引脚
led = 11
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)


try:
    while True:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led, GPIO.LOW)
        time.sleep(0.5)
finally:
    print("Cleaning Up!")
    GPIO.cleanup()
