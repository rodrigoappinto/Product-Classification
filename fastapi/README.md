# FastAPI Initialization

The objective of the FastAPI folder is to encapsulate and isolate the HTTP endpoint from the iterative testing notebooks.

## Steps for Replication

1. If you still do not have the Docker image for this FastAPI app please make sure to build the image.

    1.1. Make sure you have docker installed and running.

    1.2. Create the docker image: ```docker build --platform linux/amd64 . -t product-categorization```

    1.3 Check for the image: ```docker images```

2. In case you already have your image, run it. 
    
    2.1. Run the docker container: ```docker run --platform linux/amd64 -p 8080:8080 product-categorization```
        
    - Note: Make sure to perform port forwarding to access it on your local machine.

3. When the container is running, make sure to access the http endpoint:

    3.1. Follow the link: ```http://0.0.0.0:8080/docs```

Now you should be all set to start requesting!