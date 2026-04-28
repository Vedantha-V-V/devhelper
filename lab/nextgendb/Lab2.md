# Lab-2 CouchDB

## Step 1: Create database

### Commands
```bash
curl -X PUT http://localhost:5984/studentdb
```

## Step 2: Insert documents

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/studentdb/_bulk_docs
-H "Content-Type: application/json" 
-d '{
  "docs": [
    { "SRN": "S001", "Sname": "Rahul",   "Degree": "BCA", "Sem": 3, "CGPA": 7.8 },
    { "SRN": "S002", "Sname": "Ananya",  "Degree": "BCA", "Sem": 5, "CGPA": 6.5 },
    { "SRN": "S003", "Sname": "Vikram",  "Degree": "MCA", "Sem": 2, "CGPA": 8.2 },
    { "SRN": "S004", "Sname": "Meena",   "Degree": "BCA", "Sem": 1, "CGPA": 5.9 },
    { "SRN": "S005", "Sname": "Suresh",  "Degree": "BSc", "Sem": 4, "CGPA": 7.1 },
    { "SRN": "S006", "Sname": "Priya",   "Degree": "BCA", "Sem": 6, "CGPA": 9.0 },
    { "SRN": "S007", "Sname": "Arjun",   "Degree": "MCA", "Sem": 3, "CGPA": 6.3 },
    { "SRN": "S008", "Sname": "Kavya",   "Degree": "BCA", "Sem": 2, "CGPA": 7.0 },
    { "SRN": "S009", "Sname": "Rohan",   "Degree": "BSc", "Sem": 5, "CGPA": 8.5 },
    { "SRN": "S010", "Sname": "Divya",   "Degree": "BCA", "Sem": 4, "CGPA": 6.8 }
  ]
}'
```

## Step 3: Display all documents

### Commands
```bash
curl -X GET http://admin:admin123@localhost:5984/studentdb/_all_docs
```

## Step 4: All BCA Students

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/studentdb/_find
-H "Content-Type: application/json"
-d '{
  "selector": { "Degree": "BCA" }
}'
```

## Step 5: All students in ascending order by Sname

### Commands
```bash
curl -X PUT http://admin:admin123@localhost:5984/studentdb/_index 
-H "Content-Type: application/json" 
-d '{
  "index": { "fields": ["Sname"] },
  "name": "sname-index",
  "type":"json"
}'

curl -X POST http://admin:admin123@localhost:5984/studentdb/_find
-H "Content-Type: application/json" 
-d '{
  "selector": {},
  "sort": [{ "Sname": "asc" }],
}'
```

## Step 6: First 5 Students

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/studentdb/_find
-H "Content-Type: application/json" 
-d '{
  "selector": {},
  "limit": 5
}'
```

## Step 7: Students 12, 13, 14

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/studentdb/_find
-H "Content-Type: application/json" 
-d '{
  "selector": {
      "SRN" : {
         "$in":[12,13,14]
      }
  }
}
```

## Step 8: Degree of Student "Rahul"

### Commands
```bash
curl -X POST http://admin:admin@localhost:5984/studentdb/_find
-H "Content-Type: application/json" 
-d '{
  "selector": { "Sname": "Rahul" },
  "fields": ["Sname", "Degree"]
}'
```

## Step 9: BCA STUDENTS WITH CGPA > 6 AND < 7.5

### Commands
```bash
curl -X POST http://admin:admin123@localhost:5984/studentdb/_find
-H "Content-Type: application/json" 
-d '{
  "selector": {
    "Degree": "BCA",
    "CGPA": { "$gt": 6, "$lt": 7.5 }
  }
}'
```