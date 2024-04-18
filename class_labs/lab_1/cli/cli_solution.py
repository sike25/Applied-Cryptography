import sys, getopt

try:
# ------------------------------------------------------------------------------------
    opts, args = getopt.getopt(sys.argv[1:],'hdo:', ['help', 'decode', 'outputfile='])
#                                             ^              ^^^^^^^^^
#                           new option added here     and      here
# ------------------------------------------------------------------------------------
except getopt.GetoptError:
    print('Error: Unknown option detected.')
    print('Type <scriptname> -h for help.')
    sys.exit(1)

# ------------------------------------------
# default operation is set to 'encode'
#
operation = 'encode' # default operation
# ------------------------------------------
keystring = None
outputfile = None

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print('Usage:')
# ------------------------------------------------------------------------------------
        print('  <scriptname> [-d -o <outputfile>] <inputfile> <keystring>')
        print('  <scriptname> [--decode --outputfile <outputfile>] <inputfile> <keystring>')
#                             ^^^^^^^^^
#                      usage strings are updated
# ------------------------------------------------------------------------------------
        sys.exit(0)
# ------------------------------------------
# handling the new option
#
    elif opt in ('-d', '--decode'):
        operation = 'decode'
# ------------------------------------------
    elif opt in ('-o', '--outputfile'):
        outputfile = arg

if len(args) < 2:
    print('Error: Input file name or key string is missing.')
    print('Type <scriptname> -h for help.')
    sys.exit(1)
else:
    inputfile = args[0]
    keystring = args[1]

if not outputfile:
    outputfile = inputfile
    print('Warning: No output file name was given, input file will be overwritten.')

print('Input file name:  ' + inputfile)
print('Output file name: ' + outputfile)
print('Key string: ' + keystring)
print('Key bytes:  ' + keystring.encode('ASCII').hex())
# ------------------------------------------
# printing out the option
#
print('Operation: ' + operation)
# ------------------------------------------

# real processing would start here ...
