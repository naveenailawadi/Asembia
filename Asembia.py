# object to handle an attendee and get the relevant information
class Attendee:
	def __init__(self, data):
		self.data = data

	# to dict function to export relevant data points
	def to_dict(self):
		relevant_dict = {
			'first_name': self.data['firstName'],
			'last_name': self.data['lastName'],
			'title': self.data['title'],
			'company': self.data['company']
		}

		return relevant_dict