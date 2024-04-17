from constants import INFILE, CLEAN_FILE
import json

# clean function
def clean(dirty_json):
	# first, remove all incompletes
	dirty_json = [obj for obj in dirty_json if obj['status'] == 'COMPLETE']

	# lose the request headers & only save the body's text, but as a json
	bodies = []
	for obj in dirty_json:
		# get the body of the response
		output = json.loads(obj['response']['body']['text'])

		# add the output to the bodies
		bodies.append(output)

	return bodies


# main function
def main(infile=INFILE, clean_file=CLEAN_FILE):
	# open the infile
	with open(infile, 'r', encoding='utf8') as infile:
		# make a json
		json_dict = json.loads(infile.read())

	# clean up the json
	json_dict = clean(json_dict)

	# this will out put all responses to the requests
	with open(CLEAN_FILE, 'w', encoding='utf8') as outfile:
		outfile.write(json.dumps(json_dict, indent=4))


if __name__ == '__main__':
	main()