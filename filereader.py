import os
try:
  name=input("enter a file:")
  handle=open(name)
except:
  print("invalid file name!")
  quit()
upfile=name.upper()
current_path=os.path.dirname(os.path.realpath(__file__))
subdir="subdir"
filepath=os.path.join(current_path,subdir,upfile)
path=current_path+"/"+subdir
if not os.path.exists(path):
    os.mkdir(os.path.join(current_path,subdir))
file_object=open(filepath,"w")
for line in handle:
    upline=line.upper()
    file_object.write(upline)
