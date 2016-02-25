import sys
sys.path.append('/home/cirrascale/q_files/stanford-corenlp-python/')
import jsonrpc as jsonrpc
from simplejson import loads


def tag_sentence(sentence):

    server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
                             jsonrpc.TransportTcpIp(addr=("127.0.0.1", 8080)))

    result = loads(server.parse(sentence))
    tagged_sentence = []
    
    for word in result[u'sentences'][0][u'words']:
        tagged_sentence.append([word[0], word[1][u'PartOfSpeech'].lower()])
    #print tagged_sentence
    return tagged_sentence

#print tag_sentence('I need you to work on the documents, please have them to me quickly')

