# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 01:42:26 2017

@author: seung eon
"""
'''
import math as m
word = input('단어를 입력하시오\n')

iter_num = m.floor(len(word)/2)
count = 0

for i in range(iter_num):
    if len(word)%2==0 and word[i]==word[2*iter_num-i-1]:
        count+=1
    if len(word)%2==1 and word[i]==word[2*iter_num-i]:
        count+=1
        
if count==iter_num:
    print('회문입니다.')
else :
    print('회문이 아닙니다.')
''' 
    
word = input('단어를 입력하시오\n')

iter_num = int(len(word)/2) # len(word)//2 랑 똑같데..ㅠ
count = 0

for i in range(iter_num):
    if word[i]==word[-i-1]:
        count+=1
        
if count==iter_num:
    print('회문입니다.')
else :
    print('회문이 아닙니다.')