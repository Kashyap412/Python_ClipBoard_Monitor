from time import strftime
import pyperclip,time,datetime,sys

def Banner(a):
	print("\n"+"#"*49)
	print("#  Welcome to KashY "+a+" #\n#\t\t\t\t\t\t#")
	print("#\t\tStart Cliping ...\t\t#\n#\t\t\t\t\t\t#")
	print("#"*49+"\n\n")

def End_Banner():
	print("\n"+"#"*49+"\n#\t\t\t\t\t\t#")
	print("#\t   Cliping Stoped and Saved \t\t#\n#\t\t\t\t\t\t#")
	print("#"*49+"\n\n")

def createClipBoardFile(data):	
	x = datetime.datetime.now()
	filename = "KashY-ClipBoard-"+str(x.year)+"-"+str(x.month)+"-"+str(x.day)+"-"+str(x.hour)
	filename = str(filename)+".txt"
	
	with open(filename, '+a') as output:
		try:
			output.write("%s\t%s\n\n" % (str(x), str(data)))
		except:
			output.write("%s\t%s\n\n" % (str(x), str(data.encode('UTF-8'))))

old_data = ""
Banner("ClipBoard Sniffing Software")

while True:
	try:
		data = pyperclip.paste()
		if data != old_data:
			old_data = data
			createClipBoardFile(data)
		time.sleep(0.1)
	except KeyboardInterrupt:
		End_Banner()
		sys.exit()