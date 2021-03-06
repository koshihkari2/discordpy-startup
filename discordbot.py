import urllib.parse
from discord.ext import commands
import os
import traceback
import wikipedia
from discord.ext import tasks
from datetime import datetime 
import requests
import discord
from bs4 import BeautifulSoup
import re



CHANNEL_ID = 684761828483792943
bot = commands.Bot(command_prefix='=')
token = os.environ['DISCORD_BOT_TOKEN']


import random
#テキストファイルに書き換え予定
random_list = ['わかばシューター','もみじシューター','おちばシューター','スプラシューターコラボ','.52ガロン','.96ガロンデコ','シャープマーカー','Ｎ－ＺＡＰ８９','Ｎ－ＺＡＰ８５','プライムシューター','シャープマーカネオ','ボールドマーカーネオ','プロモデラーＲＧ','スプラシューター','.52ガロンデコ','Ｌ3リールガンＤ','ジェットスイーパーカスタム','プライムシューターコラボ','もみじシューター','プロモデラーＭＧ','Ｈ3リールガンチェリー','.96ガロン','ボールドマーカー７','Ｎ－ＺＡＰ８３','Ｌ3リールガン','ジェットスイーパー','Ｈ3リールガンＤ','ボトルガイザー','ボトルガイザーフォイル','スプラシューターベッチュー','プライムシューターベッチュー','Ｌ3リールガンベッチュー','.52ガロンベッチュー','デュアルスイーパー','デュアルスイーパーカスタム','スプラマニューバー','スプラマニューバーコラボ','スパッタリー','ケルビン525','スパッタリー・ヒュー','クアッドホッパーブラック','ケルビン525デコ','クアッドホッパーホワイト','スプラマニューバ－ベッチュー','ケルビン525ベッチュー','スパッタリークリア','スプラスコープ','スクイックリンα','スプラチャージャー','１４式竹筒銃・甲','スクイックリンγ','１４式竹筒銃・丙','スクイックリンβ','１４式竹筒銃・乙','ソイチューバー','スプラチャージャーコラボ','リッター４Ｋ','４Ｋスコープ','リッター４Ｋカスタム','４Ｋスコープカスタム','ソイチューバーカスタム','スプラチャージャーベッチュー','スプラスコープベッチュー','ノヴァブラスターネオ','ロングブラスターカスタム','ホットブラスターカスタム','ノヴァブラスター','ラピッドブラスラー','ロングブラスターネクロ','ホットブラスター','Ｒブラスターエリートデコ','ラピットブラスターデコ','ロングブラスター','クラッシュブラスター','クラッシュブラスターネオ','ノヴァブラスターベッチュー','ラピッドブラスターベッチュー','ダイナモローラー','スプラローラーコラボ','カーボンローラー','ダイナモローラーテスラ','スプラローラー','カーボンローラーデコ','ヴァリアブルローラー','ヴァリアブルローラーフォイル','スプラローラーベッチュー','ダイナモローラーベッチュー','ホクサイ','パブロ','ホクサイ・ヒュー','パーマネントパブロ','パブロ・ヒュー','ホクサイベッチュー','バケットスロッシャー','ヒッセン','スクリュースロッシャー','バケットスロッシャーデコ','バケットスロッシャーソーダ','ヒッセン・ヒュー','スクリュースロッシャーネオ','エクスプロッシャー','オーバーフロッシャー','スクリュースロッシャーベッチュー','エクスプロッシャーカスタム','オーバーフロッシャーデコ','スプラスピナーコラボ','バレルスピナーデコ','ハイドラントカスタム','バレルスピナー','バレルスピナーリミックス','ハイドラント','スプラスピナー','クーゲルシュライバー','ノーチラス４７','クーゲルシュライバー・ヒュー','ノーチラス７９','スプラスピナーベッチュー','パラシェルター','キャンピングシェルター','スパイガジェット','パラシェルターソレーラ','スパイガジェットソレーラ','キャンピングシェルターソレーラ','スパイガジェットベッチュー','キャンピングシェルターカーモ']

syuter_list = random_list[0:33]


def weather_search(user_id):
    #{user_id(int):weather_id(str)}
    #テキストファイルに書き換え予定
    id_dict = {625161458145034270:'130010',677040897514536960:'120010',475916023690821642:'140020'}
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
    try:
        query_params = {'city': id_dict[user_id]}
    except KeyError:
        return ['あなたの居住区は登録されていません','登録を希望する場合はこしひかりに連絡連絡～♪']
    result_list = []
    data = requests.get(url, params=query_params).json()
    for weather in data['forecasts']:
        result_list.append(weather['dateLabel'] + 'の天気：' + weather['telop'])
    return result_list



@bot.event
async def on_ready():
    CHANNEL_ID = 684761828483792943
    channel = bot.get_channel(CHANNEL_ID)
#     await channel.send('おはよう！')
    url = os.environ['URL']
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content,'lxml')
    elems = soup.select('#l-main > div:nth-child(4) > dl > dd:nth-child(2) > a')
    str_elems = str(elems)
    url_end = re.search('html', str_elems).end()
    send_url = url[:-10] + str_elems[10:url_end]
    title_start = re.search('>', str_elems).end()
    title = str_elems[title_start: -5]
    embed = discord.Embed(title=title, description=send_url, color=discord.Color.blue())
    await channel.send(embed=embed)

    
@bot.command()
async def buki(ctx,arg='スベテ'):
    """
    ランダムで武器をひとつ選びます
    シューター・マニューバー・ローラー・チャージャー・ブラスター・
    スピナー・スロッシャー・フデ・シェルターから種類を指定できます。
    何も指定しなかった場合はすべての武器からランダムで選びます。
    """
    if arg == 'マニューバー':
        await ctx.send(random.choice(random_list[33:46]))
    elif arg == 'シューター':
        await ctx.send(random.choice(random_list[0:33]))
    elif arg == 'ローラー':
        await ctx.send(random.choice(random_list[77:87]))
    elif arg == 'チャージャー':
        await ctx.send(random.choice(random_list[46:63]))
    elif arg == 'ブラスター':
        await ctx.send(random.choice(random_list[63:77]))        
    elif arg == 'スピナー':
        await ctx.send(random.choice(random_list[106:118]))   
    elif arg == 'スロッシャー':
        await ctx.send(random.choice(random_list[94:106]))
    elif arg == 'フデ':
        await ctx.send(random.choice(random_list[87:93]))
    elif arg == 'シェルター':
        await ctx.send(random.choice(random_list[118:]))
    elif arg == 'スベテ':
        await ctx.send(random.choice(random_list))

    
@bot.command()
async def weather(ctx):
    """
    コマンド実行者居住区の天気を知ることができます
    """
    result = weather_search(ctx.author.id)
    title_name = f'★{ctx.author.name}居住区の天気★'
    word_num = len(result)
    if word_num == 2:
        reply = f'{result[0]}\n{result[1]}'
    elif word_num == 3:
        reply = f'{result[0]}\n{result[1]}\n{result[2]}'
    else:
        reply = 'エラーだよ！'
    embed = discord.Embed(title=title_name,description=reply,color=0X00BFFF)
    await ctx.send(embed=embed)
    
@bot.command()
async def wiki(ctx,*,search_word):
    """
    指定した単語をwikipediaで検索します。10個以内の検索候補を表示します。
    知りたいものの左に書かれている数字を受け取ると、その単語の説明・URLを送信します。
    """
    wikipedia.set_lang('ja')
    number = 0
    express = ''
    search = wikipedia.search(search_word)
    for i in search:
        #print(str(number) + i)
        number += 1
        express += str(number) + ':' + i + '\n'
    embed = discord.Embed(title='検索候補',description=express,color=0x00FFFF)
    await ctx.send(embed=embed)

    if len(search) > 0:

        def check(m):
            try:
                int(m.content)
            except ValueError:
                return False
            else:
                return m.author == ctx.author and m.channel == ctx.channel and 1<= int(m.content) <= 10

        base_index = await bot.wait_for('message',check=check,timeout=60)
        index = int(base_index.content) - 1
        try:
            wiki_page = wikipedia.page(search[index])
        except Exception:
            responce_word = 'エラーだよ！'
        else:
            wiki_content = wiki_page.content
            responce_word = wiki_content[0:wiki_content.find("。")] + "。\n"
            wiki_word = urllib.parse.unquote(wiki_page.url[30:])
            responce_word += 'https://ja.wikipedia.org/wiki/' + wiki_word
    else:
        responce_word = 'その単語は登録されてないよ！'
    
    embed = discord.Embed(title='検索結果', description=responce_word, color=0x00FFFF)
    await ctx.send(embed=embed)
    
@bot.command()
async def notification(ctx):
    if ctx.author.id != 625161458145034270:
        print('無視')
        return
    url = os.environ['URL']
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content,'lxml')
    elems = soup.select('#l-main > div:nth-child(4) > dl > dd:nth-child(2) > a')
    str_elems = str(elems)
    url_end = re.search('html', str_elems).end()
    send_url = url[:-10] + str_elems[10:url_end]
    title_start = re.search('>', str_elems).end()
    title = str_elems[title_start: -5]
    embed = discord.Embed(title=title, description=send_url, color=discord.Color.blue())
    await ctx.send(embed=embed)


    
bot.run(token)

