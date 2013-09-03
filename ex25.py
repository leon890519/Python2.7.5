# -*- coding:utf-8 -*-

def break_words(stuff):
	"""This function will break up words for us."""   # 当在python编译器中 import ex25 后，help（ex25）会将本行也打印出来。
	words = stuff.split(' ')
	return words  # 此时返回的words 是一个list
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
def print_first_word(words): # 此时的words是一个list，对words操作会改变它自己。类似c++中的引用传递
	"""Prints the first word after popping it off."""
	word = words.pop(0) 
	print word
	
def print_last_word(words):
	"""Prints the last word after popping if off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)