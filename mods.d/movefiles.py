import os
import re

files = os.listdir('.')
for f in files:
    if not f.endswith(".conf"):
        continue
    #print(f)
    s = open(f).read()
    new_name = re.match("\[([a-zA-Z0-9]*)\]",s).group(1)
    old_name = new_name.lower()
    print(f"git mv {old_name}.zip {new_name}.zip")

