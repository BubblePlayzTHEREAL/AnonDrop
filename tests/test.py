import AnonDrop

AnonDrop.CLIENT_ID = "CLIENT ID HERE"

output = AnonDrop.upload("test.txt")
print(output.fileurl)
print(output.filepage)
print(output.fileid)
fileid = output.fileid
input("Press Enter to delete the file...")

AnonDrop.delete(fileid)
