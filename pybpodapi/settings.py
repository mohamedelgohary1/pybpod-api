# !/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime, time


PYBPOD_API_LOG_LEVEL = None
PYBPOD_API_LOG_FILE  = 'pybpod-api.log'

PYBPOD_API_MODULES = [
	'pybpod_rotaryencoder_module'
]

# stream the session file to the stdin (terminal)
PYBPOD_API_STREAM2STDOUT = True
# accept commands from the stdin
PYBPOD_API_ACCEPT_STDIN  = False

#SUPPORTED BPOD FIRMWARE VERSION
#TARGET_BPOD_FIRMWARE_VERSION = "9"  # 0.7.5
#TARGET_BPOD_FIRMWARE_VERSION = "13" # 0.7.9
#TARGET_BPOD_FIRMWARE_VERSION = "15" # 0.8
#TARGET_BPOD_FIRMWARE_VERSION = "17" # 0.9
TARGET_BPOD_FIRMWARE_VERSION  = "20"  

SERIAL_PORT 	= None
NET_PORT 		= None
WORKSPACE_PATH 	= 'BPOD-WORKSPACE'
PROTOCOL_NAME 	= datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H-%M-%S')
BAUDRATE 		= 1312500
SYNC_CHANNEL 	= 255
SYNC_MODE 		= 1


BPOD_BNC_PORTS_ENABLED 		= [True, True]
BPOD_WIRED_PORTS_ENABLED 	= [True, True]
BPOD_BEHAVIOR_PORTS_ENABLED = [True, True, True, True, True, True, True, True]

#SERIAL_PORT = '/dev/ttyACM0'

