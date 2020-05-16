from discord.ext import commands
import os
import traceback
import wikipedia
import wikitry
from discord.ext import tasks
from datetime import datetime 
import requests
import discord


CHANNEL_ID = 684761828483792943
bot = commands.Bot(command_prefix='=')
token = os.environ['DISCORD_BOT_TOKEN']


import random
random_list = ['わかばシューター','もみじシューター','おちばシューター','スプラシューターコラボ','.52ガロン','.96ガロンデコ','シャープマーカー','Ｎ－ＺＡＰ８９','Ｎ－ＺＡＰ８５','プライムシューター','シャープマーカネオ','ボールドマーカーネオ','プロモデラーＲＧ','スプラシューター','.52ガロンデコ','Ｌ3リールガンＤ','ジェットスイーパーカスタム','プライムシューターコラボ','もみじシューター','プロモデラーＭＧ','Ｈ3リールガンチェリー','.96ガロン','ボールドマーカー７','Ｎ－ＺＡＰ８３','Ｌ3リールガン','ジェットスイーパー','Ｈ3リールガンＤ','ボトルガイザー','ボトルガイザーフォイル','スプラシューターベッチュー','プライムシューターベッチュー','Ｌ3リールガンベッチュー','.52ガロンベッチュー','デュアルスイーパー','デュアルスイーパーカスタム','スプラマニューバー','スプラマニューバーコラボ','スパッタリー','ケルビン525','スパッタリー・ヒュー','クアッドホッパーブラック','ケルビン525デコ','クアッドホッパーホワイト','スプラマニューバ－ベッチュー','ケルビン525ベッチュー','スパッタリークリア','スプラスコープ','スクイックリンα','スプラチャージャー','１４式竹筒銃・甲','スクイックリンγ','１４式竹筒銃・丙','スクイックリンβ','１４式竹筒銃・乙','ソイチューバー','スプラチャージャーコラボ','リッター４Ｋ','４Ｋスコープ','リッター４Ｋカスタム','４Ｋスコープカスタム','ソイチューバーカスタム','スプラチャージャーベッチュー','スプラスコープベッチュー','ノヴァブラスターネオ','ロングブラスターカスタム','ホットブラスターカスタム','ノヴァブラスター','ラピッドブラスラー','ロングブラスターネクロ','ホットブラスター','Ｒブラスターエリートデコ','ラピットブラスターデコ','ロングブラスター','クラッシュブラスター','クラッシュブラスターネオ','ノヴァブラスターベッチュー','ラピッドブラスターベッチュー','ダイナモローラー','スプラローラーコラボ','カーボンローラー','ダイナモローラーテスラ','スプラローラー','カーボンローラーデコ','ヴァリアブルローラー','ヴァリアブルローラーフォイル','スプラローラーベッチュー','ダイナモローラーベッチュー','ホクサイ','パブロ','ホクサイ・ヒュー','パーマネントパブロ','パブロ・ヒュー','ホクサイベッチュー','バケットスロッシャー','ヒッセン','スクリュースロッシャー','バケットスロッシャーデコ','バケットスロッシャーソーダ','ヒッセン・ヒュー','スクリュースロッシャーネオ','エクスプロッシャー','オーバーフロッシャー','スクリュースロッシャーベッチュー','エクスプロッシャーカスタム','オーバーフロッシャーデコ','スプラスピナーコラボ','バレルスピナーデコ','ハイドラントカスタム','バレルスピナー','バレルスピナーリミックス','ハイドラント','スプラスピナー','クーゲルシュライバー','ノーチラス４７','クーゲルシュライバー・ヒュー','ノーチラス７９','スプラスピナーベッチュー','パラシェルター','キャンピングシェルター','スパイガジェット','パラシェルターソレーラ','スパイガジェットソレーラ','キャンピングシェルターソレーラ','スパイガジェットベッチュー','キャンピングシェルターカーモ']

syuter_list = random_list[0:33]


def weather_search():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
    query_params = {'city': '130010'}
    result_list = []
    data = requests.get(url, params=query_params).json()
    for weather in data['forecasts']:
        result_list.append(weather['dateLabel'] + 'の天気：' + weather['telop'])
    return result_list



@bot.event
async def on_ready():
    CHANNEL_ID = 684761828483792943
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')

    
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


@bot.command(aliases=["kan"])
async def kanji(ctx,yomi,kaki):
    """
    漢字テスト対策用コマンドです。
    =kan 読み　書き　のように使用します。
    """
    await ctx.channel.send(f'「{yomi}」を漢字で書くと：||{kaki}||')
    await ctx.message.delete()
    
@bot.command(aliases=["eng"])
async def english(ctx,japanese,english):
    """
    英単語テスト対策用コマンドです。
    =eng 日本語　英語　のように使用します。
    """
    await ctx.channel.send(f'「{japanese}」を英語で書くと：||{english}||')
    await ctx.message.delete()
   
@bot.command()
async def wiki(ctx,*,args):
    """
    入力された単語をwikiで調べます。
    """
    result = wikitry.wikipediaSearch(args)
    print(args)
    embed = discord.Embed(title='検索結果',description=result,color=0X98FB98)
    await ctx.send(embed=embed)
    
@bot.command()
async def weather(ctx):
    """
    こしひかり居住区の天気を知ることができます
    """
    result = weather_search()
    word_num = len(result)
    if word_num == 2:
        reply = f'{result[0]}\n{result[1]}'
    elif word_num == 3:
        reply = f'{result[0]}\n{result[1]}\n{result[2]}'
    else:
        reply = 'エラーだよ！'
    embed = discord.Embed(title='★こしひかり居住区の天気★',description=reply,color=0X00BFFF)
    await ctx.send(embed=embed)


    
bot.run(token)

