import discord
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')

@bot.command('help')
async def command_help(ctx:commands.Context):
    await ctx.send('/plastic'
'/fires'
'/pollution')

@bot.command('info')
async def command_info(ctx:commands.Context):
    await ctx.send('Привет я демонстративный бот который заботиться о природе !')

@bot.command('plastic')
async def command_plastic(ctx):
    await ctx.send('Существует несколько технологий переработки пластика:'
'Первичная переработка включает измельчение, плавление, формование, инъекционное формование и вакуумное формование..'
'Вторичная переработка включает химические процессы, при которых пластиковые отходы подвергаются химическому разложению или превращению в более простые соединения.'
'Затем эти соединения используются при производстве новых пластиков или других продуктов.'
'В результате вторичной переработки пластика могут получаться гранулы, стружка, вторичные сырьевые материалы, энергия, новые изделия из пластика и сырьё для других отраслей.')

@bot.command('fires')
async def command_fires(ctx):
    await ctx.send('Лесные пожары — это стихийное бедствие, представляющее собой неконтролируемое горение лесов и других территорий (горных местностей, степей).'

'Последствия лесных пожаров огромны: разрушаются целые экосистемы, ухудшается экологическая обстановка больших территорий, гибнут люди и животные.'

'Виды лесных пожаров:'

'1.Низовые. Причиной является возгорание лесной подстилки.'

'2.Верховые. Огонь идёт вверх, поднимается по стволу и охватывает крону дерева.'

'3.Подземные (торфяные). Горение идёт в торфяном слое на глубине более 50 см.'

'4.Валежные. Устойчивый вариант низового пожара.'

'5.Пятнистые. Являются одной из стадий верховых пожаров.'

'Если вы видите перед собой в лесу тлеющую лесную подстилку или остатки костра, постарайтесь затушить это любыми доступными средствами. Пламя можно затоптать, залить водой.'

'Если вы видите, что ситуация вышла из-под контроля, и справиться с распространением пламени своими силами не получится, сразу вызывайте службу спасения.')

@bot.command('pollution')
async def command_pollution(ctx):
    await ctx.send('Загрязнение окружающей среды — это поступление в среду нехарактерных для неё веществ, а также превышение естественного уровня веществ и энергии.'

'Загрязнения бывают:'

'1.Природные: например, вулканическая лава и пепел.'

'2.Антропогенные: выхлопные газы, сточные воды и др.'

'По причинам загрязнения выделяют:'

'1.Химическое: попадание чужеродных веществ в почву, воздух и воду.'

'2.Физическое: изменение физических параметров среды.'

'3.Биологическое: попадание в экосистемы нехарактерных для них видов организмов и продуктов их жизнедеятельности.'

'По масштабам воздействия загрязнения бывают:'

'1.Локальное: загрязнение небольшой территории.'

'2.Региональное: охватывает большие территории.'

'3.Глобальное: охватывает всю Землю или большую её часть.')


bot.run("")
