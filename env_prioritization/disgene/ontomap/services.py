
import requests

def map_ontologies(kword):
	url = 'https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue=mus+musculus'

	params = {'term': kword}
	r = requests.get(url, params=params)
	ontologies = r.json()

	return ontologies