import argparse
import sys
import os
from collections import defaultdict

def argparsing():
	parser = argparse.ArgumentParser(description='CCWC: word, line, character, and byte count.')
	parser.add_argument('file', type=str, nargs='*', help='Optional file name(s)')
	parser.add_argument('-c', action="store_true", help='Activate count bytes')
	parser.add_argument('-m', action="store_true", help='Activate count characters')
	parser.add_argument('-w', action="store_true", help='Activate count words')
	parser.add_argument('-l', action="store_true", help='Activate count lines')
	args = parser.parse_args()
	files:list = args.file
	opts = {k: args.__dict__[k] for k in args.__dict__ if k!='file'}
	if all(op == False for op in opts.values()):
		opts['c'] = True
		opts['w'] = True
		opts['l'] = True
	if opts['c'] and opts['m']:
		args = "".join(x for x in sys.argv if x.startswith('-'))
		idx_c = args.rfind('c')
		idx_m = args.rfind('m')
		if idx_c < idx_m:
			opts['c'] = False
		else:
			opts['m'] = False
	return files, opts

def count_lines(s:str) -> int:
	return len(s.splitlines())

def count_lines_b(binary_data:bytes) -> int:
	return binary_data.count(b'\n')

def count_words(s:str) -> int:
	return len(s.split())

def count_words_b(binary_data:bytes) -> int:
	return len(binary_data.split())

def count_bytes_fn(filename:str) -> int:
	return os.path.getsize(filename)

def count_chars_b(binary_data:bytes):
	count = 0
	for byte in binary_data:
		if byte & 0xC0 != 0x80:
			# This byte is the start of a new UTF-8 character
			count += 1
	return count

def count_chars_fn(filename:str) -> int:
	with open(filename, 'rb') as file:
		content = file.read()
		return count_chars_b(content)

def ccwc_output(opts, counts, fn):
	cc = f"{counts['c']:>8}" if opts['c'] else ""
	cm = f"{counts['m']:>8}" if opts['m'] else ""
	cw = f"{counts['w']:>8}" if opts['w'] else ""
	cl = f"{counts['l']:>8}" if opts['l'] else ""
	fn = f" {fn}" if fn != "" else ""
	out = f"{cl}{cw}{cc}{cm}{fn}"
	return out

def ccwc_file(filename:str, opts:dict):
	res = {}
	if opts['c']:
		res['c'] = count_bytes_fn(filename)
	if opts['m']:
		res['m'] = count_chars_fn(filename)
	with open(filename) as fd:
		txt = fd.read()
	if opts['w']:
		res['w'] = count_words(txt)
	if opts['l']:
		res['l'] = count_lines(txt)
	return res

def ccwc_stdin(opts:dict):
	res = {}
	binary_data = sys.stdin.buffer.read()
	if opts['c']:
		res['c'] = len(binary_data)
	if opts['m']:
		res['m'] = count_chars_b(binary_data)
	if opts['w']:
		res['w'] = count_words_b(binary_data)
	if opts['l']:
		res['l'] = count_lines_b(binary_data)
	return res

def ccwc():
	files, opts = argparsing()
	counts_l = []
	for f in files:
		counts = ccwc_file(f, opts)
		counts_l.append(counts)
		out = ccwc_output(opts, counts, f)
		print(out)
	if len(files) > 1:
		res = defaultdict(int)
		for file_count in counts_l:
			for o, v in file_count.items():
				res[o] += v 
		out = ccwc_output(opts, res, "total")
		print(out)
	if not files:
		counts = ccwc_stdin(opts)
		out = ccwc_output(opts, counts, "")
		print(out)

if __name__ == "__main__":
	ccwc()