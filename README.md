# daw-atividade-Django

# Corrida de Moto

Um sistema de gerenciamento de corridas de moto desenvolvido com Django.

## Descrição

Este projeto é uma aplicação web Django para gerenciar corridas de moto. Ele permite o cadastro de pilotos, motos e corridas, fornecendo uma plataforma para organização e acompanhamento de eventos de motociclismo.

## Funcionalidades

- Cadastro de Pilotos
- Registro de Motos
- Agendamento de Corridas
- Associação de Motos a Pilotos
- Gerenciamento de Participantes em Corridas

## Estrutura do Projeto

- `corrida_de_moto/`: Diretório principal do projeto Django
- `settings.py`: Configurações do projeto
- `urls.py`: Configuração de URLs do projeto
- `wsgi.py` e `asgi.py`: Configurações para deploy
- `gerenciamento/`: Aplicativo principal
- `models.py`: Define os modelos Piloto, Moto e Corrida
- `admin.py`: Configuração do painel administrativo
- `migrations/`: Migrações do banco de dados

## Modelos

- **Piloto**: Armazena informações sobre os pilotos (nome, data de nascimento, nacionalidade)
- **Moto**: Registra detalhes das motos (modelo, marca, cilindrada) e associa a um piloto
- **Corrida**: Gerencia informações sobre as corridas (data, localização) e as motos participantes
