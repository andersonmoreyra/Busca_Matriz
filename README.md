# CMMS - Computerized Maintenance Management System

Este repositório contém o desenvolvimento de um sistema completo de gestão de manutenção (EAM/CMMS). Ele foi desenhado para resolver problemas operacionais, técnicos e administrativos e contempla as regras de negócio de 11 grandes módulos industriais.

O catálogo completo com as 872 funcionalidades idealizadas pode ser encontrado no arquivo `CATALOGO_FUNCIONALIDADES.md`.

## Arquitetura e Módulos já Construídos
O sistema utiliza **Python + Django** e está divido nos seguintes módulos funcionais operando com Banco de Dados Relacional e Proteção CSRF.

- **`assets`**: Gestão de Ativos (Hierarquias, Máquinas, Componentes, Centros de custo).
- **`orders`**: Ordens de Serviço (Solicitações, Tickets, Planejamento de Tarefas).
- **`inventory`**: Almoxarifado (Peças/SKUs, Armazéns e Movimentações).
- **`maintenance_planning`**: Preventivas e Preditivas (Gatilhos de tempo e uso).
- **`purchasing`**: Gestão de Compras (Fornecedores e Pedidos).
- **`personnel`**: Mão de obra (Equipes, Especialidades, Apontamento de horas).
- **`inspections`**: Roteiros e check-lists de calibração.
- **`reliability`**: Confiabilidade e Análise de Causas Raiz (Causas/Modos).
- **`safety`**: Segurança do Trabalho (LOTO / Permissões / NR).
- **`projects`**: Paradas industriais programadas.
- **`documents` & `reports` & `operations`**: Bases de Conhecimento, KPIS (Dashboards) e Indisponibilidade Operacional.
- **`core_web`**: Interface pública para Solicitantes e Dashboard.

---

## 🚀 Como testar e instalar na sua máquina local

Para facilitar a sua vida, nós incluímos scripts de auto-configuração!

### Se você usa Windows:
1. Faça o download/pull do código e extraia na sua máquina.
2. Abra a pasta do projeto e dê dois cliques no arquivo **`setup.bat`** (ou rode ele no prompt de comando).
3. Ele vai instalar tudo automaticamente.

### Se você usa Mac ou Linux:
1. Faça o download/pull do código.
2. Abra o terminal na pasta do projeto.
3. Rode o script de instalação com o comando:
   ```bash
   bash setup.sh
   ```

---

## Entrando no Sistema

Ao final do `setup`, você já terá o banco de dados pronto e os pacotes instalados. Agora basta criar o seu usuário e ligar o servidor.

Abra o terminal com o ambiente ativado (`source venv/bin/activate` ou `venv\Scripts\activate`) e digite:

**1. Crie seu usuário de Administrador:**
```bash
python manage.py createsuperuser
```
*(Digite o nome de usuário, um email se quiser, e a senha mestre. O que você digitar de senha ficará invisível por segurança do terminal, mas está sendo computado).*

**2. Ligue a Aplicação Web:**
```bash
python manage.py runserver
```

**3. Acesse no Navegador!**
- 🌐 **Portal Público (Solicitantes / Dashboards):** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- ⚙️ **Painel Administrativo do CMMS (Backoffice):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

*(Use o usuário que você acabou de criar no passo 1 para fazer login no painel administrativo).*

---

### Execução de Testes
Caso queira verificar a integridade da arquitetura de software, você pode rodar a suíte de testes com o comando `python manage.py test`. Há mais de 30 cenários que testam as ligações entre OS, Ativos e Preventivas.
