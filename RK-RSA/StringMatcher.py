import RollingHash
import csv
import random
import time
import time
import re


RollingHash = RollingHash.RollingHash

def KarpRabin(s,t):

	#hashing s
	rs = RollingHash(256,2147483647)
	for c in s: rs.append(c)


	rt = RollingHash(256,2147483647)
	#hashing the string consisting of the first |s| chars
	for c in t[:len(s)]: rt.append(c)
	if(rs.hash() == rt.hash()): return 0
	ab = []

	#sliding
	for i in range(len(s),len(t)):
		rt.skip()
		rt.append(t[i])
		if(rs.hash() == rt.hash()): ab.append ( i-len(s)+1 )
	
	return ab

	#if we're here, s is not in t
#	raise ValueError('substring not found')


#assert(KarpRabin("the","the thing we're looking for is here") == 0)
#assert(KarpRabin("567","01234567") == 5)
#assert(KarpRabin("bcd","abcde") == 1)

text = ''
with open("abc.txt", "r+") as file:
	for l in file.readlines():
		text+= l
	file.close()

text1 = ''
with open("efg.txt", 'r+') as file:
	for l in file.readlines():
		text1+= l
	file.close()



print (KarpRabin(text1, text))


def createData(file_name,val):

	#file_name = input("Enter the file name to create >>")
	#key_num = int(input("no of keys to be inserted"))

	key_pat = int(val)
	with open(file_name,'w') as out:

		#rand_list = random.sample(range(0,10000), key_num)
		#rand_list = key_pat
		for val in file_name:
			out.write(str(val))
			#out.write(",")
			#out.write("0")
	

#		while(key_num>0):
#			value = (str(random.randint(1,100))+",")
#			out.write(value)
			#out.write(",")
			#value = str(random.randint(0,1000))
			#out.write(value)
#			key_num-=1
#	
        
	out.close() 
def python_verify(pattern):
	match_list = []
	count = 0
	pat = re.compile(pattern)
	#file = open("abc.txt","r")
	for i,line in enumerate (open("abc.txt","r")):
		#print(line)
		for match in pat.finditer(line):

			match_list.append((count+match.start()))
		count+=len(line)
	print(match_list)


key_pat = ""
while(1):

	

	print ("1. Enter to RK")
	print ('2. exit')
	print("3.verify")

	choice = input("enter your choice? : ")
	
	if(choice == '1'):
		
		key_pat = input("enter the keys patteren : ")
		
		start = time.time()
		print (KarpRabin(key_pat, text))

		end = time.time()
		print("time: ",end - start)

	elif(choice == '2'):
		exit()
	elif(choice == '3'):
		print(key_pat)
		python_verify(key_pat)

	else:
		print("none")
	

#print (KarpRabin("", text))



#error case
#KarpRabin("not found","")