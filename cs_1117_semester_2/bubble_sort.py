L1 = [5, 89, 21, 9, 7, 3, 10, 29, 87]  # n = 6


def BubbleSort(l):

    # loop for every round or iteration over the list that we need to take n=20, n-1 iterations i.e 19
    for noPasses in range(len(l)-1):
        change = False
    # loop for every pair we need to examine - in a single given iteration
        for PairNo in range(len(l)-1):
        # if the second number is less than the first number
            if l[PairNo] > l[PairNo+1]:
                temp = l[PairNo]
                l[PairNo] = l[PairNo + 1]
                l[PairNo + 1] = temp
                change = True
        #    however Python has a lovely little function SWAP - l[PairNo],l[PairNo+1] = l[PairNo+1], l[PairNo]
        #       #x,y = y,x this will NOT work in any other language
        #       # be ware of x,y = y,x (works) and the inbuilt swap function.
        #       # While they work we will do a "traditional" swap
        #       # swap by creating a temporary third variable.
        if change == False:
            return l
       
        print("Round", noPasses + 1, ":", l)


# Python program for implementation of Selection Sort

# Traverse through all array elements
def selectionSort(l):
    for i in range(len(l)):
        
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
                
        # Swap the found minimum element with
        # the first element		
        l[i], l[min_idx] = l[min_idx], l[i]

        return l
       
    print("Round", noPasses + 1, ":", l)




# Implementation of Insertion Sort
# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])



myList1 = BubbleSort(L1)
mylist2 = selectionSort(L1)
myList3 = insertionSort(L1)

