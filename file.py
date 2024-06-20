import math

def smallest(list):
	smallestItem = list[0]
	for item in list:
		if item < smallestItem:
			smallestItem = item
	return smallestItem

def sort(list):
	sortedList = []
	limit = 0
	while limit < len(list):
		small = smallest(list)
		sortedList.append(small)
		list.remove(small)
	return sortedList

def median(list):
	newList = sort(list)
	if len(newList) % 2 != 0:
		median = newList[math.floor(len(newList)/2)]
		print(f"The median is {median}.")
	else:
		higherMiddleNum = newList[math.floor(len(newList)/2 - 1)]
		lowerMiddleNum = newList[math.ceil(len(newList)/2)]
		median = (int(higherMiddleNum) + int(lowerMiddleNum)) / 2
		print(f"The median is {median}.")

def mean(list):
	finalValue = 0
	for item in list:
		finalValue = finalValue + int(item)
	print(f"The mean is {finalValue / 2}.")

def range(list):
  newList = sort(list)
  print(f"The range is {newList[-1] - newList[0]}.")

while 1:
	print("------------------------------------------------------------------------")
	print("----------Standard Deviation Calculator (with no math functions)--------")
	print("------------------------------------------------------------------------")
	
	list = input("Provide a list of numbers (separated by commas):").split(",")
	options = ["Sort", "Median", "Mean", "Range"]
	for count, ele in enumerate(options, 1):
	  print(f"{count}. {ele}")
	option = input(">>> ")
	if option.lower() == "exit":
		break
	match int(option):
		case 1:
	    		sort(list)
	  	case 2:
	    		median(list)
	  	case 3:
	    		mean(list)
	  	case 4:
	    		range(list)
