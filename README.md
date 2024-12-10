# exam-container-web-service
# **Exam Container Web Service**

**Project Structure**

``` 
exam-container-web-service/
│
├── api-gateway/                     # API Gateway logic
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── database-service/                # Database Service logic
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── checksum-service/                # Checksum logic
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── docker-compose.yml               # Configuration for Docker Compose
├── .gitignore                        # Git ignore file
├── data/                             # Persistent database storage
├── README.md                         # Documentation
```

Command to start up
```
docker-compose up --build
```

Takes a string as input and calculates its sha256 show the result
```
POST http://localhost:5050/compute-checksum
-H "Content-Type: application/json"
-d '{"string": "tester", "algorithm": "sha512"}'
```
```
curl http://localhost:5050/list-checksums
```

To try another algorithm change sha512 to sha256
```
POST http://localhost:5050/compute-checksum
-H "Content-Type: application/json"
-d '{"string": "tester", "algorithm": "sha256"}'
```

To check if Data must sustain a container update (Stop and rerun container) thn show the result
```
sudo docker compose down --remove-orphans
sudo docker compose up --build -d
curl http://localhost:5050/list-checksums
```


     




