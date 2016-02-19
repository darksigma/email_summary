from pyteaser import Summarize
import sys

text_file = sys.argv[1]
title_file = sys.argv[2]
text = open(text_file, 'rb').read()
title = open(title_file, 'rb').read()

summaries = Summarize(text, title)
print summaries
