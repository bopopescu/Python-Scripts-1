from subprocess import PIPE, Popen

listing = Popen(["ls", "-l"], stderr=PIPE, stdout=PIPE)

for bytes in listing.stdout:
    line = bytes.decode()
    if line.startswith("total"):
        continue
    splitline=line.split()

    if int(splitline[4]) > 100:
        print("%s \t\t\t %s" %(splitline[8], splitline[4]))


