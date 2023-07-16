# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

import sensor, image, time, lcd
from machine import UART    #导入UART模块
from fpioa_manager import fm

fm.register(7, fm.fpioa.UART1_RX, force = True)      # 配置 7 脚为 UART2_RX 强制注册
fm.register(8, fm.fpioa.UART1_TX, force = True)      # 配置 8 脚为 UART2_TX 强制注册
uart_A = UART(UART.UART1, 115200, 8, 1, 0, timeout=100000, read_buf_len=4096)#数据位 8 停止位 1 校验位 0 超时时间 100000ms 缓冲区大小 4096

lcd.init(freq=15000000)
sensor.reset()                      # Reset and initialize the sensor. It will
                                    # run automatically, call sensor.run(0) to stop
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.

while(True):
    clock.tick()                    # Update the FPS clock.
    img = sensor.snapshot()         # Take a picture and return the image.
    lcd.display(img)                # Display on LCD
    uart_A.write("1") #将检测到的物体发送到串口
    print(uart_A.write("1"))              # Note: MaixPy's Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.
