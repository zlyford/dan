import sys, wave


def compare(path1, path2):
    file1 = open_file(path1)
    file2 = open_file(path2)
    print 'comparing ' + path1 + ' and ' + path2 + '...'
    # do stuff here

# opens the audio file at the given location
def open_file(path):
    try:
        audio = wave.open(path)
    except:
        sys.stderr.write('ERROR: ' + str(sys.exc_info()[0]) + '\n')
        sys.exit(-1)
    return audio


# Parse arguments
if __name__ == '__main__':
    if (len(sys.argv) != 5) or (sys.argv[1] != '-f') or (sys.argv[3] != '-f'):
        sys.stderr.write('ERROR: Invalid command.\n')
        sys.exit(-1)
    else:
        compare(sys.argv[2], sys.argv[4])
        sys.exit(0)
