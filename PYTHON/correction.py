import glob
import errno
path = '/home/meenu/Desktop/bbox/Labels/001/*.txt' #note C:
files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:
        	
            for line in f:
                text = line.split()
                if (text == ['0']):
                	print f
    except IOError as exc: #Not sure what error this is
        if exc.errno != errno.EISDIR:
            raise