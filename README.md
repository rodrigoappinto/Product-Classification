# Product Classification Project

The objective of this project was to develop a Machine Learning model to do Product Classification from Amazon products and make it available through HTTP request.

Unfortunately, there is no way of sharing my pre-trained models and pre-trained dataset through git. Thus, I kindly request you to place the following [data](https://drive.google.com/file/d/1ja0R-7MAyO1FTG4XRi2TA_PIbt61Bp6g/view?usp=drive_link) folder inside the root folder of project and also the ´´´data/models´´´ folder inside of the fastapi app root folder.

Thanks for understanding :)

## Dataset
### Observations

From the provided dataset it was clear that most of it columns were composed of text-based data. Thus, it was initially implied that a model specialized in text classification was the best approach to the problem.

### Decisions

For the preprocessing of the dataset size (1.2M records), it was important to be able to process and analyze data with ease locally, thus, the dataset was sampled to 10%. However, given that there is some class unbalancing for a few classes (run notebooks/data_analysis.ipynb notebook to check the plot) it was important to perform this sampling class wise, therefore the data was grouped by class and 10% of the records of each class was chosen to make it up for the final dataset.

Additionally, a new column was created by merging the selected features (Title, Brand, Description, feature) separated by the [SEP] tag to match the DistilBERT input. This was then used as the training data of the model.

## Model
### Decisions

It was important to choose a model that was not only light, in order to perform inference at ease, but at the same time accurate enough to be able to achieve good results. 

The decision was clear, using a BERT-like model was a good initial approach to the problem. The first instict was to use a lighter version of the original BERT model developed by Google, **DistilBERT**.

However, BERT-like models are design to predict words that are hidden within a [MASK] tag and not for multi-class classification. Thus, several steps had to be taken:

1. Change the architecture to allow for multi-class classification by including a linear and softmax layer at the end of the base DistilBERT.
    
    -  The Linear layer allowed the model to map the output of the DistilBERT model into the desired number of classes.
    - The Softmax layer allows to convert the outputs of the Linear layer into probabilities.

2. Freeze the original BERT parameters, so that training does not interfere with BERT initial pre-trained knowledge.

3. Train the new added multi-class classification layers on the Amazon Product Classification data.

### Observations

After some training, the model reached an Accuracy of 78.59%, a Precision of 75.10%, a Recall of 78.59%, an F1 score of 76.29% in the testing dataset. 
Although not much training was performed, this model was still able to achieve very good results in a task of multi-classification, demonstrating its amazing text context understanding capabilities. However, there are some important things I would like to highlight:

- There was some class unbalancing, thus it would be important to tackle this problem (such as creating dummy data by using techniques such as SMOTE) to improve the dataset quality.

- Some feature engineering could have been done to swaps some of the features used for training and predictions.

- A better approach could be used to fill out the missing values in the dataset.

- The few number of epochs for training (due to low resources) might impact the model performance.

- Some hyperparameter tuning, such as increase the max number of tokens or increase and decrease LR and BS, could have been made in order to improve the model performance.

- The lenghty inputs given the size of some descriptions and features might surpass the model contextual understanding of the sentences and lose records information.

- The contextual window could have been increased to take into account more context of the input.

- Unfreeze some or even all DistilBERT initial parameter in order to make it adapt to the dataset.

### Aditional Notes:

- As said earlier, there is still a lot to explore in order to improve model quality, however despite all this, DistilBERT has shown to be a very easy model to be worked with, and given that someday I might have more time and resources to play around with this model it will definitely be a model that I will have in consideration. 


## Model Benefits and Downsides

### Benefits:

1. Given that we are using an HTTP endpoint to get a classification from the model, it is important for it to give a response promptly and DistilBERT is able to provide that at a much higher rate than the base BERT without losing much more of its original accuracy.

2. Given the time restriction of the project and the lack of resources to train a complex model, it was important to have a model that could be trained relatively fast. DistilBERT accomplishes that perfectly.

### Downsides:

1. As a pre-trained model, and given that it has less parameters than the base BERT model, it is important to note that the model has limited knowledge, which might mitigate it performance in smaller datasets.

2. The model does not have the best long-range dependencies, making it possible to lose information when the text inputs are lenghty.


## Project Organization

This project is split into two different sections, the Notebook section and the HTTP Endpoint section:

- The Notebook section is where all the analysis and experiments are performed. These include the initial analysis and filtering of the dataset, and the model training (that is later swapped to a .py file for ease of running).
    
    - This workflow allows me to initially speed up the iteration and debugging process by running each cell one by one to perform specific tasks and make small changes on stuff that needs to be changed.

- The HTTP endpoint section is where the final code, that is going to eventually make it into production, is placed. This allows me to completly separate the iterative testing code from the final and current productionized solution that is acessible through an endpoint, for which was chosen FastAPI.  


## Running Project with Docker

- To run the HTTP API image please follow the instructions inside the ```/fastapi/README.md```.

- To run the training image please:
    
    1. Create the docker image: ```docker build --platform linux/amd64 . -t product-categorization-training```

    2. Run the docker image: ```docker run -it --platform linux/amd64 product-categorization-training```

        2.1. If you want the model to appear locally after training please add the flag to link the volumes the docker container volume to the local volume (ex. ```-v /data/models:/product_categorization_training/data/models product-categorization-training```)
