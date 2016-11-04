mapping=dict()
temp=""
plain=open('unigrams','w')
unique_values=[]

with open('curiosity_output') as f:
    for line in f:
    	line=line[:-1]
    	# print line
    	# print "---------------------------------------"
    	try:
    		#it is the list
    		fruits = eval(line)
    		# print "fruits",fruits
    		mapping[temp]=fruits
    	except:
    		#if it is the name of the word
    		# print "vegetables",line
    		mapping[line]=""
    		temp=line

for key,value in mapping.items():
	for ttuple in value:
		# print value,": ",ttuple
		for x in ttuple:
			if isinstance(x, (str, unicode)):
				print x,": ",ttuple
				if x not in unique_values:
					unique_values.append(x)
					plain.write(x)
					plain.write("\n")

f.close()
plain.close()