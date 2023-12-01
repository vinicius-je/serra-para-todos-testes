from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def main():
    driver = webdriver.Chrome()
    driver.get("https://serra.budibase.app/app/serra-para-todos#/deficiencia")

    sleep(12)

    botao_novo = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/button")
    wait = WebDriverWait(driver, timeout=10)
    wait.until(lambda x : botao_novo.is_displayed())
    botao_novo.click()
    
    input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/input")
    wait = WebDriverWait(driver, timeout=5)
    wait.until(lambda x : input.is_displayed())
    input.send_keys("Linguiça")

    botao_salvar = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button")
    wait = WebDriverWait(driver, timeout=5)
    wait.until(lambda x : botao_salvar.is_displayed())
    botao_salvar.click()

if __name__ == "__main__":
    main()