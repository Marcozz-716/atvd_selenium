from packaging import version
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Login:
    def logar(self):
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome

        navegador = webdriver.Chrome(service=servico);
        navegador.get("http://localhost:8888/login/")
        navegador.find_element('xpath', '//*[@id="email"]').send_keys("Marcos")
        navegador.find_element('xpath', '//*[@id="password"]').send_keys("12345678")
        navegador.find_element('xpath', '//*[@id="signin"]').click()
        resultado = navegador.find_element('Xpath', '//*[@id="messageFeedback"]').text
        print(resultado)