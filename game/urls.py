from django.contrib import admin
from django.urls import path, include
from game import views 

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('language', views.language, name="language"),
    path('options', views.options, name="options"),
    path('options/hindi', views.optionsh, name="options"),
    path('levels/vegetables', views.levelVege, name="levelVege"),
    path('levels/hindi/vegetables', views.levelVegeh, name="levelVege"),

    path('vegetables/level2', views.levelVege1, name="levelVege1"),
    path('vegetables/level1', views.levelVege2, name="levelVege2"),
    # path('vegetables/hindi/level2', views.levelVege1h, name="levelVege1"),
    # path('vegetables/hindi/level1', views.levelVege2h, name="levelVege2"),

    path('levels/flowers', views.levelFlower, name="levelflower"),
    path('flowers/level2', views.levelflower2, name="levelflower1"),
    path('flowers/level1', views.levelflower1, name="levelflower1"),
    path('levels/hindi/flowers', views.levelFlowerh, name="levelflower"),
    # path('flowers/hindi/level2', views.levelflower2h, name="levelflower1"),
    # path('flowers/hindi/level1', views.levelflower1h, name="levelflower1"),
    
    path('levels/fruits', views.levelFruits, name="levelFruits"),
    path('fruits/level1', views.levelFruits1, name="levelFruits1"),
    path('fruits/level2', views.levelFruits2, name="levelFruits2"),
    path('levels/hindi/fruits', views.levelFruitsh, name="levelFruits"),
    # path('fruits/hindi/level1', views.levelFruits1h, name="levelFruits1"),
    # path('fruits/hindi/level2', views.levelFruits2h, name="levelFruits2"),

    path('levels/shapes', views.levelshapes, name="levelshapes"),
    path('shapes/level1', views.levelshapes1, name="levelshapes1"),
    path('shapes/level2', views.levelshapes2, name="levelshapes2"),
    path('levels/hindi/shapes', views.levelshapesh, name="levelshapes"),
    # path('shapes/hindi/level1', views.levelshapes1h, name="levelshapes1"),
    # path('shapes/hindi/level2', views.levelshapes2h, name="levelshapes2"),

    path('levels/birds', views.levelbirds, name="levelbirds"),
    path('birds/level1', views.levelbirds1, name="levelbirds1"),
    path('birds/level2', views.levelbirds2, name="levelbirds2"),
    path('levels/hindi/birds', views.levelbirdsh, name="levelbirds"),
    path('birdshindi/level1', views.levelbirds1h, name="levelbirds1"),
    path('birdshindi/level2', views.levelbirds2h, name="levelbirds2"),

    path('levels/colours', views.levelcolours, name="levelcolours"),
    path('colours/level1', views.levelcolours1, name="levelcolours1"),
    path('colours/level2', views.levelcolours2, name="levelcolours2"),
    path('levels/hindi/colours', views.levelcoloursh, name="levelcolours"),
    path('colourshindi/level1', views.levelcolours1h, name="levelcolours1"),
    path('colourshindi/level2', views.levelcolours2h, name="levelcolours2"),

    path('levels/domestic', views.leveldomestic, name="leveldomestic"),
    path('domestic/level1', views.leveldomestic1, name="leveldomestic1"),
    path('domestic/level2', views.leveldomestic2, name="leveldomestic2"),
    path('levels/hindi/domestic', views.leveldomestich, name="leveldomestic"),
    path('domestichindi/level1', views.leveldomestic1h, name="leveldomestic1"),
    path('domestichindi/level2', views.leveldomestic2h, name="leveldomestic2"),

    path('levels/festivals', views.levelfestivals, name="levelfestivals"),
    path('festivals/level1', views.levelfestivals1, name="levelfestivals1"),
    path('festivals/level2', views.levelfestivals2, name="levelfestivals2"),
    path('levels/hindi/festivals', views.levelfestivalsh, name="levelfestivals"),
    path('festivalshindi/level1', views.levelfestivals1h, name="levelfestivals1"),
    path('festivalshindi/level2', views.levelfestivals2h, name="levelfestivals2"),


    path('levels/seasons', views.levelseasons, name="levelseasons"),
    path('seasons/level1', views.levelseasons1, name="levelseasons1"),
    path('seasons/level2', views.levelseasons2, name="levelseasons2"),
    path('levels/hindi/seasons', views.levelseasonsh, name="levelseasons"),
    # path('seasons/hindi/level1', views.levelseasons1h, name="levelseasons1"),
    # path('seasons/hindi/level2', views.levelseasons2h, name="levelseasons2"),
  
  
    path('levels/wild', views.levelwild, name="levelwild"),
    path('wild/level1', views.levelwild1, name="levelwild1"),
    path('wild/level2', views.levelwild2, name="levelwild2"),
    path('levels/hindi/wild', views.levelwildh, name="levelwild"),
    path('wildhindi/level1', views.levelwild1h, name="levelwild1"),
    path('wildhindi/level2', views.levelwild2h, name="levelwild2"),

    path('levels/numbers', views.levelnumbers, name="levelnumbers"),
    path('numbers/level1', views.levelnumbers1, name="levelnumbers1"),
    path('numbers/level2', views.levelnumbers2, name="levelnumbers2"),
    path('levels/hindi/numbers', views.levelnumbersh, name="levelnumbers"),
    # path('numbers/hindi/level1', views.levelnumbers1h, name="levelnumbers1"),
    # path('numbers/hindi/level2', views.levelnumbers2h, name="levelnumbers2"),

    path('levels/vehicles', views.levelvehicles, name="levelvehicles"),
    path('vehicles/level1', views.levelvehicles1, name="levelvehicles1"),
    path('vehicles/level2', views.levelvehicles2, name="levelvehicles2"),
    path('levels/hindi/vehicles', views.levelvehiclesh, name="levelvehicles"),
    # path('vehicles/hindi/level1', views.levelvehicles1h, name="levelvehicles1"),
    # path('vehicles/hindi/level2', views.levelvehicles2h, name="levelvehicles2"),

    path('levels/DailyLifeObjects', views.levelDailyLifeObjects, name="levelDailyLifeObjects"),
    path('DailyLifeObjects/level1', views.levelDailyLifeObjects1, name="levelDailyLifeObjects1"),
    path('DailyLifeObjects/level2', views.levelDailyLifeObjects2, name="levelDailyLifeObjects2"),
    path('levels/hindi/DailyLifeObjects', views.levelDailyLifeObjectsh, name="levelDailyLifeObjects"),
    # path('DailyLifeObjectshindi/level1', views.levelDailyLifeObjects1h, name="levelDailyLifeObjects1"),
    # path('DailyLifeObjectshindi/level2', views.levelDailyLifeObjects2h, name="levelDailyLifeObjects2"),

    path('levels/SignsSymbols', views.levelSignsSymbols, name="SignsSymbols"),
    path('SignsSymbols/level1', views.levelSignsSymbols1, name="SignsSymbols1"),
    path('SignsSymbols/level2', views.levelSignsSymbols2, name="SignsSymbols2"),
    path('levels/hindi/SignsSymbols', views.levelSignsSymbolsh, name="SignsSymbols"),
    path('SignsSymbolshindi/level1', views.levelSignsSymbols1h, name="SignsSymbols1"),
    path('SignsSymbolshindi/level2', views.levelSignsSymbols2h, name="SignsSymbols2"),
    
    path('levels/sports', views.levelsports, name="sports"),
    path('sports/level1', views.levelsports1, name="sports1"),
    path('sports/level2', views.levelsports2, name="sports2"),
    path('levels/hindi/sports', views.levelsportsh, name="sports"),
    # path('sports/hindi/level1', views.levelsports1h, name="sports1"),
    # path('sports/hindi/level2', views.levelsports2h, name="sports2"),
    
    
    path('animaloption', views.animaloption, name="animaloption"),
    path('animaloption/hindi', views.animaloptionh, name="animaloption"),
    
    path('win', views.win, name="Win"),
    path('lost', views.lost, name="lost")
]
