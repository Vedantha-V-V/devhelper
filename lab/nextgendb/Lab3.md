# Lab-3 CouchDB

## Step 1: Create Database

### Commands
```bash
curl -X PUT http://localhost:5984/library
```

# Step 2: Insert Documents

### Commands
```bash
curl -X POST http://localhost:5984/library 
-H "Content-Type: application/json" 
-d '{"ISBN":"978-0-7432-7356-5","Title":"The Great Gatsby","Author":"F. Scott Fitzgerald","Genre":"Fiction","PublicationYear":1925,"CopiesAvailable":5,"Rating":4.5}'
curl -X POST http://localhost:5984/library 
-H "Content-Type: application/json" 
-d '{"ISBN":"978-0-06-112008-4","Title":"To Kill a Mockingbird","Author":"Harper Lee","Genre":"Fiction","PublicationYear":1960,"CopiesAvailable":3,"Rating":4.8}'
curl -X POST http://localhost:5984/library 
-H "Content-Type: application/json" 
-d '{"ISBN":"978-0-14-028329-7","Title":"1984","Author":"George Orwell","Genre":"Dystopian","PublicationYear":1949,"CopiesAvailable":4,"Rating":4.7}'
curl -X POST http://localhost:5984/library 
-H "Content-Type: application/json" 
-d '{"ISBN":"978-0-7432-7357-2","Title":"Brave New World","Author":"Aldous Huxley","Genre":"Dystopian","PublicationYear":1932,"CopiesAvailable":2,"Rating":4.3}'
curl -X POST http://localhost:5984/library 
-H "Content-Type: application/json" 
-d '{"ISBN":"978-0-06-093546-9","Title":"To Kill a Mockingbird II","Author":"Harper Lee","Genre":"Fiction","PublicationYear":2015,"CopiesAvailable":6,"Rating":4.1}'
curl -X POST http://localhost:5984/library 
-H "Content-Type: application/json" 
-d '{"ISBN":"978-0-7432-7358-9","Title":"Animal Farm","Author":"George Orwell","Genre":"Fiction","PublicationYear":1945,"CopiesAvailable":7,"Rating":4.4}'
```

## Step 3: All Documents

### Commands
```bash
curl -X GET http://localhost:5984/library/_design/library/_view/all_books
```

## Step 4: Genre: Fiction

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/library/_find \
-H "Content-Type: application/json" \
-d '{
    "selector": {
        "Genre":"Fiction"
    }
}'
```

## Step 5: Books Sorted by Title (A-Z)

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/library/_design/library/_index \
-H "Content-Type: application/json" \
-d '{
    "index": {"fields":["Title"]},
    "name" : title-index
    "type":json
}'

curl -X POST http://admin:admin123@localhost:5984/library/_design/library/_find \
-H "Content-Type: application/json" \
-d '{
    "selector": {

    },
    "sort" : [
        { "Title":"asc" }
    ]
}'
```

## Step 6: First 3 Books

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/library/_design/library/_find \
-H "Content-Type: application/json" \
-d '{
    "selector": {

    },
    "limit": 3
}'
```

## Step 8: Display Books 2222 and 3333

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/library/_design/library/_index \
-H "Content-Type: application/json" \
-d '{
    "selector": {

    },
    "ISBN": {
        "$in" : ["2222","3333"]
    }
}'
```

## Step 9: Author of 'The Great Gatsby'

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/library/_design/library/_find \
-H "Content-Type: application/json" \
-d '{
    "selector": {
        "Title": "The Great Gatsby"
    },
    "fields" : ["Author"]
}'
```