from seleniumbase import SB

# Esse comando abre o navegador, vai no Google e pesquisa
with SB() as sb:
    sb.open("https://google.com")
    sb.type('textarea[name="q"]', "Engenharia UFMG")
    sb.click('input[value="Pesquisa Google"]')
    
    # Espera 5 segundos para você ver o resultado
    sb.sleep(5) 
    print("Sucesso! O robô funcionou.")