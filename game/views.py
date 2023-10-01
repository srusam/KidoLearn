from django.shortcuts import render, HttpResponse


def welcome(request):
    return render(request, 'Welcome2.html')

def language(request):
    return render(request, 'index.html')

def options(request):   
    return render(request, 'options.html')

def optionsh(request):
    return render(request, 'optionshindi.html')

def language(request):
    return render(request, 'language.html')

def levelVege(request):
    context = {'calling_view': 'vegetable'}
    return render(request, 'levels.html', context)


def levelVegeh(request):
    context = {'calling_view': 'vegetable'}
    return render(request, 'levelshindi.html', context)

def levelFlower(request):
    context = {'calling_view': 'flower'}
    return render(request, 'levels.html', context)

def levelFlowerh(request):
    context = {'calling_view': 'flower'}
    return render(request, 'levelshindi.html', context)


def levelFruits(request):
    context = {'calling_view': 'fruits'}
    return render(request, 'levels.html', context)
def levelFruitsh(request):
    context = {'calling_view': 'fruits'}
    return render(request, 'levelshindi.html', context)

def levelshapes(request):
    context = {'calling_view': 'shapes'}
    return render(request, 'levels.html', context)

def levelshapesh(request):
    context = {'calling_view': 'shapes'}
    return render(request, 'levelshindi.html', context)

def levelbirds(request):
    context = {'calling_view': 'birds'}
    return render(request, 'levels.html', context)

def levelbirdsh(request):
    context = {'calling_view': 'birds'}
    return render(request, 'levelshindi.html', context)

def levelcolours(request):
    context = {'calling_view': 'colours'}
    return render(request, 'levels.html', context)
def levelcoloursh(request):
    context = {'calling_view': 'colours'}
    return render(request, 'levelshindi.html', context)

def leveldomestic(request):
    context = {'calling_view': 'domestic'}
    return render(request, 'levels.html', context)
def leveldomestich(request):
    context = {'calling_view': 'domestic'}
    return render(request, 'levelshindi.html', context)

def levelfestivals(request):
    context = {'calling_view': 'festivals'}
    return render(request, 'levels.html', context)
def levelfestivalsh(request):
    context = {'calling_view': 'festivals'}
    return render(request, 'levelshindi.html', context)

def levelseasons(request):
    context = {'calling_view': 'seasons'}
    return render(request, 'levels.html', context)
def levelseasonsh(request):
    context = {'calling_view': 'seasons'}
    return render(request, 'levelshindi.html', context)

def levelwild(request):
    context = {'calling_view': 'wild'}
    return render(request, 'levels.html', context)

def levelnumbers(request):
    context = {'calling_view': 'numbers'}
    return render(request, 'levels.html', context)

def levelvehicles(request):
    context = {'calling_view': 'vehicles'}
    return render(request, 'levels.html', context)

def levelDailyLifeObjects(request):
    context = {'calling_view': 'DailyLife'}
    return render(request, 'levels.html', context)

def levelwildh(request):
    context = {'calling_view': 'wild'}
    return render(request, 'levelshindi.html', context)

def levelnumbersh(request):
    context = {'calling_view': 'numbers'}
    return render(request, 'levelshindi.html', context)

def levelvehiclesh(request):
    context = {'calling_view': 'vehicles'}
    return render(request, 'levelshindi.html', context)

def levelDailyLifeObjectsh(request):
    context = {'calling_view': 'DailyLife'}
    return render(request, 'levelshindi.html', context)


def levelSignsSymbols(request):
    context = {'calling_view': 'SignsSymbols'}
    return render(request, 'levels.html', context)
def levelSignsSymbolsh(request):
    context = {'calling_view': 'SignsSymbols'}
    return render(request, 'levelshindi.html', context)


def levelsports(request):
    context = {'calling_view': 'sports'}
    return render(request, 'levels.html', context)
def levelsportsh(request):
    context = {'calling_view': 'sports'}
    return render(request, 'levelshindi.html', context)

 
# level 1 and level 2

def levelVege1(request):
    return render(request, 'gamearea.html')

def levelVege1h(request):
    return render(request, 'gamearea.html')

def levelVege2(request):
    return render(request, 'veglev2.html')

def levelflower2(request):
    return render(request, 'flowers.html')

def levelflower1(request):
    return render(request, 'flowers_Level1.html')

def levelFruits1(request):
    return render(request, 'fruits_Level1.html')

def levelFruits2(request):
    return render(request, 'fruits.html')

def levelshapes1(request):
    return render(request, 'shapes_Level1.html')

def levelshapes2(request):
    return render(request, 'shapes.html')

def levelbirds1(request):
    return render(request, 'Birds_Level1.html')

def levelbirds2(request):
    return render(request, 'birds.html')

def levelbirds1h(request):
    return render(request, 'level1_Birds_in_Hindi.html')

def levelbirds2h(request):
    return render(request, 'level2_birds_in_Hindi.html')

def levelcolours1(request):
    return render(request, 'Colours_Level1.html')

def levelcolours2(request):
    return render(request, 'colours.html')

def levelcolours1h(request):
    return render(request, 'level1_Colors_in_Hindi.html')

def levelcolours2h(request):
    return render(request, 'level2_colors_hindi.html')

def leveldomestic1(request):
    return render(request, 'Domestic_Level1.html')

def leveldomestic2(request):
    return render(request, 'Domestic.html')

def leveldomestic1h(request):
    return render(request, 'level1_Domestic_in_Hindi.html')

def leveldomestic2h(request):
    return render(request, 'level2_domestic_in_Hindi.html')

def levelfestivals1(request):
    return render(request, 'festivals_Level1.html')

def levelfestivals2(request):
    return render(request, 'festivals.html')

def levelfestivals1h(request):
    return render(request, 'level1_Festivals_in_Hindi.html')

def levelfestivals2h(request):
    return render(request, 'level2_festivals_hindi.html')

def levelnumbers1(request):
    return render(request, 'numbers_Level1.html')

def levelnumbers2(request):
    return render(request, 'numbers.html')

def levelseasons1(request):
    return render(request, 'Seasons_Level1.html')

def levelseasons2(request):
    return render(request, 'Seasons.html')

def levelwild1(request):
    return render(request, 'Wild_level1.html')

def levelwild2(request):
    return render(request, 'Wild.html')

def levelwild1h(request):
    return render(request, 'level1_Wild_in_Hindi.html')

def levelwild2h(request):
    return render(request, 'level2_Wild_in_Hindi.html')

def levelvehicles1(request):
    return render(request, 'vehicles_Level1.html')

def levelvehicles2(request):
    return render(request, 'vehicles.html')

def levelDailyLifeObjects1(request):
    return render(request, 'daily_life_objects_Level1.html')

def levelDailyLifeObjects2(request):
    return render(request, 'daily_life_objects.html')

def levelDailyLifeObjects1h(request):
    return render(request, 'daily_life_objects_Level1.html')

def levelDailyLifeObjects2h(request):
    return render(request, 'daily_life_objects.html')

def levelSignsSymbols1(request):
    return render(request, 'signs__symbols_Level1.html')

def levelSignsSymbols2(request):
    return render(request, 'signs_&_symbols.html')

def levelSignsSymbols1h(request):
    return render(request, 'level1_signs_symbols_in_Hindi.html')

def levelSignsSymbols2h(request):
    return render(request, 'level2_Signs_Symbols_in_Hindi.html')

def levelsports1(request):
    return render(request, 'sports_Level1.html')

def levelsports2(request):
    return render(request, 'sports.html')

def animaloption(request):
    return render(request, 'Animalsoption.html')

def animaloptionh(request):
    return render(request, 'Animalsoptionh.html')



def win(request):
    return render(request, 'Finalwin.html')

def lost(request):
    return render(request, 'Sorrypage.html')

