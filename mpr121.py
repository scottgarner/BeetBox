# Based on Arduino example by Jim Lindblom
# http://bildr.org/2011/05/mpr121_arduino/

import smbus
bus = smbus.SMBus(1)

# MPR121 Register Defines

MHD_R = 0x2B
NHD_R = 0x2C
NCL_R = 0x2D
FDL_R = 0x2E
MHD_F = 0x2F
NHD_F = 0x30
NCL_F = 0x31
FDL_F = 0x32
ELE0_T = 0x41
ELE0_R = 0x42
ELE1_T = 0x43
ELE1_R = 0x44
ELE2_T = 0x45
ELE2_R = 0x46
ELE3_T = 0x47
ELE3_R = 0x48
ELE4_T = 0x49
ELE4_R = 0x4A
ELE5_T = 0x4B
ELE5_R = 0x4C
ELE6_T = 0x4D
ELE6_R = 0x4E
ELE7_T = 0x4F
ELE7_R = 0x50
ELE8_T = 0x51
ELE8_R = 0x52
ELE9_T = 0x53
ELE9_R = 0x54
ELE10_T = 0x55
ELE10_R = 0x56
ELE11_T = 0x57
ELE11_R = 0x58
FIL_CFG = 0x5D
ELE_CFG = 0x5E
GPIO_CTRL0 = 0x73
GPIO_CTRL1 = 0x74
GPIO_DATA = 0x75
GPIO_DIR = 0x76
GPIO_EN = 0x77
GPIO_SET = 0x78
GPIO_CLEAR = 0x79
GPIO_TOGGLE = 0x7A
ATO_CFG0 = 0x7B
ATO_CFGU = 0x7D
ATO_CFGL = 0x7E
ATO_CFGT = 0x7F

# Global Constants

TOU_THRESH = 0x06
REL_THRESH = 0x0A

# Routines

def readData(address):
	MSB = bus.read_byte_data(address, 0x00)
	LSB = bus.read_byte_data(address, 0x01)

	#touchData = (MSB << 8) | LSB
	touchData = MSB;

	return touchData;

def setup(address):

	bus.write_byte_data(address, ELE_CFG, 0x00)

	# Section A - Controls filtering when data is > baseline.
	 
	bus.write_byte_data(address, MHD_R, 0x01)
	bus.write_byte_data(address, NHD_R, 0x01)
	bus.write_byte_data(address, NCL_R, 0x00)
	bus.write_byte_data(address, FDL_R, 0x00)

	# Section B - Controls filtering when data is < baseline.

	bus.write_byte_data(address, MHD_F, 0x01)
	bus.write_byte_data(address, NHD_F, 0x01)
	bus.write_byte_data(address, NCL_F, 0xFF)
	bus.write_byte_data(address, FDL_F, 0x02)	

	#Section C - Sets touch and release thresholds for each electrode

	bus.write_byte_data(address, ELE0_T, TOU_THRESH)
	bus.write_byte_data(address, ELE0_R, REL_THRESH)

	bus.write_byte_data(address, ELE1_T, TOU_THRESH)
	bus.write_byte_data(address, ELE1_R, REL_THRESH)

	bus.write_byte_data(address, ELE2_T, TOU_THRESH)
	bus.write_byte_data(address, ELE2_R, REL_THRESH)

	bus.write_byte_data(address, ELE3_T, TOU_THRESH)
	bus.write_byte_data(address, ELE3_R, REL_THRESH)

	bus.write_byte_data(address, ELE4_T, TOU_THRESH)
	bus.write_byte_data(address, ELE4_R, REL_THRESH)

	bus.write_byte_data(address, ELE5_T, TOU_THRESH)
	bus.write_byte_data(address, ELE5_R, REL_THRESH)

	bus.write_byte_data(address, ELE6_T, TOU_THRESH)
	bus.write_byte_data(address, ELE6_R, REL_THRESH)

	bus.write_byte_data(address, ELE7_T, TOU_THRESH)
	bus.write_byte_data(address, ELE7_R, REL_THRESH)

	bus.write_byte_data(address, ELE8_T, TOU_THRESH)
	bus.write_byte_data(address, ELE8_R, REL_THRESH)

	bus.write_byte_data(address, ELE9_T, TOU_THRESH)
	bus.write_byte_data(address, ELE9_R, REL_THRESH)

	bus.write_byte_data(address, ELE10_T, TOU_THRESH)
	bus.write_byte_data(address, ELE10_R, REL_THRESH)

	bus.write_byte_data(address, ELE11_T, TOU_THRESH)
	bus.write_byte_data(address, ELE11_R, REL_THRESH)	

	# Section D
	# Set the Filter Configuration
	# Set ESI2

	bus.write_byte_data(address, FIL_CFG, 0x04)

	# Section E
	# Electrode Configuration
	# Set ELE_CFG to 0x00 to return to standby mode

	bus.write_byte_data(address, ELE_CFG, 0x0C)  # Enables all 12 Electrodes	
