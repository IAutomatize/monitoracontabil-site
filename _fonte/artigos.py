# -*- coding: utf-8 -*-
"""
A LISTA — a ordem daqui é a ordem do índice e a que define o "Leia também"
(cada artigo aponta para os dois seguintes, circularmente). Mexer na ordem muda
os dois; é de propósito, para não existir uma segunda lista de curadoria para
manter em dia.
"""
from artigos_juridico import JURIDICO
from artigos_gestao import GESTAO

ARTIGOS = JURIDICO + GESTAO
