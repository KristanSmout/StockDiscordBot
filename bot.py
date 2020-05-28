import discord,lxml
import yfinance as yf
from discord.ext import commands
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyCodes


Bot = commands.Bot(command_prefix = '!')
C = CurrencyRates()
B = BtcConverter()
Currency = CurrencyCodes()



@Bot.event
async def on_ready():
    print("Investment Bot Is Ready!")
    
@Bot.command(brief='Check if the bot is running',description='This is a command designed to check the bot is able to read messages and run commands')
async def ping(ctx):
    await ctx.send('Pong!')

@Bot.command(brief='Show custom command list',description='Custom command viewer for the bot')
async def commands(ctx):
    PublicCommands = [\
        '!ping','| Check the bot is alive'\
        '!dividend','| Provide dividend ex-date and payment ammount (Local Currency)'\
        '!opinion','| Provide a general conses on company'\
        '!sus','| Check the enviromentak sustainability of a company'\
            ]
    await ctx.send('These are the current commands \n No information provided as a result of this bot is advise')
    print(PublicCommands)

@Bot.command(brief='Show excahnge rates for a specific currency',description='This command allows a range of currencies to be shown for the equivilent of 1 of the selected currency')
async def exchangerate(ctx,arg):
    arg = arg.upper()
    CList = C.get_rates(arg)
    FakeCList = str(CList)
    FakeCList = FakeCList.split('{')
    #print(FakeCList[1])
    FakeCList = FakeCList[1]
    FakeCList = FakeCList.split(',')
    Printout = '``` '
    i = 0
    for item in FakeCList:
        Printout = Printout + FakeCList[i] + ' \n'
        i = i + 1
    Printout = Printout + '```'
    Printout = Printout.replace("'","")
    Printout = Printout.replace("}","")
    await ctx.send(Printout)
    
    #CList = FakeCList.split(',')
    #await ctx.send(CList)

@Bot.command(brief='Compare two currencies',description = 'Compare the direct value of two currencies')
async def exchange(ctx,arg1,arg2):
    arg1 = arg1.upper()
    arg2 = arg2.upper()
    
    if(arg1 == 'BTC' or arg2 == 'BTC'):
        
        if(arg1 == 'BTC'):
            Value = B.get_latest_price(arg2)
            await ctx.send('```' + '1 BTC = ' + str(Value) + ' ' + arg2 + '```')
        else:
            if(arg2 == 'BTC'):
                Value = B.convert_to_btc(1,arg1)
                await ctx.send('```' + '1 ' + arg1 + ' = ' + str(Value) + arg2 + '```')
            else:
                print('IDK')
    else:
    
        Answer = C.get_rate(arg1,arg2)
        Total = Answer
        await ctx.send('``` ' + '1 ' + arg1 + ' = ' + str(Total) + ' ' + arg2 + '```')
    

@Bot.command(brief='Check for free share codes',description = 'This command will allow you to see any codes that can provide free shares')
async def freeshare(ctx):
    await ctx.send('If your account is less than 1 week old you can use the code' + '```' + "DIVEX" + '```')

@Bot.command(brief='Check company sustainability report',description='This command will give you a list of ecological sustainability ratings for the company')
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

@Bot.command(brief='Check latest ex date and dividend payout',description = 'Check the latest ex date for company and see how much each share will produce as a dividend (Local Currency)')
async def dividend(ctx, arg):
    try:
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
    except:
        await ctx.send('```diff\n - No Dividend Found```') 

@Bot.command(brief='See analyst opinions',description='Check the latest analyst reports on a specific company')
async def opinion (ctx, arg):

    LocalTicker = yf.Ticker(str(arg))
    TempVar = (str(LocalTicker.recommendations))
    FakeVar = TempVar.split('\n')

    Source1 = FakeVar[len(FakeVar) - 7]
    Source2 = FakeVar[len(FakeVar) - 6]
    Source3 = FakeVar[len(FakeVar) - 5]
    Source4 = FakeVar[len(FakeVar) - 4]
    Source5 = FakeVar[len(FakeVar) - 3]

    Source1 = Source1.split('  ')
    Source2 = Source2.split('  ')
    Source3 = Source3.split('  ')
    Source4 = Source4.split('  ')
    Source5 = Source5.split('  ')

    #Opinion 1
    RefinedSource1 = (' '.join(Source1).split())
    del RefinedSource1[0]
    del RefinedSource1[0]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source1Opinion = RefinedSource1[(len(RefinedSource1) - 1)]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source1Name = ''.join([str(x) + ' ' for x in RefinedSource1])
    Source1Gap = (20 - len(Source1Name))

    #opinon 2
    RefinedSource1 = (' '.join(Source2).split())
    del RefinedSource1[0]
    del RefinedSource1[0]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source2Opinion = RefinedSource1[(len(RefinedSource1) - 1)]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source2Name = ''.join([str(x) + ' ' for x in RefinedSource1])
    Source2Gap = (20 - len(Source2Name))

    #opinon 3
    RefinedSource1 = (' '.join(Source3).split())
    del RefinedSource1[0]
    del RefinedSource1[0]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source3Opinion = RefinedSource1[(len(RefinedSource1) - 1)]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source3Name = ''.join([str(x) + ' ' for x in RefinedSource1])
    Source3Gap = (20 - len(Source3Name))

    #opinon 4
    RefinedSource1 = (' '.join(Source4).split())
    del RefinedSource1[0]
    del RefinedSource1[0]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source4Opinion = RefinedSource1[(len(RefinedSource1) - 1)]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source4Name = ''.join([str(x) + ' ' for x in RefinedSource1])
    Source4Gap = (20 - len(Source4Name))

    #opinon 5
    RefinedSource1 = (' '.join(Source5).split())
    del RefinedSource1[0]
    del RefinedSource1[0]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source5Opinion = RefinedSource1[(len(RefinedSource1) - 1)]
    del RefinedSource1[(len(RefinedSource1) - 1)]
    Source5Name = ''.join([str(x) + ' ' for x in RefinedSource1])
    Source5Gap = (20 - len(Source5Name))

    Source1 = Source1Name + (' '*Source1Gap + Source1Opinion) + '\n'
    Source2 = Source2Name + (' '*Source2Gap + Source2Opinion) + '\n'
    Source3 = Source3Name + (' '*Source3Gap + Source3Opinion) + '\n'
    Source4 = Source4Name + (' '*Source4Gap + Source4Opinion) + '\n'
    Source5 = Source5Name + (' '*Source5Gap + Source5Opinion) + '\n'

    TitleText = '   Company   ' + '         ' + 'Opinion\n'

    FinalString = '```' + TitleText + Source1 + Source2 + Source3 + Source4 + Source5 + '```'
    await ctx.send(arg)
    await ctx.send(FinalString)

@Bot.command(brief='Get currency symbol',description='Get the symbol of the specified currency')
async def symbol(ctx, arg):
    arg = arg.upper()
    if(arg != 'BTC'):
        Symbol = Currency.get_symbol(arg)
        await ctx.send('```' + str(arg) + ' is denoted as ' + Symbol + '```')
    else:
        Symbol = B.get_symbol()
        await ctx.send('```' + 'Bitcoin is denoted as ' + Symbol + '```')

###BITCOIN STUFF###


Token = open('Token.txt', 'r').read()
Bot.run(Token)
