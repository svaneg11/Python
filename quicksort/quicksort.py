numeros = []	#list that keep the numbers for sorting



def main():
	path = raw_input('Insert name of the file to sort:')	#read name/path of unsorted
	exitfile = raw_input('Insert name for exit file:')		#read name for output file
	archivo = open(path,'r')							#open file to read
	linea = archivo.readline()							#read line from file
	while linea!='':									#while there is something to read
		numeros.append(int(linea))						#append number from line to the end of numeros[]
		linea = archivo.readline()						#read next line
	archivo.close()										#close file
	#print numeros,'\n'									#print numbers before sorting.it's adviced to uncomment only for small lists of numbers
	sort()
	#print numeros										#print numbers after sorting.
	salida = open(exitfile,'w')							#create a new file and open it to insert the sorted numbers
	count = 0
	while count<len(numeros):
		salida.write(str(numeros[count])+'\n')			#write sorted list into output file
		count+=1
	print 'Sorted.'



def sort():								#Starts quicksort
	if(len(numeros)>1):					#if numbers to sort are more than one, do
		quicksort(0,len(numeros)-1)		#quicksort is started with a partition from index 0 to length of list-1 (whole list).
	else:
		return



def quicksort(low,high):
	"""low: from where the partition begins
	   high: where the partition ends
	   the partition is the range of the list where each recursion is working"""

	i = low			#index i from the list starts from low
	j = high		#index j from the list starts from high

	pivot = numeros[(low+high)/2] 		#pivot is the number of the middle of the list partition

	while i<=j:
		while numeros[i]<pivot: 		#while numbers[i] is less than pivot, increment i
			i+=1

		while numeros[j]>pivot:			#while numbers[j] is greater than pivot, decrement j
			j-=1

		if(i<=j):						#if index i hasn't surpassed index j swap numbers[i] with numbers[j].
			aux = numeros[i]
			numeros[i] = numeros[j]
			numeros[j] = aux
			i+=1						#increment i by 1
			j-=1						#decrement j by 1

	if(i<high):							#if index i hasn't surpassed index high call quicksort with partition from i to high 
		quicksort(i,high)
	if(low<j):
		quicksort(low,j)				#if index low hasn't surpassed index j call quicksort with partition from low to j 




if __name__ == '__main__':
	main()