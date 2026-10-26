
# Answers

## 1. Service discovery
My app connects to Redis using the name redis on port 6379. Docker Compose lets services find each other by their service names on its network. On the default docker run network, containers generally cannot find each other by name in the same way.

## 2. Stateless app and persistent data
The app is stateless because the counter is stored in Redis , not in the app container. while the database is stateful because it stores data in a volume. After removing and recreating the app, the counter stayed the same. It also survived docker compose down, but reset after docker compose down -v because the Redis volume was deleted.

## 3. Database password and Git
A database password should come from an environment variable or a secrets manager. It should not be committed to Git because someone could access or copy it even from a private repository. My Redis setup doesn't require a password, so I didn't use one.

## AI assistant disclosure
I used an AI assistant to understand Docker Compose,I tested the commands and reviewed the code to understand how the services communicate.
