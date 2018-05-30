import sys,time,random,os

from colorama import Fore, Style
b = Fore.BLUE
g = Fore.GREEN
r = Fore.RED
y = Fore.GREEN
c = Fore.CYAN
w = Fore.WHITE
res = Style.RESET_ALL

def clear():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])

def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
                                                                    HashTools V1.0
                                                __  __           __       ______            __    
                                               / / / /___ ______/ /_     /_  __/___  ____  / /____
                                              / /_/ / __ `/ ___/ __ \     / / / __ \/ __ \/ / ___/
                                             / __  / /_/ (__  ) / / /    / / / /_/ / /_/ / (__  ) 
                                            /_/ /_/\__,_/____/_/ /_/    /_/  \____/\____/_/____/  
                                                iraniancoders.ir  -   iran-cyber.net
                                                            github.com/iwhh                                              
------------------------------------------------------------------------------------------------------------------------------------------------------

    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

def base64():
	print y + "[" + r + "!" + y + "] " + c + "Methods -> \n" + y + "[" + r + "1" + y + "] " + g + "base64 Encode\n" + y + "[" + r + "2" + y + "] " + g + "base64 Decode"

def getback():
	print y + "[" + r + "1" + y + "] " + g + "Back yo menu\n" + y + "[" + r + "2" + y + "] "+ g + "Exit"
def gb():
	print r + "-----------------------------------------------"
	print y + "[" + r + "1" + y + "] " + g + "Back to menu\n" + y + "[" + r + "2" + y + "] " + g + "Exit"

def options():
	text = y + "[" + r + "*" + y + "] " + w + "Methods -> \n" + y + "[" + r + "1" + y + "] " + g + "Base64 \n" + y + "[" + r + "2" + y + "] " + g + "Md5 \n" + y + "[" + r + "3" + y + "] " + g + "Sha1 \n" + y + "[" + r + "4" + y + "] " + g +  "Sha224 \n" + y + "[" + r + "5" + y + "] " + g + "Sha256 \n" + y + "[" + r + "6" + y + "] " + g + "Sha384 \n" + y + "[" + r + "7" + y + "] " + g + "Sha512 "
	print text
def md5():
	print y + "[" + r + "!" + y + "] " + c + "Methods -> \n" + y + "[" + r + "1" + y + "] " + g + "md5 Encode\n"

def sha224():
	print y + "[" + r + "!" + y + "] " + c + "Methods -> \n" + y + "[" + r + "1" + y + "] " + g + "sha224 Encode\n"
def sha1():
	print y + "[" + r + "!" + y + "] " + c + "Methods -> \n" + y + "[" + r + "1" + y + "] " + g + "sha1 Encode\n"
def sha256():
	print y + "[" + r + "!" + y + "] " + c + "Methods -> \n" + y + "[" + r + "1" + y + "] " + g + "sha256 Encode\n"
def sha384():
	print y + "[" + r + "!" + y + "] " + c + "Methods -> \n" + y + "[" + r + "1" + y + "] " + g + "sha384 Encode\n"
def sha512():
	print y + "[" + r + "!" + y + "] " + c + "Methods -> \n" + y + "[" + r + "1" + y + "] " + g + "sha512 Encode\n"