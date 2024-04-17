from constants import INFILE
import json

# main function
def main(file=INFILE):
	# open the file
	with open(file, 'r', encoding='utf8') as infile:
		# make a json
		json_dict = json.loads(infile.read())

	# save the new (prettified) soup
	with open(file, 'w', encoding='utf8') as outfile:
		outfile.write(json.dumps(json_dict, indent=4))


if __name__ == '__main__':
	main()