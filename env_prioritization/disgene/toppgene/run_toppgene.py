import mechanize
import re

br = mechanize.Browser()

# Automate the data submission
br.open("https://toppgene.cchmc.org/prioritization.jsp")


class  Transaction(object):
	"""docstring for  Transaction"""
	def __init__(self, url):
		self.url = url
	def run(self):
		br = mechanize.Browser()
		br.set_handle_robots(False)
		# br.addheaders = [('User-agent', 'Mozilla/5.0 Compatible')]
		resp = br.open(url)
		resp.read()

		assert(resp.code == 200), 'Bad Response: HTTP %s' % resp.code

		br.select_form(nr=1)
		br.form['name']='sickle cell'

		resp = br.submit()
		# resp.read()
		assert(resp.code == 200), 'Bad Response: HTTP %s' % resp.code
		return resp.read()

if __name__ == "__main__":
	url = 'http://localhost:8000/search/'
	trans = Transaction(url)

	print trans.run()

