from crewai import Crew
import pandas as pd
import os
import base64
from email.message import EmailMessage

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import cairosvg  # converter SVG para PDF


# === Função para gerar o certificado a partir do template SVG ===
def gerar_certificado_svg(nome, horas, texto, template_path="certificado_template.svg", output_dir="certificados"):
    os.makedirs(output_dir, exist_ok=True)

    with open(template_path, "r", encoding="utf-8") as f:
        svg_template = f.read()

    # Substituir as tags do SVG
    svg_personalizado = (
        svg_template.replace("<<nome>>", nome)
        .replace("<<horas>>", f"{horas} horas")
        .replace("<<texto do certificado>>", texto)
    )

    # Gerar caminho do arquivo PDF
    nome_arquivo = f"{nome.replace(' ', '_')}.pdf"
    caminho_pdf = os.path.join(output_dir, nome_arquivo)

    # Converter SVG para PDF
    cairosvg.svg2pdf(bytestring=svg_personalizado.encode("utf-8"), write_to=caminho_pdf)
    return caminho_pdf


# === Função para enviar o email via Gmail API ===
def enviar_email(nome, email_destino, pdf_path):
    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/gmail.send"])
    service = build("gmail", "v1", credentials=creds)

    mensagem = EmailMessage()
    mensagem["To"] = email_destino
    mensagem["Subject"] = "Seu Certificado de Participação"
    mensagem.set_content(f"""
Olá, {nome}!

Agradecemos por sua participação no evento. Em anexo, você encontrará seu certificado digital.

Atenciosamente,
Equipe Organizadora
""")

    with open(pdf_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(pdf_path)

    mensagem.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)
    raw_message = base64.urlsafe_b64encode(mensagem.as_bytes()).decode()

    try:
        service.users().messages().send(userId="me", body={"raw": raw_message}).execute()
        print(f"✔️ Email enviado para {email_destino}")
    except HttpError as error:
        print(f"❌ Erro ao enviar email para {email_destino}: {error}")


# === Agente do CrewAI para gerar e enviar certificados ===
class CertificadoAgent:
    def __init__(self, csv_path):
        self.dados = pd.read_csv(csv_path)

    def executar(self):
        for _, linha in self.dados.iterrows():
            nome = linha["nome"]
            email = linha["email"]
            horas = linha["horas"]
            texto = linha["texto"]

            print(f"🔧 Gerando certificado para {nome}...")
            caminho_pdf = gerar_certificado_svg(nome, horas, texto)

            print(f"📤 Enviando email para {email}...")
            enviar_email(nome, email, caminho_pdf)


# === Execução principal com CrewAI ===
if __name__ == "__main__":
    agente_certificados = CertificadoAgent("certificados.csv")
    crew = Crew(agents=[agente_certificados])
    crew.kickoff()
