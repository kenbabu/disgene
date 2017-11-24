
import requests

def map_ontologies(kword):
	params = {'term': kword}
	url = 'https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue='
	r = requests.get(url, params=params)
	p = requests.get('https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue={0}'.format(kword))
	print p

	return p.json()

	# print url+kword
	# ontologies = r.json()

	# return ontologies

print map_ontologies('cancer')