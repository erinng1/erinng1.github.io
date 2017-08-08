def box(width, height):
    for h in range(height):
        print width * '#'

'''
OR

def orBox(width, height):
	print ('#' * width + '\n') * height

OR OR 

def theOtherBox(width, height)
	for i in range (:height+1) :
		for i in range(:width) :
			print '#', 
		print ''	
'''

box(int(raw_input('width?')), int(raw_input('height?')))
