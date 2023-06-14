# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'), '<h1><br><br><center>SOLUTION SPRINT FASE 5<center></h1><br><br><b>#fiap #10asoo #agoravai<p><img src="https://media.tenor.com/gpgRaDj_ym4AAAAd/acabou-pel%C3%AA.gif" width="172.66" height="97.125">')