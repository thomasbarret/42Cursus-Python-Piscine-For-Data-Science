import sys

try:
	if len(sys.argv) == 1:
		print("")
		sys.exit()
	if len(sys.argv) != 2:
		raise AssertionError("more than one argument is provided")

	if int(sys.argv[1]) % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
     
except ValueError:
    print(f"AssertionError: argument is not an integer")
except AssertionError as e:
    print(f"AssertionError: {e}")
    
    



    