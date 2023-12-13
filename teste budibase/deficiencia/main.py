from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def click_btn(driver, xpath, timeout=5):
    botao = driver.find_element(By.XPATH, xpath)
    wait = WebDriverWait(driver, timeout=timeout)
    wait.until(lambda x : botao.is_displayed())
    botao.click()
    
def input_text(driver, xpath, text, timeout=5):
    input = driver.find_element(By.XPATH, xpath)
    wait = WebDriverWait(driver, timeout=timeout)
    wait.until(lambda x : input.is_displayed())
    input.send_keys(text)

def teste_categoria_deficiencia(driver):
    xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button"
    xpath_botao_salvar =  "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
    xpath_input_categoria = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"

    try:
        driver.get("https://serra.budibase.app/app/serra-para-todos#/categoria")
        sleep(12)
        
        click_btn(driver, xpath_botao_novo, 10)
        input_text(driver, xpath_input_categoria, "Categoria Teste")
        click_btn(driver, xpath_botao_salvar)
        
        print(">> O TESTE PASSOU !")
    except:
        print(">> O TESTE FALHOU !")  

def teste_deficiencia(driver):
    xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button"
    xpath_botao_salvar =  "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
    xpath_input_deficiencia = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
    xpath_categoria_select = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/button"
    xpath_categoria = "/html/body/div[2]/div/div/div[1]/div/div[5]/div/div/div/ul/li[2]"
        
    try:
        driver.get("https://serra.budibase.app/app/serra-para-todos#/deficiencia")
        sleep(12)
        
        click_btn(driver, xpath_botao_novo, 10)
        input_text(driver, xpath_input_deficiencia, "Deficiência Teste")
        click_btn(driver, xpath_categoria_select, 10)
        sleep(3)
        click_btn(driver, xpath_categoria)
        click_btn(driver, xpath_botao_salvar)
        
        print(">> O TESTE PASSOU !")
    except:
        print(">> O TESTE FALHOU !")  

def main():
    driver = webdriver.Chrome();
    teste_categoria_deficiencia(driver)
    teste_deficiencia(driver)
    
if __name__ == "__main__":
    main()