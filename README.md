
# CENG413 HW-2: Two Services with Docker Compose

Build and start: `docker compose up -d --build`
Check services: `docker compose ps`
Test state: `Invoke-RestMethod -Method Post http://localhost:8080/count/increment`
Read state: `Invoke-RestMethod http://localhost:8080/count`
Stop services: `docker compose down`
