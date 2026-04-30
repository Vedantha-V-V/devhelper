# DevHelper

## Postgres

```bash
docker start postgres
docker exec -it postgres psql -U postgres
```

## CouchDB

```bash
docker run -d --name mycouchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin123 -p 5984:5984 couchdb
```

## Neo4j

```bash
docker run -d --name neo4j-container -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j
```

## Redis

```bash
docker run --name redis-server -p 6379:6379 -d redis
```