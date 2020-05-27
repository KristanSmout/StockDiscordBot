import discord,lxml
import yfinance as yf
from discord.ext import commands


Bot = commands.Bot(command_prefix = '!')

@Bot.event
async def on_ready():
    print("Investment Bot Is Ready!")
    
@Bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@Bot.command()
async def sus(ctx, arg):
    await ctx.send(arg)
    LocalTicker = yf.Ticker(str(arg))
    TempVar = (str(LocalTicker.sustainability))
    TempStorage = (TempVar.split('\n'))
    Finalstring = '```'
    for line in TempStorage:
        linesplit = line.split(' ')
        ItemTitle = linesplit[0]
        TitleLength = len(ItemTitle)
        SpacerCount = 25 - len(ItemTitle)
        Spacer = (' ' * SpacerCount)
        Value = (len(linesplit) - 1)
        Finalstring = (Finalstring + ItemTitle + '' + Spacer + linesplit[Value] + '\n')
    await ctx.send(Finalstring + '```')

@Bot.command()
async def dividend(ctx, arg):
    await ctx.send(arg)
    LocalTicker = yf.Ticker(str(arg))
    TempVar = (str(LocalTicker.dividends))
    #print(TempVar)
    TempStorage = (TempVar.split('\n'))
    LineFinder = len(TempStorage) - 2
    TempMainLine = TempStorage[LineFinder]
    FinalSplit = TempMainLine.split(' ')
    RealDate = FinalSplit[0].split('-')
    PaymentLen = len(FinalSplit) - 1
    Finalstring = '```'
    Finalstring = Finalstring + 'Ex Date           : ' + RealDate[2] + '/' + RealDate[1] + '/' + RealDate[0] + '\nDividend Payment  : ' + FinalSplit[PaymentLen]
    await ctx.send(Finalstring + '```')

@Bot.command()
async def opinion (ctx, arg):
    await ctx.send(arg)
    LocalTicker = yf.Ticker(str(arg))
    TempVar = (str(LocalTicker.recommendations))
    print(TempVar)
    print('========')
    FakeVar = TempVar.split('\n')
    print(FakeVar)


    Source1 = FakeVar[len(FakeVar) - 7]
    Source2 = FakeVar[len(FakeVar) - 6]
    Source3 = FakeVar[len(FakeVar) - 5]
    Source4 = FakeVar[len(FakeVar) - 4]
    Source5 = FakeVar[len(FakeVar) - 3]

    print('=======')
    print(Source1)
    print(Source2)
    print(Source3)
    print(Source4)
    print(Source5)

    Source1 = Source1.split('  ')
    Source2 = Source2.split('  ')
    Source3 = Source3.split('  ')
    Source4 = Source4.split('  ')
    Source5 = Source5.split('  ')
    print('=============')
    #Work on splitting the text, Remove first two, last one then set new last to the value and all prior to the name
    RefinedSource1 = (' '.join(Source1).split())
    RefinedSource1 = (' '.join(Source1).split()).remove(0)
    RefinedSource1 = (' '.join(Source1).split()).remove(0)
    RefinedSource2 = (' '.join(Source2).split()).pop()
    RefinedSource3 = (' '.join(Source3).split()).pop()
    RefinedSource4 = (' '.join(Source4).split()).pop()
    RefinedSource5 = (' '.join(Source5).split()).pop()

    print(RefinedSource1)



Bot.run('NzE0OTMxNjY1MzY5MzAxMDIz.Xs12JQ.HsTJaT6jtYhT0Rvsupf94rli7y4')
