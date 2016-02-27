from stanford_tagger import tag_sentence

def is_imperative(sentence, verbose = False):
    if_words = ['if']
    breaks = [',',';',':'] 
    auxiliary_words = ['please', 'ought', 'should', 'must', 'shall', 'might', 'will']
    verb_tags = ['vb', 'vbd', 'vbg', 'vbn', 'vbp', 'vbz']
    noun_tags = ['nn','nns','nnp','nnps','prp', 'prp$' , 'to'] 
    tagged_sentence = tag_sentence(sentence)
    if verbose:
        print 'Tagged sentence: ' + str(tagged_sentence)
    #Remove auxiliary phrases
    is_imperative = False
    cut_point = 0
    if_point = 0
    for i in range(len(tagged_sentence)):
       
        if tagged_sentence[i][0].lower() in if_words:
           if_point = i
           for j in range(min(i + 5, len(tagged_sentence))):
               if tagged_sentence[j][0] in breaks:
                   cut_point = j
           if cut_point == 0:
               cut_point = if_point + 4
    tagged_sentence = tagged_sentence[cut_point:]
    if verbose:
        print 'Removed conditionals: ' + print_words(tagged_sentence)
    cut_point = 0               
    for i in range(min(4, len(tagged_sentence))):
        if tagged_sentence[i][0].lower() in auxiliary_words:
            
            cut_point = i
    tagged_sentence = tagged_sentence[cut_point:]
    if verbose:
        print 'Removed auxiliaries: ' + print_words(tagged_sentence)
          
    for i in range(min(4, len(tagged_sentence))):
        if tagged_sentence[i][1] in verb_tags:
            is_imperative = True
            for j in range(i):
                #print tagged_sentence[j]
                if tagged_sentence[j][1] in noun_tags:
                    return False
    return is_imperative

#print is_imperative('You must go to the market.') 

#print tag_sentence('yolo squad')

def print_words(tagged_sentence):
    breaks = [',', ';', '.', ':', '!', '?']
    sentence_string = ''
    for i in range(len(tagged_sentence)):
       if tagged_sentence[i][0] not in breaks:
           sentence_string += ' '
       sentence_string += tagged_sentence[i][0]
    return sentence_string
