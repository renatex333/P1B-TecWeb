# Projeto 1 - Parte B
Por: Renato Laffranchi Falcão

Para iniciar o servidor:

docker run --rm --name pg-docker -e POSTGRES_PASSWORD=escolhaumasenha -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres


