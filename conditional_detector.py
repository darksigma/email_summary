import re
def is_conditional(sentence):
    subsentences = re.split('[,;](?!\d)', sentence)
    conditional_words = ['if']
    for sub in subsentences:
       sub_list = sub.split(' ')
       for word in sub_list[:3]:
           if word.lower() in conditional_words:
               return True
    return False    

#read_emails(sys.argv[1])
