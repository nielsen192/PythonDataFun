from textblob import TextBlob

filetext = open('sample_text.txt', 'r')
text = filetext.read()

print(text)
analysis = TextBlob(text)
print(analysis.sentiment)
filetext.close()
