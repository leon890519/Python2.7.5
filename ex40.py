# -*- coding:utf-8 -*-

# 我们可以在成员名称前添加 "__" 使其成为私有成员
# python中的class属性分为类属性和实例属性，其中实例属性是可以动态构建的，类属性也可以动态创建
# 实例属性可以访问类属性，但是类不能访问实例属性

class Song:
#	song_lyrics = 'class attribute' # Song_lyrics 是类属性
	def __init__(self, lyrics):
		self.lyrics = lyrics # lyrics 是实例属性
#		song_lyrics = lyrics # song_lyrics 只是一个局部变量，不是上面的类属性
#		Song.song_lyrics = lyrics # 创建类属性要用 类名.Attribute = object
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
#	def sing(self):
#		for line in song_lyrics:
#			print line
			
happy_bday = Song(["Happy birthday to you", 
				"I don't want to get sued",
				"So I'll stop right there"])
	
bulls_on_parade = Song(["They rally around the family",
					"With pockets full of shells"])
					
happy_bday.sing_me_a_song()

Song.song_lyrics = "class attribute" # 动态创建类属性
#bulls_on_parade.song_lyrics = 'modify'
print bulls_on_parade.song_lyrics

print Song.song_lyrics