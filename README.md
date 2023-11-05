# nlp_ner
 Named entity recognition

# Target : create NER for Product
definition of product (Google): an article or substance that is manufactured or refined for sale.

### App flow training (this can be organized in a DAG in a production process)

- ```python data_processing_training.py```
- ```python model_training.py```

### App flow for forecasting
- ```python model_forecasting.py```


# Design flow :
## Step 1: Text processing 
## Step 2: Annotation
 - 2.1 annotate the text : https://tecoholic.github.io/ner-annotator/
 - 2.1 : 
   - Open the annotations.json file and remove the first part, where there are the classes.
   - Keep the JSON consistent (remove {} braces ). Save the file.

## Step 3 : Model training
## Step 4 : Predictions (out of sample data)
