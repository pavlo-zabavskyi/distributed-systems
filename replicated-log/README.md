# How to Run

To run the services using Docker Compose, follow these steps:

## Running the Containers
### 1.Build and Start the Containers

#### Starting the Master Node

To build and start the master node, use the following commands:
```
docker build -t master:2.0 .
docker stop master_node
docker rm master_node
docker run --name master_node --network replicated_log -p 8050:8050 master:2.0
Starting Replica Node A
```

To build and start replica node A, use the following commands:
```
docker build -t secondary:2.0 .
docker stop secondary_node_a
docker rm secondary_node_a
docker run --name secondary_node_a --network replicated_log -p 50051:50051 secondary:2.0
Starting Replica Node B
```

To build and start replica node B, use the following commands:
```
docker stop secondary_node_b
docker rm secondary_node_b
docker run --name secondary_node_b --network replicated_log -p 50052:50051 secondary:2.0
```

After the build is complete, you can access the APIs via the following URLs:
* Master API: http://localhost:8050

To get list of messages on secondary use gRPC `GetAllMessages` method. 
