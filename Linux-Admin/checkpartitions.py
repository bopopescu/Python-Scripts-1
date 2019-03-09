from optparse import OptionParser

# create the parser
parser = OptionParser()

parser.add_option("-t", "--threshold",
                  dest = "threshold",
                  type = "int",
                  default= 70,
                  help = "Set threshold to 80/90/100"
                )

(options, args) = parser.parse_args()
print("threshold is %d" % options.threshold)


