# Lab-4: Neo4j

## Step 1: Create data

### Commands
```bash
CREATE (u1:User {UserID: 1, Username: "Alice"}),
       (u2:User {UserID: 2, Username: "Bob"}),
       (u3:User {UserID: 3, Username: "Jane"}),
       (u4:User {UserID: 4, Username: "John"}),
       (u5:User {UserID: 5, Username: "Emma"}),
       (u6:User {UserID: 6, Username: "Chris"})

CREATE (u3)-[:FOLLOWS]->(u1),
       (u3)-[:FOLLOWS]->(u2),
       (u4)-[:FOLLOWS]->(u1),
       (u5)-[:FOLLOWS]->(u1),
       (u6)-[:FOLLOWS]->(u2),
       (u4)-[:FOLLOWS]->(u2)
```

## Step 2: Display all users

### Commands
```bash
MATCH (u:User)
RETURN u
```

## Step 3: Display users followed by "Jane"

### Commands
```bash
MATCH (j:User {Username: "Jane"})-[:FOLLOWS]->(u)
RETURN u
```

## Step 4: Display all users in ascending order by Username

### Commands
```bash
MATCH (u:User)
RETURN u
ORDER BY u.Username ASC
```

## Step 5: Find users who follow both "Alice" and "Bob"

### Commands
```bash
MATCH (u)-[:FOLLOWS]->(:User {Username: "Alice"}),
      (u)-[:FOLLOWS]->(:User {Username: "Bob"})
RETURN u
```

## Step 6: Find users with the most number of followers

### Commands
```bash
MATCH (u:User)<-[:FOLLOWS]-(f)
RETURN u, COUNT(f) AS followers
ORDER BY followers DESC
LIMIT 1
```

## Step 7: Display first 5 users

### Commands
```bash
MATCH (u:User)
RETURN u
LIMIT 5
```