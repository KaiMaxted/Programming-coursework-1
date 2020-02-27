import os.path

OPTION_RANGE = 14
HEADER_LENGTH = 3
LINE_LENGTH = 10

def greyscale(image_list):

    '''this function returns a greyscale version of the image input. it does this
    by averaging out the red green and blue values of each pixel and replacing them with
    that average'''

    

    for i in range(len(image_list)):
        total = 0
        average = 0
        for j in range(3):
            total += image_list[i][j]
        average = total/3
        for j in range(3):
            image_list[i][j] = int(average)
    
    return(image_list)
            
            


def only_red(image_list):

    '''this function returns an image with only the red values left in each pixel,
    it does this by replacing the blue and green value of each pixel with 0'''
    
    for i in range(len(image_list)):
        image_list[i][1],image_list[i][2] = 0,0

    return(image_list)


def only_blue(image_list):

    '''this function returns an image with only the blue values left in each pixel,
    it does this by replacing the red and green value of each pixel with 0'''
    
    for i in range(len(image_list)):
        image_list[i][0],image_list[i][2] = 0,0

    return(image_list)

def only_green(image_list):

    '''this function returns an image with only the green values left in each pixel,
    it does this by replacing the blue and red value of each pixel with 0'''
    
    for i in range(len(image_list)):
        image_list[i][0],image_list[i][1] = 0,0

    return(image_list)

def negative_red(image_list):

    '''this function returns a "negative red" image of the given image. it does this
    by replacing the red value of each pixel with 255 - it's original value.'''

    for i in range(len(image_list)):
        image_list[i][0] = 255 - image_list[i][0]

    return(image_list)


def negative_green(image_list):

    '''this function returns a "negative green" image of the given image. it does this
    by replacing the green value of each pixel with 255 - it's original value.'''

    for i in range(len(image_list)):
        image_list[i][1] = 255 - image_list[i][0]

    return(image_list)



def negative_blue(image_list):

    '''this function returns a "negative blue" image of the given image. it does this
    by replacing the blue value of each pixel with 255 - it's original value.'''

    for i in range(len(image_list)):
        image_list[i][2] = 255 - image_list[i][0]

    return(image_list)


def negative_image(image_list):

    '''this function does what the above 3 do but all at the same time. it replaces
    each colour value in every pixel with 255 - its original value'''

    for i in range(len(image_list)):
        for j in range(3):
            image_list[i][j] = 255 - image_list[i][j]

    return(image_list)



def extreme_contrast(image_list):

    '''this function returns the extreme contrast of its given image. it does this by
    changing all pixel values that are above 126 to 255 and everything 126 or below to 0.'''

    for i in range(len(image_list)):
        for j in range(3):
            if image_list[i][j] < 127:
                image_list[i][j] = 0
            else:
                image_list[i][j] = 255

    return(image_list)

def stacktwo(image_list):

    '''This function takes the given image and returns two of them on top of each other.
    when this function is called the code doubles the rows that are returned at the end of the program.'''
    

    image_list += image_list

    return(image_list)



def sidebyside(image_list):

    '''this function returns the given image side by side with itself. it does this by zipping two of itself to
    a new list called b twice. it then returns b. when this function is called we have doubled the columns so that it
    outputs the full image'''

    b = []

    for j in range(rows):
        for i in range(cols):
            b.append(image_list[i+cols*j])
        for i in range(cols):
            b.append(image_list[i+cols*j])

    return(b)

def add_frame(image_list):
    b = []
    x = [0,0,0]
    
    valid_option = False

    while not valid_option:
        colour = input("\n\tWhat colour would you like the frame to be?(red/green/blue/white/black/custom):  ")
        if colour == "red":
            x = [255,0,0]
            valid_option = True
        elif colour == "green":
            x = [0,255,0]
            valid_option = True
        elif colour == "blue":
            x = [0,0,255]
            valid_option = True
        elif colour == "white":
            x = [255,255,255]
            valid_option = True
        elif colour == "black":
            x = [0,0,0]
            valid_option = True
        elif colour == "custom":
            valid_red_value = False
            while not valid_red_value:
                red_value = int(input("\n\tinput red value for the frame (min 0, max 255):  "))
                if red_value <= 255 and red_value >= 0:
                    valid_red_value = True
                else:
                    print("\n\tinvalid red value. Please try again.")
            valid_green_value = False
            while not valid_green_value:
                green_value = int(input("\n\tinput green value for the frame (min 0, max 255):  "))
                if green_value <= 255 and green_value >= 0:
                    valid_green_value = True
                else:
                    print("\n\tinvalid green value. Please try again.")
            valid_blue_value = False
            while not valid_blue_value:
                blue_value = int(input("\n\tinput blue value for the frame (min 0, max 255):  "))
                if blue_value <= 255 and blue_value >= 0:
                    valid_blue_value = True
                else:
                    print("\n\tinvalid blue value. Please try again.")
            x = [red_value, green_value, blue_value]
            valid_option = True
            
        else:
            print("\n\tNot a valid colour option. Please choose one of the suggested options.")
    
    
    size = int(cols/20+1)

    for j in range(rows):
        for i in range(size): 
            b.append(x)
        for i in range(cols):
            b.append(image_list[i+cols*j])
        for i in range(size):
            b.append(x)

    b = [x]*size*(size*2 + cols) + b + [x]*size*(size*2 + cols)
    
    return(b)

def rotate_90(image_list):
    b = []
    for i in range(cols):
        for j in range(rows):
            x = (rows-1) - j
            y = (x*cols+i)
            b.append(image_list[y])
    return(b)




def menu_option(menu_option):
    l = len(menu_option)
    print("\t\t<-|-|-|-|-"," "*5, menu_option," "*(25-l), "\t-|-|-|-|->")
    
    
            
    


def print_menu():
	titler("Picture options: ")
	menu_option("[1]  convert to greyscale")
	menu_option("[2]  just the reds")
	menu_option("[3]  just the greens")
	menu_option("[4]  just the blues")
	menu_option("[5]  negative reds")
	menu_option("[6]  negative greens")
	menu_option("[7]  negative blues")
	menu_option("[8]  negative image")
	menu_option("[9]  extreme contrast")
	menu_option("[10]  stack two pictures")
	menu_option("[11]  side by side")
	menu_option("[12]  four pictures")
	menu_option("[13]  frame the picture")
	menu_option("[14]  rotate 90 clockwise")
	


def get_menu_option(prompt):

	valid_option = False

	while not valid_option:
		print_menu()
		try:
			option = int(input(prompt))
			if option in range(1, OPTION_RANGE + 1) :
				valid_option = True
			else:
				raise ValueError
		except ValueError:
			print("\n\n\tthat's not a valid choice, please try again.")

	return option


def get_valid_filename(prompt):
	'''Use prompt (a string) to ask the user to type the name of a file. If
	the file does not exist, keep asking until they give a valid filename.
	Return the name of that file.
	'''

	filename = input(prompt)
	while not os.path.exists(filename):
		print("That file does not exist.")
		filename = input(prompt)
	return filename


def get_dimensions(input_filename):
	''' Read the image size from the file header.
		Return a tuple containing the number of rows and columns.
	'''

	with open(input_filename, 'r') as file:
		file.readline()
		dimensions = file.readline().split()

	rows = int(dimensions[0])
	cols = int(dimensions[1])
	return rows, cols



def get_file_contents(input_filename):
	'''
	Return the tokens in the file as a list.
	Ignore the file header.
	'''

	line_count = 1
	read_data = []

	with open(input_filename, 'r') as file:

		for line in file:
			# ignore the header
			if line_count <= HEADER_LENGTH:
				line_count += 1
			else:
				read_data += line.split()

	return read_data


def read_image(input_filename):
	'''
	Return a list of the pixels in the file.
	'''

	read_data = get_file_contents(input_filename)

	# convert all the ascii pixel values to numbers
	read_data = [ int(x) for x in read_data ]

	# put the r,g,b values in a list
	all_pixels = []
	for i in range(0, len(read_data), 3):
		rgb = read_data[i : i + 3]
		all_pixels.append(rgb)

	return all_pixels


def write_image(rows, cols, image, output_filename):
	''' Write the list of pixels to a file. '''

	with open(output_filename, 'w') as file:
		file.write("P3\n")
		file.write(str(rows) + " " + str(cols) + "\n")
		file.write("255\n")

		for i in range(len(image)):
			for channel in image[i]:
				file.write(str(channel))
				file.write(" ")

			file.write("\t")

			if i % LINE_LENGTH == 0:
				file.write("\n")

def titler(TITLE):
    l = len(TITLE)
    for i in range(3):
        print()
    print("\t\t", "*"*l)
    print("\t\t", TITLE)
    print("\t\t", "*"*l)
    for i in range(3):
        print()



if __name__ == '__main__':

    titler("Welcome to the Portable Pixmap (PPM) Image Editor!")


    prompt = "\n\tenter the name of the image file: "
    input_image_filename = get_valid_filename(prompt)


    # This isn't a very efficient approach but it's best for the coursework
    cols, rows = get_dimensions(input_image_filename)

    image_list = read_image(input_image_filename)

    output_image_filename = input("\n\tenter the name of the output file: ")

    prompt = "\n\tyour choice: "
    menu_choice = get_menu_option(prompt)

    if menu_choice == 1:
        greyscale(image_list)
        rows,cols=cols,rows
    elif menu_choice == 2:
        only_red(image_list)
    elif menu_choice == 3:
        only_green(image_list)
    elif menu_choice == 4:
        only_blue(image_list)
    elif menu_choice == 5:
        negative_red(image_list)
    elif menu_choice == 6:
        negative_green(image_list)
    elif menu_choice == 7:
        negative_blue(image_list)
    elif menu_choice == 8:
        negative_image(image_list)
    elif menu_choice == 9:
        extreme_contrast(image_list)
    elif menu_choice == 10:
        stacktwo(image_list)
        rows = rows*2
    elif menu_choice == 11:
        image_list = sidebyside(image_list)
        cols = cols*2
    elif menu_choice == 12:
        image_list = sidebyside(image_list)
        cols = cols*2
        image_list = stacktwo(image_list)
        rows = rows*2
    elif menu_choice == 13:
        image_list = add_frame(image_list)
        rows += (int(cols/20)*2) + 2
        cols += (int(cols/20)*2) + 2
    elif menu_choice == 14:
        image_list = rotate_90(image_list)
        rows,cols = cols,rows
    
        


    write_image(cols, rows, image_list, output_image_filename)
    print("\nImage written to file: {}".format(output_image_filename))
