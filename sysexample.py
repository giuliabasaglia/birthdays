import sys
if len(sys.argv)==3:
    name= sys.argv[1]
    data= sys.argv[2]
else:
    print("Please run the program like: "
          "python3 main.py username data") 
    exit() 
