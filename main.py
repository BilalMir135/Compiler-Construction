import lexer
import syntaxAnalyzer
import json

#read code from file
with open('code2.txt','r') as file:
    source_code = file.read()

#create tokens
lex = lexer.Lexical_Analyzer()
tokens = lex.tokenization(source_code)

#print tokens
#for token in tokens:
    #print(token)

#store tokens in file
with open ('tokens.json','w') as file:
    json.dump(tokens,file)

#adding last token
tokens.append(('$','$','$'))

sa = syntaxAnalyzer.SyntaxAnalyzer(tokens)
sa.parser()