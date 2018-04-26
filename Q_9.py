str1 ='shah'

str2 = 'I am fine shah'
common = list(set([c for c in str1 if c in str2 ]))

print common
#######################################
set_result = set.intersection(set(str1), set(str2))

print set_result
