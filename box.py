def box(width, height):
    for h in range(height):
        print width * '#'

'''
OR

def orBox(width, height):
	print ('#' * width + '\n') * height
'''

box(int(raw_input('width?')), int(raw_input('height?')))
