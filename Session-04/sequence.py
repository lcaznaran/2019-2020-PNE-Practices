from pathlib import Path

FILENAME = "ADA.txt"

contents = Path(FILENAME).read_text()

lines = contents.split("\n")

#the join is to connect the \n with the list of strings

body = "".join(lines[1:])

print(len(body))