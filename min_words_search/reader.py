import simplejson as json

# Check distance to out parts for each word

class reader():
	def __init__(self):
		self.words = {}
		
	def compute(self, in_file):
		return self._read_graph(in_file)

	def _read_graph(self, in_file):
		
		print("READ : Reading json file : " + in_file)
		
		with open(in_file, 'r', encoding='utf-8') as f:
			data_text = f.read()
			
		print("READ : Parsing json file")
		
		self.words = json.loads(data_text, strict=False)
		
		print("READ : End, words nb : ", len(self.words))
		
		return self.words
		
	# def _compute_in_words(self):
		# # Initialising in words
		# for w in self.words:
			# self.words[w]['in_words'] = []
		# # Compute in words
		# for w in self.words:
			# w = self.words[w]
			# for ww in w['out_words']:
				# ww = self.words[ww]
				# ww['in_words'].append(w['word'])