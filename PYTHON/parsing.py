#parsing is used for making command line interfaces
import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x', type = float, default = 1.0,
						help = 'What is first number?')
	parser.add_argument('--y', type = float, default = 1.0,
						help = 'What is second number?')
	parser.add_argument('--operation', type = str, default = 'sub',
						help = 'What operation?(dd,sub,mul,div)')

	args = parser.parse_args()

	print(str(calc(args.x,args.y,args.operation)))

def calc (x,y,operation):
	
	if operation == 'add':
		return (x+y)
	elif operation == 'sub':
		return (x-y)
	elif operation == 'mul':
		return (x*y)
	elif operation == 'div':
		return (x/y)

if __name__ == '__main__':
	main()