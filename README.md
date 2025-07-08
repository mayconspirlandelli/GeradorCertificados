# GeradorCertificados
Gerador e Enviador Automático de Certificados com Python

# 🧾 Gerador e Enviador Automático de Certificados com Python, SVG, CrewAI e Gmail API

Este projeto automatiza a **geração personalizada de certificados em PDF** a partir de um **template SVG**, e envia os certificados por **e-mail com a Gmail API**. Ele utiliza a biblioteca **CrewAI** para orquestrar o processo com um agente inteligente.

---

## 🚀 Funcionalidades

- 📄 Geração automática de certificados em PDF a partir de um arquivo SVG com tags personalizadas (`<<nome>>`, `<<horas>>`, `<<texto do certificado>>`)
- 📬 Envio de e-mails personalizados com o certificado em anexo usando a API do Gmail
- 🧠 Uso do CrewAI para gerenciar as etapas como um agente
- 📊 Entrada via arquivo CSV contendo os dados de cada participante

---

## 📁 Estrutura dos Arquivos
📂 projeto-certificados/
├── certificados.csv # Lista com nomes, emails, horas e textos
├── certificado_template.svg # Template do certificado em SVG com tags
├── certificados/ # Pasta de saída com PDFs gerados
├── token.json # Token de autenticação do Gmail
├── credentials.json # Credenciais da API do Gmail
└── main.py # Script principal com CrewAI


---

## 🖼️ Exemplo de Template SVG

O template SVG deve conter as seguintes tags que serão substituídas automaticamente:

```xml
<text x="100" y="200"><<nome>></text>
<text x="100" y="250"><<horas>></text>
<text x="100" y="300"><<texto do certificado>></text>

📑 Exemplo de CSV (certificados.csv)

nome,email,horas,texto
Maria da Silva,maria@email.com,20,Participou do evento sobre IA.
João Pereira,joao@email.com,15,Colaborou com as atividades do congresso.

🛠️ Requisitos
Python 3.8+
Conta Gmail com API ativada
As seguintes bibliotecas:
pip install crewai pandas   x


