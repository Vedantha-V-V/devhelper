# Lab-5: Neo4j

## Step 1: Create Data

### Commands
```bash
CREATE (u1:User {UserID: 1, Username: "John"}),
       (u2:User {UserID: 2, Username: "Alice"}),
       (u3:User {UserID: 3, Username: "Bob"}),
       (u4:User {UserID: 4, Username: "Emma"})

CREATE (m1:Movie {MovieID: 1, Title: "Inception"}),
       (m2:Movie {MovieID: 2, Title: "The Matrix"}),
       (m3:Movie {MovieID: 3, Title: "Interstellar"}),
       (m4:Movie {MovieID: 4, Title: "Titanic"})

CREATE (u1)-[:LIKES]->(m1),
       (u1)-[:LIKES]->(m2),
       (u2)-[:LIKES]->(m1),
       (u2)-[:LIKES]->(m3),
       (u3)-[:LIKES]->(m2),
       (u3)-[:LIKES]->(m1),
       (u4)-[:LIKES]->(m1),
       (u4)-[:LIKES]->(m2)
```

## Step 2: Display all movies liked by user "John"

### Commands
```bash
MATCH (:User {Username: "John"})-[:LIKES]->(m:Movie)
RETURN m
```

## Step 3: Find all users who like the movie "Inception"

### Commands
```bash
MATCH (u:User)-[:LIKES]->(:Movie {Title: "Inception"})
RETURN u
```

## Step 4: Display all movies in ascending order by Title

### Commands
```bash
MATCH (m:Movie)
RETURN m
ORDER BY m.Title ASC
```

## Step 5: Find users who like both "The Matrix" and "Inception"

### Commands
```bash
MATCH (u:User)-[:LIKES]->(:Movie {Title: "The Matrix"}),
      (u)-[:LIKES]->(:Movie {Title: "Inception"})
RETURN u
```

## Step 6: Find the most liked movie

### Commands
```bash
MATCH (m:Movie)<-[:LIKES]-(u:User)
RETURN m, COUNT(u) AS likes
ORDER BY likes DESC
LIMIT 1
```

## Step 7: Display top 5 users who like the most movies

### Commands
```bash
MATCH (u:User)-[:LIKES]->(m:Movie)
RETURN u, COUNT(m) AS totalLikes
ORDER BY totalLikes DESC
LIMIT 5
```