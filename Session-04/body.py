from pathlib import Path

FILENAME = "U5.txt"

contents = Path(FILENAME).read_text()

lines = contents.split("\n")

#the join is to connect the \n with the list of strings

body = "\n".join(lines[1:])

print(body)