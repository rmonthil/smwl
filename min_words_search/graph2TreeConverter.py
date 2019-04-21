from collections import deque # Import les files
from math import inf

class graph_to_tree_converter:
	def __init__(self):
		self.words = {}
		self.ax_words = []
		# Tarjan algorithm utils
		self.tarj_nb = 0
		self.tarj_pile = []
		self.tarj_partition = {}

	def compute(self, input_words, store_ax_file):
		self.words = input_words
		self._compute_parts(store_ax_file)
		self._compute_distance()
		return self.words, self.tarj_partition
		#return self._compute_simple_parts(store_ax_file)
		
	def _compute_parts(self, store_ax_file):
		
		print('CONVERT : Tarjan')
		self._tarjan()
		print('CONVERT : Parts nb : ' + str(len(self.tarj_partition)))
		print('CONVERT : Word nb : ' + str(len(self.words)))
		
		# print('CONVERT : Computing in parts.')
		# _compute_in_parts()
		print('CONVERT : Computing out parts.')
		self._compute_out_parts()
		
		print('CONVERT : Computing axiomatic words.')
		# Search for no out parts as the axiomatic words
		for p_name in self.tarj_partition:
			p = self.tarj_partition[p_name]
			if p['out_parts'] == []:
				self.ax_words.append(p_name)
		print('CONVERT : Axiomatic words nb : ' + str(len(self.ax_words)))
		
		print("CONVERT : Storing axiomatic words in : " + store_ax_file)
				
		with open(store_ax_file, 'w', encoding='utf-8') as f:
			for a_w in self.ax_words:
				f.write(a_w + ' : ' + str(self.tarj_partition[a_w]['words']) + '\n')
		
		print("CONVERT : End")
		
	def _tarjan(self):
		self.tarj_nb = 0
		self.tarj_pile = []
		self.tarj_partition = {}
		
		for w in self.words:
			if not ('nb' in self.words[w]):
				self._parcours(self.words[w])
				
		# Clean
		for w in self.words:
			self.words[w].pop('nb')
			self.words[w].pop('nbAccess')
			self.words[w].pop('inPile')
		
	def _parcours(self, w):
		w['nb'] = self.tarj_nb
		w['nbAccess'] = self.tarj_nb
		self.tarj_nb = self.tarj_nb + 1
		
		self.tarj_pile.append(w)
		w['inPile'] = True
		
		for ww in w['out_words']:
			ww = self.words[ww]
			if not ('nb' in ww):
				self._parcours(ww)
				w['nbAccess'] = min(w['nbAccess'], ww['nbAccess'])
			elif ('inPile' in ww) and ww['inPile']:
				w['nbAccess'] = min(w['nbAccess'], ww['nb'])
	 
		if w['nbAccess'] == w['nb']:
			part_words = []
			ww = {}
			ww['word'] = '--null--'
			while not (ww['word'] == w['word']):
				ww = self.tarj_pile.pop()
				ww['inPile'] = False
				ww['partition'] = w['word'] # We know in wich part it is
				part_words.append(ww['word'])
			
			part = {}
			part['words'] = part_words
			
			self.tarj_partition[w['word']] = part
			
	###############################################################################
	# In and out Parts ############################################################
	###############################################################################
			
	def _compute_in_parts(self):
		# Initialising in words
		for p in self.tarj_partition:
			p = self.tarj_partition[p]
			p['in_parts'] = []
			for w in p['words']:
				w = self.words[w]
				for ww in w['in_words']:
					ww = self.words[ww]
					# First, checking if it is not one of its words.
					if not (ww['word'] in p['words']):
						# Then, checking if it is not already added.
						if not (ww['partition'] in p['in_parts']):
							# Adding the part
							p['in_parts'].append(ww['partition'])

	def _compute_out_parts(self):
		# Initialising in words
		for p in self.tarj_partition:
			p = self.tarj_partition[p]
			p['out_parts'] = []
			for w in p['words']:
				w = self.words[w]
				for ww in w['out_words']:
					ww = self.words[ww]
					# First, checking if it is not one of its words.
					if not (ww['word'] in p['words']):
						# Then, checking if it is not already added.
						if not (ww['partition'] in p['out_parts']):
							# Adding the part
							p['out_parts'].append(ww['partition'])
	
	###############################################################################
	# Computing Distance ##########################################################
	###############################################################################
	
	def _compute_distance(self):
		print('COMPUTE : Distance')
		
		# Init
		for w in self.words:
			w = self.words[w]
			w["dist_to_parts"] = []
			w["part_words"] = []
			w["marked"] = -1
			for i in range(len(self.tarj_partition[w["partition"]]["out_parts"])):
				w["dist_to_parts"].append(inf)
				w["part_words"].append('0_none')
		
		# Compute
		mark = 0
		for w in self.words:
			w = self.words[w]
			
			if not ("completed" in w):
				# Parcours
				mark += 1
				
				print('COMPUTE DISTANCE : ' + w['word'])
				
				self._distance_parcours(w, mark)
		
		# Clean
		for w in self.words:
			w = self.words[w]
		
			w.pop('marked')
			if ('completed' in w):
				w.pop('completed')
				
		# Put as relative
		for w in self.words:
			w = self.words[w]
			
			if(w["dist_to_parts"]):
				m = min(w["dist_to_parts"])
				for k in range(len(w["dist_to_parts"])):
					w["dist_to_parts"][k] -= m 
		
		print("COMPUTE : End")
		
		return self.words
		
	def _distance_parcours(self, w, mark):
		w['marked'] = mark
		
		i = 0
		for ww in w['out_words']:
			ww = self.words[ww]
			if(ww['partition'] == w['partition']):
				if (not (ww['marked'] == mark)) and (not ('completed' in ww)):
					self._distance_parcours(ww, mark)
				for k in range(len(w["dist_to_parts"])):
					# Process min my_self to save word too
					old = w['dist_to_parts'][k]
					tmp = max(i,ww['dist_to_parts'][k])
					if(tmp < old):
						w['dist_to_parts'][k] = tmp
						w["part_words"][k] = ww["part_words"][k]
			else:
				k = self.tarj_partition[w["partition"]]["out_parts"].index(ww['partition'])
				old = w['dist_to_parts'][k]
				tmp = i
				if(tmp < old):
					w['dist_to_parts'][k] = tmp
					w["part_words"][k] = ww["word"]
			i += 1
			
		# Check if completed
		k = 0
		completed = True
		while completed and k < len(w['part_words']):
			completed = w["part_words"][k] != "0_none"
			k += 1
		
		if(completed):
			w['completed'] = True
	###############################################################################
	# Other way to do it ##########################################################
	###############################################################################
	
	def _compute_simple_parts(self, store_ax_file):
		
		print('CONVERT : Simple')
		
		# Init
		for w in self.words:
			self.words[w]["out_parts"] = []
		
		nb = 0
		for w in self.words:
			w = self.words[w]
			if not ('nb' in w):
				self._simple_parcours(w, [nb])
				nb = nb + 1
		
		# Clean
		for w in self.words:
			self.words[w].pop('nb')
		
		print('CONVERT : Computing leaves.')
		# Search for no out parts as the axiomatic words
		for w in self.words:
			w = self.words[w]
			if w['out_words'] == []:
				self.ax_words.append(w['word'])
		print('CONVERT : Leaves nb : ' + str(len(self.ax_words)))
		
		print("CONVERT : Storing leaves words in : " + store_ax_file)
				
		with open(store_ax_file, 'w', encoding='utf-8') as f:
			for a_w in self.ax_words:
				f.write(a_w + '\n')
		
		print("CONVERT : End")
			
	def _simple_parcours(self, w, nbs):
		w['nb'] = nbs[0]
		
		print('CONVERT SIMPLE TREE : ' + w['word'])
		
		for ww in w['out_words']:
			ww = self.words[ww]
			if not ('nb' in ww):
				# We can go deeper
				w['out_parts'].append(ww['word'])
				self._simple_parcours(ww, nbs)
			elif not (ww['nb'] in nbs):
				# We can take possesion of the tree
				w['out_parts'].append(ww['word'])
				nbs.append(ww['nb'])
			else:
				# We can cut the link
				pass