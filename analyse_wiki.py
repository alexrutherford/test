import nltk
import collections
import operator

data=open('Pulse_Labs_Network_SOP.txt','r').read()

tokens=nltk.word_tokenize(data)
bigram_measures=nltk.collocations.BigramAssocMeasures()
finder=nltk.collocations.BigramCollocationFinder.from_words(tokens)

wordHash=collections.defaultdict(int)

stopWords=['to','of','and','in','as','is','or','with','\xb7','on',':',',','the','from','an','by','be','are','that','for','a','The','(',')','&','\xad',';',"'s",'not','such','other','all','at','this','it']

stopWords.append('should')
stopWords.append('have')
stopWords.append('may')
stopWords.append('will')
stopWords.append('can')

for t in tokens:
	wordHash[t.lower()]+=1

for stopKey in stopWords:
	try:
		del wordHash[stopKey]
	except:
		print 'CANT DELETE ',stopKey

sortedWords=sorted(wordHash.iteritems(), key=operator.itemgetter(1))
sortedWords.reverse()
for s in sortedWords[:20]:
	print '====> ',s

