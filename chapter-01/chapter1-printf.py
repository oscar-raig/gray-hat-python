from ctypes import *
libc = CDLL("/usr/lib/libc.dylib")
message_string = "Hello world!\n"
libc.printf("Testing: %s", message_string)
