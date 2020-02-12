from pathlib import Path
FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
#print(FILENAME.split())
newfile = file_contents.split("\n")
print("First line of the RNU6_269P.txt file:", newfile[0])