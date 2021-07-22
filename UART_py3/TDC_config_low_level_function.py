import time


def str_to_hex(s,interval):
    s_r = ''
    s = s.decode('latin_1')
    for x in range(0, len(s)):
        s_raw="{:0>2x}".format(ord(s[x]))
        s_r = s_r + interval + s_raw
    return s_r


def str_to_bin(s,interval):
    s_r = ''
    s = s.decode('latin_1')
    for x in range(0, len(s)):
        s_raw="{:0>8b}".format(ord(s[x]))
        s_r = s_r + interval + s_raw
    return s_r



def bin_to_hex_8bit(s):
    if len(s)  !=8 :
        print("Error the length of string is not 8")
        return ''
    hex_raw_str=hex(int(s,2))
    if len(hex_raw_str) == 3:
        return('0'+hex_raw_str[2])
    else:
        return(hex_raw_str[2:])

def bin_to_hex(s):
    if len(s) % 8 !=0 :
        print("Error the length of string is not 8N")
        return ''
    s_r = ''
    for x in range(0,len(s) // 8):
        s_r = s_r + chr(int(s[x*8:x*8+8],2))
    return s_r

def chk_len(value,length):
    if len(format(value,   'b'))>length:
        print("variable length incorrect!")
        return 1
    else: 
        return 0


def lpgbt_config_read(serial_port,lpgbt_addr,reg_addr,nb_read):
    if chk_len(lpgbt_addr,8) or chk_len(reg_addr,16) or chk_len(nb_read,8):
        return 1
    s0 = '\x00'
    s0 += chr(1*16+1)
    s0 += chr(2*16+int(format(lpgbt_addr,   'b').zfill( 8)[0 :4 ],2))
    s0 += chr(3*16+int(format(lpgbt_addr,   'b').zfill( 8)[4 :8 ],2))
    s0 += chr(4*16+int(format(reg_addr,     'b').zfill(16)[0 :4 ],2))
    s0 += chr(5*16+int(format(reg_addr,     'b').zfill(16)[4 :8 ],2))
    s0 += chr(6*16+int(format(reg_addr,     'b').zfill(16)[8 :12],2))
    s0 += chr(7*16+int(format(reg_addr,     'b').zfill(16)[12:16],2))
    s0 += chr(8*16+int(format(nb_read,      'b').zfill( 8)[0 :4 ],2))
    s0 += chr(9*16+int(format(nb_read,      'b').zfill( 8)[4 :8 ],2))
    s0 += '\x0f'
    serial_port.reset_input_buffer()
    serial_port.reset_output_buffer()

    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)

    readback = serial_port.read(nb_read+1000)
    print(readback)
    chk_readback = (lpgbt_addr*2+1)==readback[0] and readback[2]==1 and \
                readback[3]==nb_read and readback[4]==0 and \
                (readback[6]*256+readback[5])==reg_addr
    if not chk_readback:
        print("readback error!")
        return 1
    else:
        return readback[7:-1]

def lpgbt_config_single_write(serial_port,lpgbt_addr,reg_addr,value):
    if chk_len(lpgbt_addr,8) or chk_len(reg_addr,16) or chk_len(value,8):
        return 1
    s0 = '\x00'
    s0 += chr(1*16+2)
    s0 += chr(2*16+int(format(lpgbt_addr,   'b').zfill( 8)[0 :4 ],2))
    s0 += chr(3*16+int(format(lpgbt_addr,   'b').zfill( 8)[4 :8 ],2))
    s0 += chr(4*16+int(format(reg_addr,     'b').zfill(16)[0 :4 ],2))
    s0 += chr(5*16+int(format(reg_addr,     'b').zfill(16)[4 :8 ],2))
    s0 += chr(6*16+int(format(reg_addr,     'b').zfill(16)[8 :12],2))
    s0 += chr(7*16+int(format(reg_addr,     'b').zfill(16)[12:16],2))
    s0 += chr(8*16+int(format(value,      'b').zfill( 8)[0 :4 ],2))
    s0 += chr(9*16+int(format(value,      'b').zfill( 8)[4 :8 ],2))
    s0 += '\x0f'

    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)

    readback = serial_port.read(20)
    # print(readback)
    chk_readback = (lpgbt_addr*2)==readback[0] and readback[2]==1 and \
                readback[3]==1 and readback[4]==0 and \
                (readback[6]*256+readback[5])==reg_addr and \
                readback[7]==value
    if not chk_readback:
        print("readback error!")
    else:
        print("reg["+str(reg_addr)+"]="+str(value))
    return 0

def lpgbt_read_back(serial_port):
    return 1







def trst_0(serial_port):
    s0 = '\x00\x1f\x2f\x30\x44\x50\x60\x70\x80\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def trst_1(serial_port):
    s1 = '\x00\x1f\x2f\x30\x44\x50\x60\x70\x81\x0f'
    serial_port.write(s1.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def get_update_reg(reg_num, serial_port):
    content_str = '\x00'+'\x1f\x2f\x31'
    content_str = content_str+chr(4*16+reg_num)
    content_str = content_str+'\x50\x60\x70\x80'+'\x0f'
    serial_port.write(content_str.encode('latin_1'))
    config_reg_content = serial_port.read(20)
    serial_port.reset_input_buffer()
    return config_reg_content

def get_ePLLconfig_reg(serial_port):
    content_str = '\x00' + '\x1f\x2f\x31\x43\x50\x60\x70\x80'+'\x0f'
    serial_port.write(content_str.encode('latin_1'))
    config_reg_content = str_to_bin(serial_port.read(20),'')[32:59]
    serial_port.reset_input_buffer()
    ePLLconfig_reg = {}
    ePllCapA = config_reg_content[25:27]
    ePLLconfig_reg['ePllCapA'] = ePllCapA
    ePllIcpA = config_reg_content[21:25]
    ePLLconfig_reg['ePllIcpA'] = ePllIcpA
    ePllResA = config_reg_content[17:21]
    ePLLconfig_reg['ePllResA'] = ePllResA
    phase_clk320_2 = config_reg_content[13:17]
    ePLLconfig_reg['phase_clk320_2'] = phase_clk320_2
    phase_clk320_1 = config_reg_content[9:13]
    ePLLconfig_reg['phase_clk320_1'] = phase_clk320_1
    phase_clk320_0 = config_reg_content[5:9]
    ePLLconfig_reg['phase_clk320_0'] = phase_clk320_0
    phase_clk160 = config_reg_content[0:5]
    ePLLconfig_reg['phase_clk160'] = phase_clk160
    return ePLLconfig_reg




def tdc_master_reset_1(serial_port):
    s0 = '\x00\x1f\x2f\x30\x49\x50\x60\x70\x81\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1
