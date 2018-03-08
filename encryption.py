# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 16:48:16 2018

@author: Utkarsh
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newmessage = ''

message = input('Please enter a message: ')

for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		newposition = (position + key) %26
		newcharacter = alphabet[newposition]
		newmessage += newcharacter
	else:
		newmessage += character