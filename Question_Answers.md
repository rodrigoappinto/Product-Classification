# Question Answering

### What would you change in your solution if you needed to predict all the categories?

In this case, since I have a single-class prediction for a multi-class problem, the final layer is a linear layer with the number of neurons equal to the number of classes, followed by a softmax to compute the probabilities for each class. The predicted class is then determined using `argmax` to select the class with the highest probability. To further process the predictions, I would need to filter the predictions using a threshold that defines what qualifies as a valid category. After filtering, these categories can be ranked from the most probable to the least probable.

### How would you deploy this API on the cloud?

To deploy my API to the cloud, I would start by uploading the local Docker image of the FastAPI app to AWS Elastic Container Registry (ECR) so that my container images can easily acessible and pulled from it.

Next, I would set up a Kubernetes configuration by creating Deployment, Service, and Ingress YAML files. These would be the definition files that define how Docker containers are created, how they should communicate internally in the cluster and externally to handle incoming requests, and how to expose the application to the internet. Also, I would set up an Horizontal Pod Autoscaling (HPA) in the Deployment YAML to automatically scale the number of pods up or down based on the number of requests being made to the API.

Lastly, I would deploy this application by using AWS Elastic Kubernetes Service (EKS). After applying my YAML files, Kubernetes would deploy the FastAPI application, and in respect to the Ingress setup, the incoming requests would be forwarded to the correct pods, thus enabling efficient handling of API requests.

### If this model was deployed to categorize products without any supervision which metrics would you check to detect data drifting? When would you need to retrain?

In order to monitor a productionized model without any supervision it would require techniques that differ from the classic ML metrics. In the case of this project, since it encapsulates embeddings, a proper metric that could be used would be the distance between the embeddings from the transformer model output and the training data embeddings.

In such cases, this technique can be utilized to create a cluster of embeddings, using K-means or a similar clustering algorithms, from starting training data embeddings. Then, each time there's a new prediction point, its embedding output is added to the cluster and its distance to the average point of the cluster is computed. These compute these distances, techniques such as cosine similarity would work quite well.

Finally, to monitor the drift, a threshold is established for the maximum allowable distance an embedding can have from its assigned cluster. If a given number of new embeddings exceed this threshold, then there is a deviation in the distribution of input data. In such a case, new data should be collected to retrain the model to ensure the maintenance of performance and relevance.