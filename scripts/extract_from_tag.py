import re

file = open('../raw/Posts.xml')

def read_row (file):
  flag = False
  row = ''
  for i in range(0, 1000000):
    character = file.read(1)
    if not character:
      return row

    row += character

    if flag and character == '>':
      return row
    if character == '/':
      flag = True
    else:
      flag = False

for i in range(10):
  row = read_row(file)
  matches = re.search('Tags="(?:&lt;([^;]+)&gt;)+"', row)
  if matches is not None:
    print (matches.group(1))