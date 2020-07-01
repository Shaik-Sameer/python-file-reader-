import os
try:
    name=input("enter a file:")
    handle=open(name)
except:
    print("invalid file name!")
    quit()
upfile=name.upper()
try:
    file=input("enter a path for creation of new file without file name:")
    filepath=os.path.join(file,upfile)
    if not os.path.exists(file):
        os.mkdir(file)
    file_object=open(filepath,"w")
except:
    print("invalid file path" )
    quit()
for line in handle:
    upline=line.upper()
    file_object.write(upline)
