import discord
import time
import configparser
import sys

config = configparser.ConfigParser()
config.read('설정.ini')

token = config['setting']['TOKEN']

client = discord.Client()

succes_password = ''

password = input("비밀번호를 입력해주세요\n")

@client.event
async def on_ready():
    print(f'='*15+'로그인이 성공적으로 되었습니다.'+f'=' * 15)
if password == str(succes_password):
    print('어서오세요 Administrator 님')
elif not password == str(succes_password):
    print('비밀번호가 틀렸습니다.\n2초후 시스템이 종료됩니다.')
    time.sleep(2)
    sys.exit()
else:
    print('이상 접근이 감지되었습니다.\n2초후 시스템이 종료됩니다.')
    time.sleep(2)
    sys.exit()

client.run(token)
