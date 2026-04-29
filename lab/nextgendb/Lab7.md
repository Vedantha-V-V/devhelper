# Lab-7 Redis

## Step 1: Insert Employee Details

### Commands
```bash
HSET employee:1 Name "John" Department "HR" Position "Manager" Salary 60000
HSET employee:2 Name "Alice" Department "IT" Position "Developer" Salary 70000
HSET employee:3 Name "Bob" Department "HR" Position "Executive" Salary 45000
HSET employee:4 Name "Emma" Department "Finance" Position "Analyst" Salary 55000


SADD department:HR 1 3
SADD department:IT 2
SADD department:Finance 4

ZADD employee_salaries 60000 1 70000 2 45000 3 55000 4
```

## Step 2: Retrieve All Employees in "HR" Department

### Commands
```bash
SMEMBERS department:HR

GET employee:1
GET employee:3
```

## Step 3: List Employees with Salary Above 50000

### Commands
```bash
ZRANGEBYSCORE employee_salaries 50000 +inf

GET employee:1
GET employee:2
GET employee:4
```

## Step 4: Update an Employee's Position

### Commands
```bash
HSET employee:2 "Name":"Alice","Department":"IT","Position":"Senior Developer","Salary":70000

ZADD employee_salaries 70000 2
```