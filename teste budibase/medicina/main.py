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
    
def teste_medicamento(driver):
    print("# TESTE DE INTERFACE MEDICAMENTO")
    xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button"
    xpath_input_medicamento = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
    xpath_input_descricao = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input"
    xpath_botao_salvar = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
    
    try:   
        driver.get("https://serra.budibase.app/app/serra-para-todos#/medicamento")
        sleep(12)
        
        click_btn(driver, xpath_botao_novo, 10)
        input_text(driver, xpath_input_medicamento, "Medicamento de teste")
        input_text(driver, xpath_input_descricao, "Descrição do Medicamento de teste")
        input_text(driver, xpath_input_descricao, "Descrição do Medicamento de teste")
        click_btn(driver, xpath_botao_salvar)
        print(">> O TESTE PASSOU !")
    except:
        print(">> O TESTE FALHOU !")
    
def teste_doenca_cronica(driver):
    print("# TESTE DE INTERFACE DOENÇA CRÔNICA MEDICAMENTO")
    xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button"
    xpath_input_doenca = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
    xpath_input_descricao = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input"
    xpath_botao_salvar = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
    
    try:
        driver.get("https://serra.budibase.app/app/serra-para-todos#/doenca-cronica")
        sleep(12)
        
        click_btn(driver, xpath_botao_novo,10)
        input_text(driver, xpath_input_doenca, "Doença Crônica")
        input_text(driver, xpath_input_descricao, "Descrição Doença Crônica")
        click_btn(driver, xpath_botao_salvar)
        print(">> O TESTE PASSOU !")
    except:
        print(">> O TESTE FALHOU !")
        
def teste_procedimento(driver):
    print("# TESTE DE DOENÇA CRÔNICA MEDICAMENTO")
    xpath_botao_novo = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[3]/button"
    xpath_input_procedimento = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input"
    xpath_input_numero = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/input"
    xpath_input_descricao = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/input"
    xpath_botao_salvar = "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button"
    
    try:
        driver.get("https://serra.budibase.app/app/serra-para-todos#/procedimento")
        sleep(12)
        
        click_btn(driver, xpath_botao_novo, 10)
        input_text(driver, xpath_input_procedimento, "Procedimento Teste")
        input_text(driver, xpath_input_numero, "PROC-000")
        input_text(driver, xpath_input_descricao, "Descrição do Procedimento Teste")
        click_btn(driver, xpath_botao_salvar)
        print(">> O TESTE PASSOU !")
    except:
        print(">> O TESTE FALHOU !")  

def main():
    driver = webdriver.Chrome()
    
    teste_medicamento(driver)
    teste_doenca_cronica(driver)
    teste_procedimento(driver)
    
if __name__ == "__main__":
    main()