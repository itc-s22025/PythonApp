import requests
import json
import webbrowser
from random import *
from PIL import Image, ImageDraw, ImageFont
import io


class Pillow:
	def create_img(self):
		self.appended_sen = '\n'.join(Ts.sentenses)
		text = self.appended_sen
		self.Pillow_img = Image.open(io.BytesIO(requests.get(Pb.Pimage1).content))
		self.Pillow_draw = ImageDraw.Draw(self.Pillow_img)
		self.Pillow_font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',20)
	#	for i,s in enumerate(text):
	#		y = i*20
		self.Pillow_draw.text((6,16), text, fill=(245,245,245), font=self.Pillow_font)
		self.Pillow_draw.text((6,250), '「五行小説もどきジェネレータ」', fill=(245,245,245), font=self.Pillow_font)
		print('画像を生成しています...')
		self.Pillow_img.show() 


class Pixabay:
	def call_pic(self):
		self.Pbase = 'https://pixabay.com/api/?key=' 
		self.Pkey = '29451301-ec4c613c485d788191898b0f0'
		self.Pq = '/&q='
#		self.Pcol = '&colors='
		self.Pcolors = 'black'
		self.Pmin = '&min_width=640'
#		self.Psens = []
#		for _ in range(5):
#			self.Psens.append(Ts.sen)
	#	print(self.Psens)
		if '緑' in Ts.sen:
			self.Pcolors = 'green'
		elif '赤' in Ts.sen:
			self.Pcolors = 'red'
		elif '黃' in Ts.sen:
			self.Pcolors = 'yellow'
		elif '白' in Ts.sen:
			self.Pcolors = 'white'
		elif '青' in Ts.sen:
			self.Pcolors = 'blue'

		self.Purl = f'{self.Pbase}{self.Pkey}{self.Pq}%27{self.Pcolors}%27+%27{Ts.n}%27{self.Pmin}'
#		print(self.Purl)

		self.Pres = requests.get(self.Purl)
		self.Pjson_data = json.loads(self.Pres.content)
		self.Phits = self.Pjson_data['hits']
		self.Pimage = [i['webformatURL'] for i in self.Phits]
		self.Pnum = choice(self.Pimage)
		self.Pimage1 = self.Pimage[self.Pimage.index(self.Pnum)]
#		self.Pd = webbrowser.open_new_tab(self.Pimage1)
		print('画像を生成しています...')
		Pl.create_img()
#		print(self.Pimage1)


class TextSuggest:
	def __init__(self, base='https://api.a3rt.recruit.co.jp/text_suggest/v2/predict?apikey=', key='DZZDTGlGKXX6t5x20WbpNz3xiZ1C3zlY', pre='&previous_description='):
		self.base = base
		self.key = key
		self.pre = pre

	def make_text(self):
		self.lists = []
		self.texts = []
		self.urls = []
		self.sentenses = []
		for _ in range(5):
			self.typed = input('Type any words: ')
			self.lists.append(self.typed)

		for _ in range(5):
			self.word = choice(self.lists)
			self.texts.append(self.word)

		for n in self.texts:
			#self.n = choice(self.texts)
			self.url = f'{self.base}{self.key}{self.pre}{n}'
			self.urls.append(self.url)

		for m in self.urls:
			for _ in range(5):
				self.n = choice(self.texts)
			self.res = requests.get(m)
			self.json_data = json.loads(self.res.content)
			self.sugg = self.json_data['suggestion']
			self.text = [d for d in self.sugg]
			self.num = choice(self.text)
			self.this = self.text[self.text.index(self.num)]
			self.sen = list(f'{self.n}{self.this}')
			self.nas = ['にな','がな']
			self.na = choice(self.nas)
			self.sus = ['す','した']
			self.su = choice(self.sus)
			if self.sen[1] == 'な':
				self.sen[1] = f'{self.na}'
			if self.sen[-2] == 'す':
				self.sen[-2] = f'{self.su}'
			self.sentenses.append(''.join(self.sen))
		print('画像を生成しています...')		
		Pb.call_pic()


while True:
	Ts = TextSuggest()
	Pb = Pixabay()
	Pl = Pillow()
	qtn = input('プログラムを実行しますか？  y/n: ')
	if qtn == 'y':
		Ts.make_text()
	elif qtn == 'n':
		print('Bye :)')
		break
	else:
		print('Type y or n :(')





