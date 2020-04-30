import sys

if __name__ == '__main__':
	# Look for the name in exec args..
	# Get it from text input if not found.
	try:
		name = sys.argv[1]
	except IndexError:
		name = input('name: ')
	
	# No name yet? Let's put something!
	if not name:
		name = 'people'

	# Text output with the hello message.
	print('Hello, ', name, '.', sep='')
