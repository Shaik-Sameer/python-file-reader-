try:
  name=input("enter a file:")
except:
  print("invalid file name!")
  quite()
handle=open(name)
file_object=open("ABC.txt","w")
for line in handle:
    upline=line.upper()
    file_object.write(upline)
