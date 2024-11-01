## How to Run

To run the services using Docker Compose, follow these steps:

### Running the Containers
1. Build and start the containers with the following command:
```
docker-compose up --build
```
This command will:
* Build the Docker images for each service.
* Start the containers for the Master API and the Secondary APIs.

After the build is complete, you can access the APIs via the following URLs:
* Master API: http://localhost:8050

To get list of messages on secondary use gRPC `GetAllMessages` method. 
