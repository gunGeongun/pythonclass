from Poetry import *
title = '진달래 꽃'
poet='김소월'
contents = '''
시시시시시시 시시시시시시시시시시시시ㅍ
시시시시시시시시시시시시시시시시시시시시시시
시시시시시시시시시시시시
시시시시시시시시시시시시시시
시시시시시시시시시시시시시시시시시시시시
시시시시시시시시시시
'''
myPoetryBook=list()
myPoetry = Poetry(title,poet,contents.split('\n'))
myPoetryBook.append(myPoetry)
title = '진달래 꽃2'
poet='김소월'
contents = '''
시시시시시시 시시시시시시시시시시시시ㅍ
시시시시시시시시시시시시시시시시시시시시시시
시시시시시시시시시시시시
시시시시시시시시시시시시시시
시시시시시시시시시시시시시시시시시시시시
시시시시시시시시시시
'''

myPoetry = Poetry(title,poet,contents.split('\n'))
myPoetryBook.append(myPoetry)
