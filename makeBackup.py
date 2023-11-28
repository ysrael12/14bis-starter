import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from getIp import get_ip_address

def fazerbackup ():
#configuraçao do webdriver
    def configure_driver():
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=options)
        return driver

    driver = configure_driver()

    #entrando na pagina do biblivre
    andress = 'http://{}/Biblivre5/'.format(get_ip_address())
    driver.get(andress)

    #realizando o login na plataforma
    password = driver.find_element(By.NAME, 'password')
    username = driver.find_element(By.NAME, 'username')
    username.send_keys("ysrael.jesus")
    password.send_keys("ysraelop12")
    subbutton = driver.find_element(By.TAG_NAME, 'button')
    subbutton.click()

    #realizando o backup
    driver.get(andress+'?action=administration_maintenance')
    backupBtn = driver.find_element(By.LINK_TEXT, "Gerar backup completo")
    backupBtn.click()

    # Aguardar um tempo antes de fechar o navegador
    time.sleep(60)

    # Fechar o navegador
    driver.quit()