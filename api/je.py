import sys
import hh 


if len(sys.argv) < 2:
    print("Too few arguments (No arguments provided)")

elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    singer = sys.argv[1]
    hh.songs(singer)
