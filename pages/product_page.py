from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductPage(BasePage):

    # locator
    _nome_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/productTV'}
    _preco_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/priceTV'}
    _origem_x = 927
    _origem_y = 2073
    _destino_x = 967
    _destino_y = 1313
    _red_color = '(//android.widget.ImageView[@content-desc=\"Displays color of product\"])[4]'
    _color_image_view = {'by': AppiumBy.XPATH, 'value': _red_color}
    _aumentar_quantidade = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'Increases number of products'}
    _adicionar_carrinho = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'Tap to add product to cart'}

    # inicialização
    def __init__(self, driver):
        self.driver = driver

    # ações
    # validar o nome e o preço do produto
    def ler_nome(self):
        self._localizar_(self._nome_produto).text
        return self._ler(self._nome_produto)

    def ler_preco_(self):
        return self._ler(self._preco_produto)

    # arrasta para cima
    def arrastar_para_cima_(self):
        self._rolar(
            self._origem_x,
            self._origem_y,
            self._destino_x,
            self._destino_y
        )

    # realizar o fluxo de escolhas da compra
    def como_(self):
        # selecionar a cor da mochila como vermelho
        self._apertar(self._color_image_view)

        # clicar até selecionar a quantidade desejada
        for itens in range(quantidade - 1):
            self._apertar(self._aumentar_quantidade)

        # adicionar produto no carrinho
        self._apertar(self._adicionar_carrinho)
