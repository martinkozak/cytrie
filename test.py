import cytrie


#trie = {}
"""
for i in range (0, 10000000):

	addition = str(i)
	trie[addition] = addition
"""
"""
dict = {}

for i in range (0, 1000000):

	addition = str(i)
	dict[addition] = addition
"""	
#work = {"abc": "111", "def": "222"}

trie = cytrie.Trie()
#trie.prepare()
#trie["1"] = "1"
#trie["2"] = "2"
#print trie
#trie2 = cytrie.Trie()
#trie2.add("2", "2")

#trie.add_dictionary(dict)
trie.prepare()
for i in range (0, 1000000):
#	trie = cytrie.Trie()
#	trie = {}
#	trie["aaaaaaa"] = "aaaaaa"
#	trie["ccccccc"] = "cccccc"
#	trie["bbbbbbb"] = "bbbbbb"	
#	foo = trie["aaaaaaa"]
#	foo = trie["ccccccc"]
#	foo = trie["bbbbbbb"]
	addition = str(i)
#	trie.add(addition, addition)
	trie[addition] = addition

trie.shape()
#trie.clear()
#items = trie.dictionary()
#print str(trie)[0:100]

#for i in range(0, 10000000):
#	trie1 += trie2

#print len(trie)

#items = trie.dictionary()
#print items
#print len(keys)

#new_trie = trie.copy()
#items = new_trie.items()
#print items


#trie.add("1", "1")
#trie.add("12345", "12345")
#	
#trie.remove_clean("12345")

#trie.add("abc", "def")
#trie.add("ghi", "jkl")
	
#print trie.get("ghi")

#for i in range(0, 1000000):
#	trie.remove(str(i))
#
#trie.clear()
#	
#for i in range(0, 1000000):
#	foo = trie.get(str(i))
#	foo = trie[str(i)]
#	print foo

