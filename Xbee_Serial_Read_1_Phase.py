#----------Phase 1 ------------
#MAC 0013A20041893BCB
import serial
ser = serial.Serial('COM6',115200)
read_byte = ser.read()
while read_byte is not None:
    read_byte = ser.read()
    print ('%x' % ord(read_byte))
    
