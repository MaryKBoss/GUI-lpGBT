import serial
from TDC_config_low_level_function import *
from serial_config_tdc import *
from TDCreg import *
# if used in linux, uncomment the initialization below and choose the right device
# ser = serial.Serial( port='/dev/ttyUSB0', baudrate = 115200, bytesize = serial.EIGHTBITS,parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.1)

# if used in windows, uncomment the initialization below and choose the right device
ser = serial.Serial(port='/dev/ttyUSB1', baudrate = 115200, bytesize = serial.EIGHTBITS,parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.1)



write=(lpgbt_config_single_write(ser,117,108,64))
# readback=(lpgbt_config_read(ser,117,1,1))
# readback_list = []
# for i in range (len(readback)):
#     readback_list.append(format(write[i],'x').zfill(2))
# print(readback_list)
# config_reg_content = ser.read(20)
# print(config_reg_content)
# len(config_reg_content)
# TDC0 = TDCreg(ser)
# TDC0.DAQ_init()
# TDC0.update_periodic_hit()
# # #
# verificate_pass_TD_CODE = verificate_ID_CODE(ser)