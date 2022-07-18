from clases import cliente_classic
from clases import cliente_gold
from clases import cliente_black
from scripts.creacion_html import generate_html

cliente_class = cliente_classic.Classic()
cliente_gold = cliente_gold.Gold()
cliente_black = cliente_black.Black()

generate_html(cliente_class, cliente_gold, cliente_black)
