# CMMS - Computerized Maintenance Management System

Este repositório contém a base para o desenvolvimento de um sistema completo de gestão de manutenção, focado em resolver problemas operacionais, técnicos e administrativos da indústria.

## Arquitetura Inicial
O sistema está sendo construído utilizando Python com o framework Django, escolhido por sua robustez, escalabilidade e velocidade de desenvolvimento. O banco de dados planejado é o PostgreSQL para garantir a integridade dos dados e preparar a aplicação para uma possível estrutura multi-tenant no futuro.

## Estruturação de Módulos (Roadmap)

### Módulo 1: Gestão e Cadastro de Ativos (Atual)
- Hierarquias de ativos (pais, filhos).
- Registro técnico, especificações e vida útil.
- Localizações e posições operacionais.
- Centros de custo e responsáveis.

### Módulos Futuros
- **Módulo 2:** Gestão de solicitações e ordens de serviço.
- **Módulo 3:** Planejamento e estratégias de manutenção preventiva/preditiva.
- **Módulo 4:** Programação, escalonamento e controle da manutenção.
- **Módulo 5:** Execução dos serviços e mobilidade.
- ... e mais.

## Como rodar o projeto
1. Crie um ambiente virtual: `python -m venv venv`
2. Ative o ambiente: `source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt` (a ser criado)
4. Rode as migrações: `python manage.py migrate`
5. Inicialize o servidor: `python manage.py runserver`