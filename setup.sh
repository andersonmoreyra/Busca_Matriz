#!/bin/bash
echo "==========================================="
echo "  Instalador do Projeto CMMS (Linux/Mac) "
echo "==========================================="

echo "[1/4] Criando o ambiente virtual Python..."
python3 -m venv venv

echo "[2/4] Ativando o ambiente virtual..."
source venv/bin/activate

echo "[3/4] Instalando as dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[4/4] Preparando o banco de dados..."
python manage.py migrate

echo "==========================================="
echo "  Tudo pronto!                             "
echo "==========================================="
echo ""
echo "Para testar o sistema, siga as instruções abaixo:"
echo ""
echo "1. Ative o ambiente (se fechar o terminal): source venv/bin/activate"
echo "2. Crie um usuário mestre com o comando:    python manage.py createsuperuser"
echo "3. Inicie o servidor web com o comando:     python manage.py runserver"
echo "4. Abra seu navegador em:                   http://127.0.0.1:8000/"
echo ""