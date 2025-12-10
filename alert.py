import requests
import schedule
import time
import smtplib
from email.mime.text import MIMEText

# CONFIGURAÇÕES
URL = "https://visa.vfsglobal.com/ago/pt/prt/book-an-appointment"

EMAIL_ORIGEM = "engraciadecastro65@gmail.com"
EMAIL_SENHA = "dohqumznsvptcfay"  # senha de app
EMAIL_DESTINO = "engraciadecastro65@gma"


def site_disponivel():
    try:
        r = requests.get(URL, timeout=10)
        return r.status_code == 200
    except:
        return False


def enviar_email(mensagem):
    try:
        msg = MIMEText(mensagem)
        msg["Subject"] = "Alerta - VFS"
        msg["From"] = EMAIL_ORIGEM
        msg["To"] = EMAIL_DESTINO

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ORIGEM, EMAIL_SENHA)
            server.sendmail(EMAIL_ORIGEM, EMAIL_DESTINO, msg.as_string())
    except Exception as e:
        print(f"Erro ao enviar email: {e}")


def verificar():
    if site_disponivel():
        print("Site disponível!")
        enviar_email("O site da VFS está disponível!")
    else:
        print("Site indisponível no momento.")


# Executar a verificação a cada 60 segundos
schedule.every(60).seconds.do(verificar)

print("Monitoramento iniciado...")

while True:
    schedule.run_pending()
    time.sleep(1)






