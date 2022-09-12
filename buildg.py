from random import randint
from random import choice, choices

Abaddon = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Абадона'}
Alchemist = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Алхимика'}
Ancient_Apparition = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Апарата'}
Anti_Mage = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Антимага'}
Arc_Warden = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Арк вардена'}
Axe = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Акса'}
Bane = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'бэйна'}
Batrider = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Бэтрайдера'}
Beastmaster = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Бистмастера'}
Bloodseeker = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Блудсикера'}
Bounty_Hunter = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Баунти хантера'}
Brewmaster = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Брюмастера'}
Bristleback = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Бристелбека'}
Broodmother = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Бруду'}
Centaur_Warrunner = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Кентавра'}
Chaos_Knight = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Цка'}
Chen = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Чена'}
Clinkz = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Клинкза'}
Clockwerk = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Клокверка'}
Crystal_Maiden = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Цмку'}
Dark_Seer = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Дарк сира'}
Dark_Willow = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Дарк виллоу'}
Dawnbreaker = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Давнбрейкершу'}
Dazzle = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Дазла'}
Death_Prophet = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Профку'}
Disruptor = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Дисраптора'}
Doom = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Дума'}
Dragon_Knight = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Дка'}
Drow_ranger = {'range': True, 'spells': False, 'waganim': True, 'wshard': True, 'name': 'Траксу'}
Earth_Spirit = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Земелю'}
Earthshaker = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Шейкера'}
Elder_Titan = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Титана'}
Ember_Spirit = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Эмбера'}
Enchantress = {'range': True, 'spells': False, 'waganim': True, 'wshard': True, 'name': 'Энчу'}
Enigma = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Энигму'}
Faceless_Void = {'range': False, 'spells': False, 'waganim': True, 'wshard': True, 'name': 'Фэйслесс войда'}
Grimstroke = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Грима'}
Gyrocopter = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Гирокоптера'}
Hoodwink = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Худвинк'}
Huskar = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Хускара'}
Invoker = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Инвокера'}
Io = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Виспа'}
Jakiro = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Джакиро'}
Juggernaut = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Джагернаута'}
Keeper_of_the_Light = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Котла'}
Kunkka = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Кунку'}
Legion_Commander = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Легу'}
Leshrac = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Лешрака'}
Lich = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Лича'}
Lifestealer = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Гулю'}
Lina = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Лину'}
Lion = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Лиона'}
Lone_Druid = {'range': False, 'spells': False, 'waganim': True, 'wshard': True, 'name': 'Лон друида'}
Luna = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Луну'}
Lycan = {'range': False, 'spells': False, 'waganim': True, 'wshard': True, 'name': 'Ликана'}
Magnus = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Магнуса'}
Marci = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Марси'}
Mars = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Марса'}
Medusa = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Медузу'}
Meepo = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Мипо'}
Mirana = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Мирану'}
Monkey_King = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Мка'}
Morphling = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Морфа'}
Naga_Siren = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Нагу'}
Natures_Prophet = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Фуриона'}
Necrophos = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Некрофоса'}
Night_Stalker = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Нса'}
Nyx_Assassin = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Никса'}
Ogre_Magi = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Огр мага'}
Omniknight = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Омника'}
Oracle = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Оракла'}
Outworld_Destroyer = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Од'}
Pangolier = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Панго'}
Phantom_Assassin = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Мортру'}
Phantom_Lancer = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Пла'}
Phoenix = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Феникса'}
Primal_Beast = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Праймл биста'}
Puck = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Пака'}
Pudge = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Пуджа'}
Pugna = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Пугну'}
Queen_of_Pain = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Квопу'}
Razor = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Разора'}
Riki = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Рики'}
Rubick = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Рубика'}
Sand_King = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Ска'}
Shadow_Demon = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Шд'}
Shadow_Fiend = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Сфа'}
Shadow_Shaman = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Шамана'}
Silencer = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Сало'}
Skywrath_Mage = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Скаймага'}
Slardar = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Слардара'}
Slark = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Сларка'}
Snapfire = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Бабку'}
Sniper = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Снайпера'}
Spectre = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Спектру'}
Spirit_Breaker = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Бару'}
Storm_Spirit = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Шторма'}
Sven = {'range': False, 'spells': True, 'waganim': True, 'wshard': True}
Techies = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Течиса'}
Templar_Assassin = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Темпларку'}
Terrorblade = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Тб'}
Tidehunter = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Тайда'}
Timbersaw = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Тимбера'}
Tinker = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Тинкера'}
Tiny = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Тини'}
Treant_Protector = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Трента'}
Troll_Warlord = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Тролля'}
Tusk = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Таска'}
Underlord = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Андерлорда'}
Undying = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Андаинга'}
Ursa = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Урсу'}
Vengeful_Spirit = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Венгу'}
Venomancer = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Веника'}
Viper = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Вайпера'}
Visage = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Висажа'}
Void_Spirit = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Войд спирита'}
Warlock = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Варлока'}
Weaver = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Вивера'}
Windranger = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Врку'}
Winter_Wyvern = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Виверну'}
Witch_Doctor = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Вд'}
Wraith_King = {'range': False, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Вк'}
Zeus = {'range': True, 'spells': True, 'waganim': True, 'wshard': True, 'name': 'Зевса'}


Heroes = [Abaddon, Alchemist, Ancient_Apparition, Anti_Mage, Arc_Warden, Axe, Bane, Batrider, Beastmaster, Bloodseeker, Bounty_Hunter, Brewmaster, Bristleback, Broodmother, Centaur_Warrunner, Chaos_Knight, Chen, Clinkz, Clockwerk, Crystal_Maiden, Dark_Seer, Dark_Willow, Dawnbreaker, Dazzle, Death_Prophet, Disruptor,Doom, Dragon_Knight, Drow_ranger, Earth_Spirit, Earthshaker, Elder_Titan, Ember_Spirit, Enchantress, Enigma, Faceless_Void, Grimstroke, Gyrocopter, Hoodwink, Huskar, Invoker, Io, Jakiro, Juggernaut, Keeper_of_the_Light, Kunkka, Legion_Commander, Leshrac, Lich, Lifestealer, Lina, Lion, Lone_Druid, Luna, Lycan, Magnus, Marci, Mars, Medusa, Meepo, Mirana, Monkey_King, Morphling, Naga_Siren, Natures_Prophet, Necrophos, Night_Stalker, Nyx_Assassin, Ogre_Magi, Omniknight, Oracle, Outworld_Destroyer, Pangolier, Phantom_Assassin, Phantom_Lancer, Phoenix, Primal_Beast, Puck, Pudge, Pugna, Queen_of_Pain, Razor, Riki, Rubick, Sand_King, Shadow_Demon, Shadow_Fiend, Shadow_Shaman, Silencer, Skywrath_Mage, Slardar, Slark, Snapfire, Sniper, Spectre, Spirit_Breaker, Storm_Spirit, Sven, Techies, Templar_Assassin, Terrorblade, Tidehunter,Timbersaw, Tinker, Tiny, Treant_Protector, Troll_Warlord, Tusk, Underlord, Undying, Ursa, Vengeful_Spirit, Venomancer, Viper, Visage, Void_Spirit, Warlock, Weaver, Windranger, Winter_Wyvern, Witch_Doctor, Wraith_King, Zeus]
linepr = ['Wraith band', 'Null talisman', 'Bracer']
lineprs = ['Morbid mask', 'Magic stick', 'Soul ring', 'Ring of Basilis', 'Headtress']
boots = ['Tranquil Boots', 'Boots of speed','Phase Boots', 'Power Treads', 'Boots of Travel','Arcane Boots']
rdfarm = ['Hand of midas', 'Mask of madnes', 'Armlet of moriggan', 'Dragon lance', 'Falcone blade']
mdfarm = ['Hand of midas', 'Mask of madnes', 'Armlet of moriggan', 'Echo sabre', 'Falcone blade']
ffarm = ['Battle Fury', 'Maelstorm', 'Radiance']
nffarm = ['Defusial blade', 'Armlet of moriggan','Witch blade', 'Crystalys ', 'Blademail', 'Hood of defiance', 'Vanguard', 'Moon shard', 'Manta style', 'Linken sphere',]
esc = ['Shadow blade', 'Blink dagger', 'force staff']
mfarm = ['Aether lenth', 'Kaya', 'Witch blade']
nmfarm = ['Aganim sceptre', 'Linken sphere', 'Orchid of Malevolence', 'Falcone blade',
'Euls Scepter of Divinity', 'Veil of Discord']
ofi = ['Black king bar', 'Silver edge', 'Desolator', 'Bloodtorn', 'Daedalus', 'Heart of Tarrasque', 'Aganim sceptre', 'Butterfly', 'Eye of skadi']
omi = ['Black king bar', 'Dagon'  'Aganim sceptre', 'Refresher orb', 'Scythe of Vyse', 'Bloodstone', 'Heart of Tarrasque']
items = ''
def create_build(hero):
	i20 = [0, 0, 0, 0, 1]
	i10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
	mage = False
	magee  = 'физического'
	farm = False
	farmm = 'боевого'
	if hero['spells'] == True:
		if randint(0, 1) == 1:
			mage = True
			magee = "магического"
		if randint(0, 1) == 1:
			farm = True
			farmm = ''
	print('Крутая сборка на', farmm, magee,  hero['name'])
	print(choice(['Баим на лайне:', 'Ультракупи все до 15:']))
	items = ((choice(linepr) + ' ') * randint(0, 3))
	print(items[:-1], *list(set(choices(lineprs, k=2))), choice(boots))
	if mage == True and farm == True:
		print(choice(['Деремся и фармим', 'Купить обязательно']))
		items = choice(mfarm), 'Hand of Midas' * choice(i20), choice(esc) * choice(i20)
		print(*items)
		print(choice(['Лэйт:', 'Лэйтуля:', 'Уничтожаем:']))
		items = choices(omi, k=randint(2,3))
		print(*items)
	elif mage == True and farm == False:
		print(choice(['Добираем:', 'Докупаем:', 'Нагибать с этим:']))
		items = choice(nmfarm), choice(esc) * choice(i20)
		print(*items)
		print('Лэйт:')
		items = choices(omi, k=randint(2,3))
		if 'Aganim sceptre' in items:
			items.remove('Aganim sceptre')
		print(*items)
	elif mage == False and farm == False:
		print(choice(['Добираем:', 'Докупаем:', 'Нагибать с этим:']))
		items = choices(nffarm, k=2), choice(esc) * choice(i20)
		print(*items)
		print(choice(['Лэйт:', 'Лэйтуля:', 'Уничтожаем:']))
		items = choices(ofi, k=randint(2,3))
		print(*items)
	elif mage == False and farm == True:
		print(choice(['Фармим:', 'Докупаем:', 'Фармим с этим']))
		if hero['range'] == False:
			items = choice(nffarm) * randint(0,1), choice(mdfarm) * choice(i20), choice(esc) * choice(i10), choice(ffarm)
			print(*items)
		else:
			items = choice(nffarm) * randint(0,1), choice(rdfarm) * choice(i20), choice(esc) * choice(i10), choice(ffarm)
			print(*items)
		print(choice(['Лэйт:', 'Лэйтуля:', 'Уничтожаем:']))
		items = choices(ofi, k=randint(3,4))
		print(*items)

def get_random_build():
	create_build(choice(Heroes))


print('Выбери одного героя из списка для создания сборки: Abaddon, Alchemist, Ancient_Apparition, Anti_Mage, Arc_Warden, Axe, Bane, Batrider, Beastmaster, Bloodseeker, Bounty_Hunter, Brewmaster, Bristleback, Broodmother, Centaur_Warrunner, Chaos_Knight, Chen, Clinkz, Clockwerk, Crystal_Maiden, Dark_Seer, Dark_Willow, Dawnbreaker, Dazzle, Death_Prophet, Disruptor,Doom, Dragon_Knight, Drow_ranger, Earth_Spirit, Earthshaker, Elder_Titan, Ember_Spirit, Enchantress, Enigma, Faceless_Void, Grimstroke, Gyrocopter, Hoodwink, Huskar, Invoker, Io, Jakiro, Juggernaut, Keeper_of_the_Light, Kunkka, Legion_Commander, Leshrac, Lich, Lifestealer, Lina, Lion, Lone_Druid, Luna, Lycan, Magnus, Marci, Mars, Medusa, Meepo, Mirana, Monkey_King, Morphling, Naga_Siren, Natures_Prophet, Necrophos, Night_Stalker, Nyx_Assassin, Ogre_Magi, Omniknight, Oracle, Outworld_Destroyer, Pangolier, Phantom_Assassin, Phantom_Lancer, Phoenix, Primal_Beast, Puck, Pudge, Pugna, Queen_of_Pain, Razor, Riki, Rubick, Sand_King, Shadow_Demon, Shadow_Fiend, Shadow_Shaman, Silencer, Skywrath_Mage, Slardar, Slark, Snapfire, Sniper, Spectre, Spirit_Breaker, Storm_Spirit, Sven, Techies, Templar_Assassin, Terrorblade, Tidehunter,Timbersaw, Tinker, Tiny, Treant_Protector, Troll_Warlord, Tusk, Underlord, Undying, Ursa, Vengeful_Spirit, Venomancer, Viper, Visage, Void_Spirit, Warlock, Weaver, Windranger, Winter_Wyvern, Witch_Doctor, Wraith_King, Zeus ')
print('-----------------------------------------------------')
print('Далее вставь его название в команду "create_build(Герой)", например create_build(Abaddon) и отправь в кончоль, если хочешь сборку на случайного героя, отправь get_random_build()')	
		
		
