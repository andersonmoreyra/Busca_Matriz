@echo off
echo ===========================================
echo   Instalador do Projeto CMMS (Windows)
echo ===========================================

echo [1/4] Criando o ambiente virtual Python...
python -m venv venv

echo [2/4] Ativando o ambiente virtual...
call venv\Scripts\activate.bat

echo [3/4] Instalando as dependencias...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo [4/4] Preparando o banco de dados...
python manage.py migrate

echo ===========================================
echo   Tudo pronto!
echo ===========================================
echo.
echo Para testar o sistema, siga as instrucoes abaixo:
echo.
echo 1. Se fechar o terminal e abrir de novo, ative o ambiente: venv\Scripts\activate
echo 2. Crie um usuario admin digitando o comando:              python manage.py createsuperuser
echo 3. Inicie o servidor web com o comando:                    python manage.py runserver
echo 4. Abra o seu navegador na seguinte URL:                   http://127.0.0.1:8000/
echo.
pause