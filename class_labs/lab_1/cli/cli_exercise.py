import sys, getopt

try:
    opts, args = getopt.getopt(sys.argv[1:],'hdo:', ['help', 'decode', 'outputfile='])
except getopt.GetoptError:
    print('Error: Unknown option detected.')
    print('Type <scriptname> -h for help.')
    sys.exit(1)
print('Options: ', end='')
print(opts)
print('Arguments: ', end='')
print(args)


keystring = None
outputfile = None
operation = "encode"

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print('Usage:')
        print('  <scriptname> [-o <outputfile> -d] <inputfile> <keystring>')
        print('  <scriptname> [--outputfile <outputfile> --decode] <inputfile> <keystring>')
        print('Warning: The -d and --decode commands set the program to decrypt. To encrypt, omit these commands.')
        sys.exit(0)
    elif opt in ('-o', '--outputfile'):
        outputfile = arg
    elif opt in ('-d', '--decode'):
        operation = "decode"


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

# -----------------------------------------------------------------
# TASK: Uncomment the line below and complete it with writing out 
# the hex representation of the key string  
# -----------------------------------------------------------------
print('Key bytes:  ' + keystring.encode('ascii').hex())

# real processing would start here ...

