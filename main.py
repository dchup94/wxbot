from wxpy import *
import random
import os
from time import sleep

bot = Bot(cache_path=True)

#sizy = bot.friends().search('sizy')[0]
#maolongniao = bot.groups().search('毛龙鸟')[0]

me = bot.friends().search('代楚鹏')[0]
tuling = Tuling(api_key= 'e5e67be375004adc9148946fe28ba7b8')

#maolongniao.send('再来一发')

blocked=[]

f = 'f'
g = 'g'

def addblock(name):
	member = bot.chats().search(name)[0]
	if member not in blocked:
		blocked.append(member)
	
def removeblock(name):
	member = bot.chats().search(name)[0]
	if member in blocked:
		blocked.remove(member)
#sizy.send('试试AI聊天')
#blocked.append(sizy)

@bot.register(msg_types=TEXT,except_self=False)
def block(msg):
	if msg.chat == me:
		if msg.text == '屏蔽':
			me.send(blocked)
		else:
			try:
				try:
					if msg.text.split(' ')[0] == '解除':
						removeblock(msg.text.split(' ')[1])
						me.send('已解除' + msg.text.split(' ')[1])
					else:
						addblock(str(msg.text))
						me.send('已屏蔽' + str(msg.text))
				except:
					addblock(str(msg.text))
					me.send('已屏蔽' + str(msg.text))
			except:
				pass
	else:
		if msg.text == '屏蔽':
			if msg.chat not in blocked:
				blocked.append(msg.chat)
		elif msg.text == '解除屏蔽':
			if msg.chat in blocked:
				blocked.remove(msg.chat)
			
	bot.messages.clear()
	
	
@bot.register(msg_types=TEXT)
def auto_reply_text(msg):
	if msg.text == '屏蔽':
		if msg.chat not in blocked:
			blocked.append(msg.chat)
	elif msg.text == '解除屏蔽':
		if msg.chat in blocked:
			blocked.remove(msg.chat)
			msg.chat.send('屏蔽解除')
	else:
		if msg.chat not in blocked:
			tuling.do_reply(msg,at_member=False)
	
	bot.messages.clear()
	
@bot.register(msg_types=PICTURE)
def auto_reply_pic(msg):
	if msg.chat not in blocked:
		pic = random.choice(os.listdir("pics/"))
		print(pic)
		msg.chat.send_image('pics/' + pic)
	
	bot.messages.clear()

	
embed()