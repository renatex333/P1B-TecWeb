# Projeto 1 - Parte B
Por: Renato Laffranchi Falcão

Para iniciar o servidor:

Execute o container (no PowerShell)

    docker run --rm --name pg-docker -e POSTGRES_PASSWORD=escolhaumasenha -d -p 5432:543
    
Rode o servidor (no Prompt e no caminho do projeto)

    python manage.py runserver

