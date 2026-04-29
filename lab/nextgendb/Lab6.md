# Lab-6: Redis

## Step 1: Sample Data Insertion

### Commands
```bash
docker run --name redis-server -p 6379:6379 -d redis
docker exec -it redis-server redis-cli
HSET product:1 Name "Smartphone" Category "Electronics" Price 800
HSET product:2 Name "Headphones" Category "Electronics" Price 600
HSET product:3 Name "Shoes" Category "Fashion" Price:1200
HSET product:4 Name "Watch" Category "Accessories" Price 700

SADD category:Electronics 101 102
SADD category:Fashion 103
SADD category:Accessories 104

ZADD price_index 900 101
ZADD price_index 700 102
ZADD price_index 800 103
ZADD price_index 1200 104
```

## Step 2: Retrieve details of a specific product by ProductID

### Commands
```bash
HGETALL product:1
```

## Step 3: Fetch all products belonging to a specific category (Electronics)

### Commands
```bash
SMEMBERS category:Electronics

HGETALL product:1
HGETALL product:2
```

## Step 4: List products in a price range (500 – 1000)

### Commands
```bash
ZRANGEBYSCORE product_prices 500 1000
```

## Step 5: Update Product Price

### Commands
```bash
HSET product:1 Price 950

ZADD price_index 950 1
```

## Step 7: Delete a Product

### Commands
```bash
DEL product:1

SREM category:Electronics 1
ZREM price_index 1
```