from random import randint
from random import choice, choices


abaddon = {'range': False, 'spells': True, 'waganim': True, 'name': 'Абадона'}
alchemist = {'range': False, 'spells': True, 'waganim': True, 'name': 'Алхимика'}
ancientapparition = {'range': True, 'spells': True, 'waganim': True, 'name': 'Апарата'}
antimage = {'range': False, 'spells': True, 'waganim': True, 'name': 'Антимага'}
arcwarden = {'range': True, 'spells': True, 'waganim': True, 'name': 'Арк вардена'}
axe = {'range': False, 'spells': True, 'waganim': True, 'name': 'Акса'}
bane = {'range': True, 'spells': True, 'waganim': True, 'name': 'бэйна'}
batrider = {'range': True, 'spells': True, 'waganim': True, 'name': 'Бэт`райдера'}
beastmaster = {'range': False, 'spells': True, 'waganim': True, 'name': 'Бистмастера'}
bloodseeker = {'range': False, 'spells': True, 'waganim': True, 'name': 'Блудсикера'}
bountyHunter = {'range': False, 'spells': True, 'waganim': True, 'name': 'Баунти хантера'}
brewmaster = {'range': False, 'spells': True, 'waganim': True, 'name': 'Брюмастера'}
bristleback = {'range': False, 'spells': True, 'waganim': True, 'name': 'Бристелбека'}
broodmother = {'range': False, 'spells': True, 'waganim': True, 'name': 'Бруду'}
centaurwarrunner = {'range': False, 'spells': True, 'waganim': True, 'name': 'Кентавра'}
chaosknight = {'range': False, 'spells': True, 'waganim': True, 'name': 'Цка'}
chen = {'range': True, 'spells': True, 'waganim': True, 'name': 'Чена'}
clinkz = {'range': True, 'spells': True, 'waganim': True, 'name': 'Клинкза'}
clockwerk = {'range': False, 'spells': True, 'waganim': True, 'name': 'Клокверка'}
crystalmaiden = {'range': True, 'spells': True, 'waganim': True, 'name': 'Цмку'}
darkseer = {'range': False, 'spells': True, 'waganim': True, 'name': 'Дарк сира'}
darkwillow = {'range': True, 'spells': True, 'waganim': True, 'name': 'Дарк виллоу'}
dawnbreaker = {'range': False, 'spells': True, 'waganim': True, 'name': 'Давнбрейкершу'}
dazzle = {'range': True, 'spells': True, 'waganim': True, 'name': 'Дазла'}
deathprophet = {'range': True, 'spells': True, 'waganim': True, 'name': 'Профку'}
disruptor = {'range': True, 'spells': True, 'waganim': True, 'name': 'Дисраптора'}
doom = {'range': False, 'spells': True, 'waganim': True, 'name': 'Дума'}
dragonknight = {'range': False, 'spells': True, 'waganim': True, 'name': 'Дка'}
drowranger = {'range': True, 'spells': False, 'waganim': True, 'name': 'Траксу'}
earthspirit = {'range': False, 'spells': True, 'waganim': True, 'name': 'Земелю'}
earthshaker = {'range': False, 'spells': True, 'waganim': True, 'name': 'Шейкера'}
eldertitan = {'range': False, 'spells': True, 'waganim': True, 'name': 'Титана'}
emberspirit = {'range': False, 'spells': True, 'waganim': True, 'name': 'Эмбера'}
enchantress = {'range': True, 'spells': False, 'waganim': True, 'name': 'Энчу'}
enigma = {'range': True, 'spells': True, 'waganim': True, 'name': 'Энигму'}
facelessvoid = {'range': False, 'spells': False, 'waganim': True, 'name': 'Фэйслесс войда'}
grimstroke = {'range': True, 'spells': True, 'waganim': True, 'name': 'Грима'}
gyrocopter = {'range': True, 'spells': True, 'waganim': True, 'name': 'Гирокоптера'}
hoodwink = {'range': True, 'spells': True, 'waganim': True, 'name': 'Худвинк'}
huskar = {'range': True, 'spells': True, 'waganim': True, 'name': 'Хускара'}
invoker = {'range': True, 'spells': True, 'waganim': True, 'name': 'Инвокера'}
io = {'range': True, 'spells': True, 'waganim': True, 'name': 'Виспа'}
jakiro = {'range': True, 'spells': True, 'waganim': True, 'name': 'Джакиро'}
juggernaut = {'range': False, 'spells': True, 'waganim': True, 'name': 'Джагернаута'}
keeperofthelight = {'range': True, 'spells': True, 'waganim': True, 'name': 'Котла'}
kunkka = {'range': False, 'spells': True, 'waganim': True, 'name': 'Кунку'}
legioncommander = {'range': False, 'spells': True, 'waganim': True, 'name': 'Легу'}
leshrac = {'range': True, 'spells': True, 'waganim': True, 'name': 'Лешрака'}
lich = {'range': True, 'spells': True, 'waganim': True, 'name': 'Лича'}
lifestealer = {'range': False, 'spells': True, 'waganim': True, 'name': 'Гулю'}
lina = {'range': True, 'spells': True, 'waganim': True, 'name': 'Лину'}
lion = {'range': True, 'spells': True, 'waganim': True, 'name': 'Лиона'}
lonedruid = {'range': False, 'spells': False, 'waganim': True, 'name': 'Лон друида'}
luna = {'range': True, 'spells': True, 'waganim': True, 'name': 'Луну'}
lycan = {'range': False, 'spells': False, 'waganim': True, 'name': 'Ликана'}
magnus = {'range': False, 'spells': True, 'waganim': True, 'name': 'Магнуса'}
marci = {'range': False, 'spells': True, 'waganim': True, 'name': 'Марси'}
mars = {'range': False, 'spells': True, 'waganim': True, 'name': 'Марса'}
medusa = {'range': True, 'spells': True, 'waganim': True, 'name': 'Медузу'}
meepo = {'range': False, 'spells': True, 'waganim': True, 'name': 'Мипо'}
mirana = {'range': True, 'spells': True, 'waganim': True, 'name': 'Мирану'}
monkeyking = {'range': False, 'spells': True, 'waganim': True, 'name': 'Мка'}
morphling = {'range': True, 'spells': True, 'waganim': True, 'name': 'Морфа'}
nagasiren = {'range': False, 'spells': True, 'waganim': True, 'name': 'Нагу'}
naturesprophet = {'range': True, 'spells': True, 'waganim': True, 'name': 'Фуриона'}
necrophos = {'range': True, 'spells': True, 'waganim': True, 'name': 'Некрофоса'}
nightstalker = {'range': False, 'spells': True, 'waganim': True, 'name': 'Нса'}
nyxassassin = {'range': False, 'spells': True, 'waganim': True, 'name': 'Никса'}
ogremagi = {'range': False, 'spells': True, 'waganim': True, 'name': 'Огр мага'}
omniknight = {'range': False, 'spells': True, 'waganim': True, 'name': 'Омника'}
oracle = {'range': True, 'spells': True, 'waganim': True, 'name': 'Оракла'}
outworlddestroyer = {'range': True, 'spells': True, 'waganim': True, 'name': 'Од'}
pangolier = {'range': False, 'spells': True, 'waganim': True, 'name': 'Панго'}
phantomassassin = {'range': False, 'spells': True, 'waganim': True, 'name': 'Мортру'}
phantomlancer = {'range': False, 'spells': True, 'waganim': True, 'name': 'Пла'}
phoenix = {'range': True, 'spells': True, 'waganim': True, 'name': 'Феникса'}
primalbeast = {'range': False, 'spells': True, 'waganim': True, 'name': 'Праймл биста'}
puck = {'range': True, 'spells': True, 'waganim': True, 'name': 'Пака'}
pudge = {'range': False, 'spells': True, 'waganim': True, 'name': 'Пуджа'}
pugna = {'range': True, 'spells': True, 'waganim': True, 'name': 'Пугну'}
queenofpain = {'range': True, 'spells': True, 'waganim': True, 'name': 'Квопу'}
razor = {'range': True, 'spells': True, 'waganim': True, 'name': 'Разора'}
riki = {'range': False, 'spells': True, 'waganim': True, 'name': 'Рики'}
rubick = {'range': True, 'spells': True, 'waganim': True, 'name': 'Рубика'}
sandking = {'range': False, 'spells': True, 'waganim': True, 'name': 'Ска'}
shadowdemon = {'range': True, 'spells': True, 'waganim': True, 'name': 'Шд'}
shadowfiend = {'range': True, 'spells': True, 'waganim': True, 'name': 'Сфа'}
shadowshaman = {'range': True, 'spells': True, 'waganim': True, 'name': 'Шамана'}
silencer = {'range': True, 'spells': True, 'waganim': True, 'name': 'Сало'}
skywrathmage = {'range': True, 'spells': True, 'waganim': True, 'name': 'Скаймага'}
slardar = {'range': False, 'spells': True, 'waganim': True, 'name': 'Слардара'}
slark = {'range': False, 'spells': True, 'waganim': True, 'name': 'Сларка'}
snapfire = {'range': True, 'spells': True, 'waganim': True, 'name': 'Бабку'}
sniper = {'range': True, 'spells': True, 'waganim': True, 'name': 'Снайпера'}
spectre = {'range': False, 'spells': True, 'waganim': True, 'name': 'Спектру'}
spiritbreaker = {'range': False, 'spells': True, 'waganim': True, 'name': 'Бару'}
stormspirit = {'range': True, 'spells': True, 'waganim': True, 'name': 'Шторма'}
sven = {'range': False, 'spells': True, 'waganim': True, 'wshard': True}
techies = {'range': True, 'spells': True, 'waganim': True, 'name': 'Течиса'}
templarassassin = {'range': True, 'spells': True, 'waganim': True, 'name': 'Темпларку'}
terrorblade = {'range': False, 'spells': True, 'waganim': True, 'name': 'Тб'}
tidehunter = {'range': False, 'spells': True, 'waganim': True, 'name': 'Тайда'}
timbersaw = {'range': False, 'spells': True, 'waganim': True, 'name': 'Тимбера'}
tinker = {'range': True, 'spells': True, 'waganim': True, 'name': 'Тинкера'}
tiny = {'range': False, 'spells': True, 'waganim': True, 'name': 'Тини'}
treantprotector = {'range': False, 'spells': True, 'waganim': True, 'name': 'Трента'}
trollwarlord = {'range': False, 'spells': True, 'waganim': True, 'name': 'Тролля'}
tusk = {'range': False, 'spells': True, 'waganim': True, 'name': 'Таска'}
underlord = {'range': False, 'spells': True, 'waganim': True, 'name': 'Андерлорда'}
undying = {'range': False, 'spells': True, 'waganim': True, 'name': 'Андаинга'}
ursa = {'range': False, 'spells': True, 'waganim': True, 'name': 'Урсу'}
vengefulspirit = {'range': True, 'spells': True, 'waganim': True, 'name': 'Венгу'}
venomancer = {'range': True, 'spells': True, 'waganim': True, 'name': 'Веника'}
viper = {'range': True, 'spells': True, 'waganim': True, 'name': 'Вайпера'}
visage = {'range': True, 'spells': True, 'waganim': True, 'name': 'Висажа'}
voidSpirit = {'range': False, 'spells': True, 'waganim': True, 'name': 'Войд спирита'}
warlock = {'range': True, 'spells': True, 'waganim': True, 'name': 'Варлока'}
weaver = {'range': True, 'spells': True, 'waganim': True, 'name': 'Вивера'}
windranger = {'range': True, 'spells': True, 'waganim': True, 'name': 'Врку'}
winterwyvern = {'range': True, 'spells': True, 'waganim': True, 'name': 'Виверну'}
witchdoctor = {'range': True, 'spells': True, 'waganim': True, 'name': 'Вд'}
wraithking = {'range': False, 'spells': True, 'waganim': True, 'name': 'Вк'}
zeus = {'range': True, 'spells': True, 'waganim': True, 'name': 'Зевса'}
yaroslavpudovkin = {'range': False, 'spells': True, 'waganim': True, 'name': 'Вк'}
Heroes = [abaddon, alchemist, ancientapparition, antimage, arcwarden, axe, bane, batrider, beastmaster, bloodseeker,
          bountyHunter, brewmaster, bristleback, broodmother, centaurwarrunner, chaosknight, chen, clinkz, clockwerk,
          crystalmaiden, darkseer, darkwillow, dawnbreaker, dazzle, deathprophet, disruptor, doom, dragonknight,
          drowranger, earthspirit, earthshaker, eldertitan, emberspirit, enchantress, enigma, facelessvoid,
          grimstroke, gyrocopter, hoodwink, huskar, invoker, io, jakiro, juggernaut, keeperofthelight, kunkka,
          legioncommander, leshrac, lich, lifestealer, lina, lion, lonedruid, luna, lycan, magnus, marci, mars,
          medusa, meepo, mirana, monkeyking, morphling, nagasiren, naturesprophet, necrophos, nightstalker,
          nyxassassin, ogremagi, omniknight, oracle, outworlddestroyer, pangolier, phantomassassin, phantomlancer,
          phoenix, primalbeast, puck, pudge, pugna, queenofpain, razor, riki, rubick, sandking, shadowdemon,
          shadowfiend, shadowshaman, silencer, skywrathmage, slardar, slark, snapfire, sniper, spectre,
          spiritbreaker, stormspirit, sven, techies, templarassassin, terrorblade, tidehunter, timbersaw, tinker,
          tiny, treantprotector, trollwarlord, tusk, underlord, undying, ursa, vengefulspirit, venomancer, viper,
          visage, voidSpirit, warlock, weaver, windranger, winterwyvern, witchdoctor, wraithking, zeus, yaroslavpudovkin]
linepr = ['Wraith_Band', 'Null_Talisman', 'Bracer']
lineprs = ['Morbid_Mask', 'Magic_Wand', 'Soul_Ring', 'Ring_of_Basilius', 'Orb_of_Corrosion']
boots = ['Tranquil_Boots', 'Boots_of_Speed', 'Phase_Boots', 'Power_Treads', 'Boots_of_Travel', 'Arcane_Boots']
rdfarm = ['Hand_of_Midas', 'Mask_of_Madness', 'Armlet_of_Mordiggian', 'Dragon_Lance', 'Falcon_Blade']
mdfarm = ['Hand_of_Midas', 'Mask_of_Madness', 'Armlet_of_Mordiggian', 'Echo_Sabre', 'Falcon_Blade']
ffarm = ['Battle_Fury', 'Maelstrom', 'Radiance']
nffarm = ['Diffusal_Blade', 'Armlet_of_Mordiggian', 'Witch_Blade', 'Crystalys', 'Blade_Mail', 'Hood_of_Defiance',
          'Vanguard', 'Moon_Shard', 'Manta_Style', 'Linkens_Sphere', 'Skull_Basher', 'Helm_of_the_Dominator', 'Urn_of_Shadows', 'Medallion_of_Courage']
esc = ['Shadow_Blade', 'Blink_Dagger', 'Force_Staff']
mfarm = ['Aether_Lens', 'Kaya', 'Witch_Blade', 'Hand_of_Midas']
nmfarm = ['Aghanim_Scepter', 'Linkens_Sphere', 'Orchid_Malevolence', 'Solar_Crest', 'Rod_of_Atos',
          'Euls_Scepter_of_Divinity', 'Veil_of_Discord', 'Urn_of_Shadows', 'Drum_of_Endurance']
ofi = ['Black_King_Bar', 'Silver_Edge', 'Nullifier', 'Desolator', 'Bloodthorn', 'Daedalus', 'Heart_of_Tarrasque', 'Aghanim_Scepter',
       'Butterfly', 'Hurricane_Pike', 'Eye_of_Skadi', 'Shiva_Guard', 'Abyssal_Blade', 'Ethereal_Blade', 'Assault_Cuirass', 'Gleipnir', 'Sange_and_Yasha', 'Kaya_and_Sange']
omi = ['Black_King_Bar', 'Dagon', 'Aghanim_Scepter', 'Refresher_Orb', 'Scythe_of_Vyse', 'Bloodstone',
       'Heart_of_Tarrasque', 'Octarine_Core', 'Revenants_Brooch', 'Wind_Waker', 'Yasha_and_Kaya', 'Gleipnir', 'Kaya_and_Sange']
items = ''
i20 = [0, 0, 0, 0, 1]
i10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
Bnames = {'buy0': ['Сапог:', 'Подкрадули:', 'Сапожек:'], 'buy1': ['Баим на лайне:', 'Покупаем до 15:', 'На начало:'], 'buy2': ['Деремся и фармим:', 'Купить обязательно:'],
          'buy3': ['Лэйт:', 'Лэйтуля:', 'Уничтожаем:'], 'buy4': ['Добираем:', 'Докупаем:', 'Нагибать с этим:'], 'buy5': ['Фармим:', 'Докупаем:', 'Фармим с этим:']}


def createbuild(hero):
    try:
        hero = hero.replace(' ', '').replace('-', '').lower()
        her = hero
        hero = Heroes[Heroes.index(globals().get(hero))]
    except:
        return None
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    n1 = 0
    n2 = 0
    n2 = 0
    n4 = 0
    mage = False
    farm = False
    if hero['spells'] == True:
        if randint(0, 1) == 1:
            mage = True
    if randint(0, 1) == 1:
        farm = True
    p1 = choice(Bnames['buy1'])
    items = ((choice(linepr) + ' ') * randint(1, 3)).split() + list(set(choices(lineprs, k=2)))
    items.sort()
    n1 = items[:-1]
    p2 = choice(Bnames['buy0'])
    n2 = [choice(boots)]
    if mage == True and farm == True:
        p3 = choice(Bnames['buy2'])
        items = [choice(mfarm)]
        if choice(i20) == 1:
            items += [choice(esc)]
        n3 = list(set(items))
        n3.sort()
        p4 = choice(Bnames['buy3'])
        n4 = choices(omi, k=randint(3, 5))
        n4
        n4 = list(reversed(n4))
    elif mage == True and farm == False:
        p3 = choice(Bnames['buy4'])
        items = [choice(nmfarm)]
        if choice(i20) == 1:
            items += [choice(esc)]
        n3 = list(set(items))
        n3.sort()
        p4 = choice(Bnames['buy3'])
        n4 = choices(omi, k=randint(3, 5))
    elif mage == False and farm == False:
        p3 = choice(Bnames['buy4'])
        items = choices(nffarm, k=2)
        if choice(i20) == 1:
            items += [choice(esc)]
        n3 = list(set(items))
        n3.sort()
        p4 = choice(Bnames['buy3'])
        n4 = choices(ofi, k=randint(3, 5))
    elif mage == False and farm == True:
        p3 = choice(Bnames['buy5'])
        if hero['range'] == False:
            items = [choice(ffarm)] + [choice(nffarm) * randint(0, 1)] + [choice(mdfarm) * choice(i20)] + [choice(esc) * choice(i10)]
            items = items[:3]
            items = list(set(items))
            items.sort()
            n3 = list(reversed(items))
        else:
            items = [choice(ffarm)] + [choice(nffarm) * randint(0, 1)] + [choice(rdfarm) * choice(i20)] + [choice(esc) * choice(i10)]
            items = items[:3]
            items = list(set(items))
            items.sort()
            n3 = list(reversed(items))
        p4 = choice(Bnames['buy3'])
        n4 = choices(ofi, k=randint(3, 5))
    return(her, p1, n1, p2, n2, p3, n3, p4, n4)


def trans(a):
    return f"ico/{a}_icon.png"
 
 
def trans1(a):
    return f"her/{a}.png"
