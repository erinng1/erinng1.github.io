def box(width, height):
    for h in range(height):
        print width * '#'


box(int(raw_input('width?')), int(raw_input('height?')))
