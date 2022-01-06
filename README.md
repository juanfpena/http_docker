

## Quickstart

Run in any CLI of your choice the followings commands:

```
docker-compose down & docker-compose rm;
docker-compose build;
docker-compose up -d;
docker-compose exec httpserver bash;
python -m create_tables
python -m create_views
python -m table_seeder
```


* For api services go to `localhost:8000`

* For CLI commands specifics refer to readme at `CLI_command/README.md`