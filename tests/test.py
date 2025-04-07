import AnonDrop

AnonDrop.CLIENT_ID = "1318419994400526488"

output = AnonDrop.upload("test.txt")
print(output.fileurl)
print(output.filepage)
print(output.fileid)
fileid = output.fileid
input("Press Enter to delete the file...")

AnonDrop.delete(fileid)
