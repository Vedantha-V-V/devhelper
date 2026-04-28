# Lab 2: NextGenDB Basics

## Step 1: Start the local database
### Dashboard Tasks

### Commands
```bash
nextgendb start
nextgendb status
```

## Step 2: Create a sample database
### Dashboard Tasks

### Commands
```bash
nextgendb shell
use training
db.createCollection("students")
```

## Step 3: Insert and read data
### Dashboard Tasks

### Commands
```bash
db.students.insertOne({ name: "Asha", course: "nextgendb" })
db.students.find()
```