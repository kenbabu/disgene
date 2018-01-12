
import requests
import json

class  Zooma(object):
	"""docstring for  Zooma"""
	def __init__(self, arg):
		super( Zooma, self).__init__()
		self.arg = arg
	def get_mapped_terms(self):
		return requests.get(url, )


def map_ontologies(kword):
	params = {'term': kword}
	url = 'https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue='
	# p = requests.get('https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue={0}'.format(kword))

	p = requests.get(url+kword)
	
	jsondata = json.loads(p.text)
	return json.dumps(jsondata, indent=4, sort_keys=False)

print map_ontologies('cancer')