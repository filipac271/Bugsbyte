# 📊 Preço Ideal – 🪲Hackathon BugsByte🪲 

Este projeto foi desenvolvido para a Hackathon BugsByte 25 e segue o tema da **MCSonae**. O objetivo principal é determinar o **preço ideal** para qualquer produto.  

## 🚀 Tecnologias Utilizadas  

- **Backend**: Python (FastAPI, Pandas)  
- **Frontend**: React (TypeScript, Tailwind CSS)  
- **Comunicação**: FastAPI  

## 🛠 Como Rodar o Projeto  

### Backend  

1. Criar e ativar um ambiente virtual:  

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   ```

2. Instalar as dependências:  

   ```bash
   pip install fastapi uvicorn pandas
   ```

3. Rodar o servidor:  

   ```bash
   uvicorn app.main:app --reload --port 8080
   ```

### Frontend  

1. Instalar as dependências:  

   ```bash
   npm install
   ```

2. Iniciar o frontend:  

   ```bash
   npm start
   ```

## 📡 Comunicação Backend ↔ Frontend  

O backend FastAPI fornece APIs que o frontend React consome para obter dados e calcular o **preço ideal** dos produtos e em alguns produtos sugere um **bundle** para aumentar as vendas.  

## 📌 Extra

Para rodar o projeto é necessário os .cvs, caso queira basta contactar-me.


