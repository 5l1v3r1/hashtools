# CopyRight IranianCoders.ir
# Editors are not programmers ;)<3

import ircoders, sys, os, time, random, base64, hashlib, webbrowser
try:
	import pyaes
except ImportError:
	print "pyaes module not installed yet\nInstalling . . .\nwhen finished run again this isciprt !"
	time.sleep(3)
	linux = 'sudo apt install python-pyaes'
	windows = 'pip install pyaes'
	os.system([linux, windows][os.name == 'nt'])
	sys.exit(	)
try:
	from colorama import Fore, Style
	cb = Fore.BLUE
	cbl = Fore.BLACK
	cr = Fore.RED
	cy = Fore.YELLOW
	cg = Fore.GREEN
	cc = Fore.CYAN
	rs = Style.RESET_ALL
except ImportError:
	print "colorama module not installed yet\nInstalling . . .\nwhen finished run again this script !"
	time.sleep(3)
	linux = 'sudo apt install python-colorama'
	windows = 'pip install colorama'
	os.system([linux, windows][os.name == 'nt'])
	sys.exit()

class base64(object):
	def __init__(self):
		self.base64()
	def base64(self):
		ircoders.clear()
		ircoders.print_logo()
		ircoders.base64()
		self.getinputb = raw_input(cc + " $ ")
		if self.getinputb == "1":
			self.enc = raw_input(cc + "Enter Your Text to Encode it : ")
			self.base64encode()
		elif self.getinputb == "2":
			self.dec = raw_input(cc + "Enter Your text to decode it : ")
			self.base64decode()
		else:
			print cg + "[ " + cg + "! Unknown Input !" + cr + " ]"
			sys.exit()
	def base64encode(self):
		print cr + "-----------------------------------------------"
		print cb + "Encoding ..."
		time.sleep(1.5)
		encoded = self.enc.encode('base64')
		print cr + "Encoded  ~> " + cy + encoded
		with open('base64-encoded.txt', 'w') as e:
			e.write(self.enc + " : " + encoded + "\n")
			e.close()
		ircoders.gb()
		self.getback = raw_input(cc + " $ ")
		if self.getback == "1":
			options()
		elif self.getback == "2":
			print cg + " Nice to meet you <3"
			sys.exit()
	def base64decode(self):
		print cr + "-----------------------------------------------"
		print cb + "Encoding ..."
		time.sleep(1.5)
		decoded = self.dec.decode('base64')
		print cr + "Decoded ~> " + cy + decoded
		with open('base64-decoded.txt', 'w') as e:
			e.write(self.dec + " : " + decoded + "\n")
			e.close()
		ircoders.gb()
		self.getback = raw_input(cc + " $ ")
		if self.getback == "1":
			options()
		elif self.getback == "2":
			print cg + " Nice to meet you <3"
class md5(object):
	def __init__(self):
		ircoders.clear()
		ircoders.print_logo()
		ircoders.md5()
		self.md5()
	def md5(self):
		self.getinputmd = raw_input(cc + " $ ")
		if self.getinputmd == "1":
			self.getinputmd51 = raw_input(cc + "Enter Your Text to Encode it : ")
			self.md5encode()
		else:
			print cg + "[ " + cg + "! Unknown Input !" + cr + " ]"
	def md5encode(self):
		print cr + "-----------------------------------------------"
		print cb + "Encoding ..."
		time.sleep(1.5)
		encoded = hashlib.md5(self.getinputmd51).hexdigest()
		print cr + "encoded ~> " + cy + encoded
		with open('md5-encoded.txt', 'w') as e:
			e.write(self.getinputmd51 + " : " + encoded)
			e.close()
		ircoders.gb()
		self.getback = raw_input(cc + " $ ")
		if self.getback == "1":
			options()
		elif self.getback == "2":
			print cg + " Nice to meet you <3"
			sys.exit()
class sha1(object):
	def __init__(self):
		ircoders.clear()
		ircoders.print_logo()
		ircoders.sha1()
		self.sha1()
	def sha1(self):
		self.getmt = raw_input(cc + " $ ")
		if self.getmt == "1":
			self.getsha1 = raw_input(cc + "Enter Your Text to Encode it : ")
			self.sha1encode()
		else:
			pass
	def sha1encode(self):
		sha1 = hashlib.sha1(str(self.getsha1))
		encoded = sha1.hexdigest()
		print cr + "-----------------------------------------------"
		print cb + "Encoding ..."
		time.sleep(1.5)
		print cr + "encoded ~> " + cy + encoded
		with open('sha1-encoded.txt', 'w') as e:
			e.write(self.getsha1 + " : " + encoded + "\n")
			e.close()
		ircoders.gb()
		self.getback = raw_input(cc + " $ ")
		if self.getback == "1":
			options()
		elif self.getback == "2":
			print cg + " Nice to meet you <3"
			sys.exit()
class sha224(object):
	def __init__(self):
		ircoders.clear()
		ircoders.print_logo()
		ircoders.sha224()
		self.sha224()
	def sha224(self):
		self.getmethod = raw_input(cc + " $ ")
		if self.getmethod == "1":
			self.getsha224 = raw_input(cc + "Enter Your Text to Encode it : ")
			self.sha224encode()
		else:
			pass
	def sha224encode(self):
		sha224 = hashlib.sha224(str(self.getsha224))
		encoded = sha224.hexdigest()
		print cr + "-----------------------------------------------"
		print cb + "Encoding ..."
		time.sleep(1.5)
		print cr + "encoded ~> " + cy + encoded
		with open('sha224-encoded.txt', 'w') as e:
			e.write(self.getsha224 + " : " + encoded)
			e.close()
		ircoders.gb()
		self.getback = raw_input(cc + " $ ")
		if self.getback == "1":
			options()
		elif self.getback == "2":
			print cg + " Nice to meet you <3"
			sys.exit()
class sha256(object):
	def __init__(self):
		ircoders.clear()
		ircoders.print_logo()
		ircoders.sha256()
		self.sha256()
	def sha256(self):
		self.getsha256input = raw_input(cc + " $ ")
		if self.getsha256input == "1":
			self.getsha256 = raw_input(cc + "Enter Your Text to Encode it : ")
			self.sha256encode()
		else:
			pass
	def sha256encode(self):
		sha256 = hashlib.sha256(self.getsha256)
		encoded = sha256.hexdigest()
		print cr + "-----------------------------------------------"
		print cb + "Enconding ..."
		time.sleep(1.5)
		print cr + "Encoded ~> " + cy + encoded
		with open('sha256-encoded.txt', 'w') as e:
			e.write(self.getsha256 + " : " + encoded + "\n")
			e.close()
		ircoders.gb()
		self.getback = raw_input(cc + " $ ")
		if self.getback == "1":
			options()
		elif self.getback == "2":
			print cg + " Nice to meet you <3"
			sys.exit()
class sha384(object):
	def __init__(self):
		ircoders.clear()
		ircoders.print_logo()
		ircoders.sha384()
		self.sha384()
	def sha384(self):
		self.inp = raw_input(cc + " $ ")
		if self.inp == "1":
			self.getsha384 = raw_input(cc + "Enter Your Text to Encode it : ")
			self.sha384encode()
		else:
			pass
	def sha384encode(self):
		sha384 = hashlib.sha384(str(self.getsha384))
		encoded = sha384.hexdigest()
		print "-----------------------------------------------"
		print cb + "Encoding ..."
		time.sleep(1.5)
		print cr + "Encoded ~> " + cy + encoded
		with open('sha384-encoded.txt', 'w') as e:
			e.write(self.getsha384 + " : " + encoded + "\n")
			e.close()
		ircoders.gb()
		self.getback = raw_input(cc + " $ ")
		if self.getback == "1":
			options()
		elif self.getback == "2":
			print cg + " Nice to meet you <3"
			sys.exit()
class sha512(object):
	def __init__(self):
		ircoders.clear()
		ircoders.print_logo()
		ircoders.sha512()
		self.sha512()
	def sha512(self):
		self.inp = raw_input(cc + " $ ")
		if self.inp == "1":
			self.getsha512 = raw_input(cc + "Enter Your Text to Encode it : ")
			self.sha512encode()
		else:
			pass
	def sha512encode(self):
		sha512 = hashlib.sha512(str(self.getsha512))
		encoded = sha512.hexdigest()
		print "-----------------------------------------------"
		print cb + "Encoding ..."
		time.sleep(1.5)
		print cr + "Encoded ~> " + cy + encoded 
		with open('sha512-encoded.txt', 'w') as e:
			e.write(self.getsha512 + " : " + encoded + "\n")
			e.close()
		ircoders.gb()
		self.getback = raw_input(cc + " $ ")
		if self.getback == "1":
			options()
		elif self.getback == "2":
			print cg + " Nice to meet you <3"
			sys.exit()
class options(object):
	def __init__(self):
		self.options()
	def options(self):
		ircoders.clear()
		ircoders.print_logo()
		ircoders.options()
		getinput = raw_input(cc + " $ ")
		if getinput == "1":
			base64()
		elif getinput  == "2":
			md5()
		elif getinput == "3":
			sha1()
		elif getinput == "4":
			sha224()
		elif getinput == "5":
			sha256()
		elif getinput == "6":
			sha384()
		elif getinput == "7":
			sha512()
		else:
			print cr + "Unknown Input"
			sys.exit()
try:
	run = options()
except KeyboardInterrupt:
	ircoders.clear()
	print "\nNice To Meet You </3"