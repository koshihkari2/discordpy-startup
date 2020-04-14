from discord.ext import commands
import os
import traceback
import wikipedia
import wikitry

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']

import random
random_list = ['わかばシューター','もみじシューター','おちばシューター','スプラシューターコラボ','.52ガロン','.96ガロンデコ','シャープマーカー','Ｎ－ＺＡＰ８９','Ｎ－ＺＡＰ８５','プライムシューター','シャープマーカネオ','ボールドマーカーネオ','プロモデラーＲＧ','スプラシューター','.52ガロンデコ','Ｌ3リールガンＤ','ジェットスイーパーカスタム','プライムシューターコラボ','もみじシューター','プロモデラーＭＧ','Ｈ3リールガンチェリー','.96ガロン','ボールドマーカー７','Ｎ－ＺＡＰ８３','Ｌ3リールガン','ジェットスイーパー','Ｈ3リールガンＤ','ボトルガイザー','ボトルガイザーフォイル','スプラシューターベッチュー','プライムシューターベッチュー','Ｌ3リールガンベッチュー','.52ガロンベッチュー','デュアルスイーパー','デュアルスイーパーカスタム','スプラマニューバー','スプラマニューバーコラボ','スパッタリー','ケルビン525','スパッタリー・ヒュー','クアッドホッパーブラック','ケルビン525デコ','クアッドホッパーホワイト','スプラマニューバ－ベッチュー','ケルビン525ベッチュー','スパッタリークリア','スプラスコープ','スクイックリンα','スプラチャージャー','１４式竹筒銃・甲','スクイックリンγ','１４式竹筒銃・丙','スクイックリンβ','１４式竹筒銃・乙','ソイチューバー','スプラチャージャーコラボ','リッター４Ｋ','４Ｋスコープ','リッター４Ｋカスタム','４Ｋスコープカスタム','ソイチューバーカスタム','スプラチャージャーベッチュー','スプラスコープベッチュー','ノヴァブラスターネオ','ロングブラスターカスタム','ホットブラスターカスタム','ノヴァブラスター','ラピッドブラスラー','ロングブラスターネクロ','ホットブラスター','Ｒブラスターエリートデコ','ラピットブラスターデコ','ロングブラスター','クラッシュブラスター','クラッシュブラスターネオ','ノヴァブラスターベッチュー','ラピッドブラスターベッチュー','ダイナモローラー','スプラローラーコラボ','カーボンローラー','ダイナモローラーテスラ','スプラローラー','カーボンローラーデコ','ヴァリアブルローラー','ヴァリアブルローラーフォイル','スプラローラーベッチュー','ダイナモローラーベッチュー','ホクサイ','パブロ','ホクサイ・ヒュー','パーマネントパブロ','パブロ・ヒュー','ホクサイベッチュー','バケットスロッシャー','ヒッセン','スクリュースロッシャー','バケットスロッシャーデコ','バケットスロッシャーソーダ','ヒッセン・ヒュー','スクリュースロッシャーネオ','エクスプロッシャー','オーバーフロッシャー','スクリュースロッシャーベッチュー','エクスプロッシャーカスタム','オーバーフロッシャーデコ','スプラスピナーコラボ','バレルスピナーデコ','ハイドラントカスタム','バレルスピナー','バレルスピナーリミックス','ハイドラント','スプラスピナー','クーゲルシュライバー','ノーチラス４７','クーゲルシュライバー・ヒュー','ノーチラス７９','スプラスピナーベッチュー','パラシェルター','キャンピングシェルター','スパイガジェット','パラシェルターソレーラ','スパイガジェットソレーラ','キャンピングシェルターソレーラ','スパイガジェットベッチュー','キャンピングシェルターカーモ']

syuter_list = random_list[0:33]


@bot.event
async def on_ready():
    CHANNEL_ID = 684761828483792943
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

    
@bot.command()
async def buki(ctx,arg='スベテ'):
    if arg == 'マニューバー':
        await ctx.send(random.choice(random_list[32:46]))
    elif arg == 'シューター':
        await ctx.send(random.choice(random_list[0:32]))
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
async def ma(ctx):
    await ctx.send(random.choice(random_list[33:46]))
    
@bot.command()
async def cya(ctx):
    await ctx.send(random.choice(random_list[46:64]))
    
@bot.command()
async def syu(ctx):
    await ctx.send(random.choice(random_list[0:33]))
    
@bot.command()
async def bu(ctx):
    await ctx.send(random.choice(random_list[64:77]))
    
@bot.command()
async def ro(ctx):
    await ctx.send(random.choice(random_list[77:87]))

@bot.command()
async def hu(ctx):
    await ctx.send(random.choice(random_list[87:93]))
    
@bot.command()
async def sur(ctx):
    await ctx.send(random.choice(random_list[94:106]))
    
@bot.command()
async def sup(ctx):
    await ctx.send(random.choice(random_list[106:118]))
    
@bot.command()
async def ka(ctx):
    await ctx.send(random.choice(random_list[118:]))


@bot.command()
async def kan(ctx,yomi,kaki):
    await ctx.channel.send(f'「{yomi}」を漢字で書くと：||{kaki}||')
    await ctx.message.delete()
    
@bot.command()
async def eng(ctx,japanese,english):
    await ctx.channel.send(f'「{japanese}」を英語で書くと：||{english}||')
    await ctx.message.delete()
   
@bot.command()
async def wiki(ctx,search_word=' '):
    if search_word is not ' ':
        result = wikitry.wikipediaSearch(search_word)
        await ctx.send(result)
    else:
        pass

    
bot.run(token)

