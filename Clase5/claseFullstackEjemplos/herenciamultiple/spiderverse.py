from herenciamultiple.spiderdos import SpiderDos
from herenciamultiple.spideruno import SpiderUno


class SpiderVerse(SpiderDos,SpiderUno):

    def __init__(self) -> None:
        print('Soy el spiderman de Tom Holland')

    def hablar(self):
        print('No me quiero ir señor Stark')
