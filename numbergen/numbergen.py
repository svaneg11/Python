#Random numbers generator
import random

nums = []	#list for the random numbers

def main():
	start = int(raw_input('Range from:'))	#start of number range, inclusive.
	stop = int(raw_input('To:'))			#end of number range, inclusive.
	count = int(raw_input('Generate:')) 	#how many numbers you want to generate.
	filename = raw_input('insert name for output file:') #name for exit file. can be omitted by pressing enter
	if filename == '':									 #if omitted exit file will be named 'random.txt'
		filename = 'random.txt'
	file = open(filename,'w')				#opens the file in which we are going to write the generated numbers.
	i = 0
	while i < count:
		nums.append(random.randint(start,stop))  #generates a random within the range [start,stop] and appends it to the end of the list
		i+=1
	#print numbers 						#print list of numbers, since printing might take a lot of time it's adviced to uncomment only for small lists of numbers
	i = 0
	while i < count:
		file.write(str(nums[i])+'\n') 	#write number of index i from the list into the file plus a newline
		i+=1
	file.close()						#close the file
	print 'Done.'

if __name__ == '__main__':
	main()
