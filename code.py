def no_4_7_after(list):
	sum=0
	for i in range(0,len(list)-1):
		if list[i] == 7:
			sum-=list[i+1]
			sum-=7
			if list[i+1] == 7 or list[i+1] == 4:
				sum+=list[i+1]
		if list[i] == 4:
			sum-=list[i+1]
			sum-=4
			if list[i+1] == 4 or list[i+1] == 7:
				sum+=list[i+1]
		sum += list[i]
	if not list[len(list)-1] == 4 and not list[len(list)-1] == 7:
		sum += list[len(list)-1]
	return sum


japan=[1,2,3,4,1,7,2,2]
print("hello",no_4_7_after(japan))