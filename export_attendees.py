from constants import CLEAN_FILE, EXCEL_FILE
from Asembia import Attendee
import pandas as pd
import json
import sys

# get attendees out of a response
def get_attendees_from_response(resp):
	# try to get 2 levels of data --> should be a list of attendees
	try:
		new_attendees = resp['data']['searchAttendees']['data']
	except KeyError:
		# return an empty list if there is nothing here
		return []

	# make a clean attendees list
	clean_attendees = []

	# for each attendee, save some information
	for attendee in new_attendees:
		# make a clean attendee
		clean_attendee = Attendee(attendee)

		# append the attendee in dictionary form
		clean_attendees.append(clean_attendee.to_dict())

	print(f"Found {len(clean_attendees)} new attendees")

	# return the clean list
	return clean_attendees

# main function
def main(clean_file=CLEAN_FILE, excel_file=EXCEL_FILE):
	# open the infile
	with open(clean_file, 'r', encoding='utf8') as clean_file:
		# get the responses
		responses = json.loads(clean_file.read())

	# make a attendee list
	attendee_list = []

	# iterate over all responses --> add attendees from each
	for resp in responses:
		new_attendees = get_attendees_from_response(resp)

		attendee_list.extend(new_attendees)

	# export the attendee list to an excel file
	df = pd.DataFrame(attendee_list)

	df.to_excel(excel_file, index=False)


if __name__ == '__main__':
	main()