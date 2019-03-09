import subprocess

def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print ("\n Gathering system information with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])

def diskspace_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print ("\n Gathering diskspace information %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])


def alternatediskspace():
    diskspace1 = "df -h"
    print ("\n Gathering diskspace information %s command:\n" % diskspace)
    subprocess.call(diskspace1, shell=True)

def listing():
    listing="ls"
    listing_args= "-l"
    listing_path="/"
    subprocess.call([listing, listing_args,listing_path])

def main():
    uname_func()
    diskspace_func()

if __name__ == '__main__':
    main()
