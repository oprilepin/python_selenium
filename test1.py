import sys
def create():
    print("creating new  file")
    name=raw_input ("enter the name of file:")
    extension=raw_input ("enter extension of file:")
    try:
        name=name+"."+extension
        file=open(name,'a')

        file.close()
    except:
            print("error occured")
            sys.exit(0)

create()
