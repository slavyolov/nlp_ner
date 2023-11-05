# nlp_ner
 Named entity recognition

# Target : create NER for Product
definition of product (Google): an article or substance that is manufactured or refined for sale.

### App flow training (this can be organized in a DAG in a production process)
- The jobs directory contains the executable files for the given tasks 
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

# Explain the solution :

Named Entity Recognition is a standard NLP task that can identify entities discussed in a text document.

For the given task, the spaCy has selected as a framework for training customer NER. This is needed because the 
pre-trained NER are not always completely accurate for the domain we are dealing with. Our aim is to take a pretrained model (the one from spaCy)
and update it with newer examples (our urls). To make this work we usually provide many training examples so that our
NER can learn and generalize well when future samples are seen.

**The first step is to extract the text from the URls**. An attempt to get only the visible content from the web pages is 
implemented, and it yielded better result than taking all data. Second some basic text processing steps were done :
- remove html tags
- remove intervals
- remove urls
- remove special characters
- replacement of multiple intervals with a single one

Second major task is to **annotate** the data we want to use for training. I did fetch the text from 150 urls but 53 texts 
were scrapped due to different errors (e.g. 403, 404, 502). The 53 sites were manually annotated. For a demo this is ok
but if we aim to put a system in production we need more examples and better labeling. Usually this part of the process
can be outsourced to accomplished vendors that have technological competence, and dedicated time (also the developers
can spend the time to build and test the system and when they get the annotations just to trigger the training using production instead of development data.

Only the PRODUCT tag was used for the annotation and the following tool was used https://tecoholic.github.io/ner-annotator/
The tool was selected because it gets the data in the expected from spaCy format. Example :

("Chair, You can sit on it!", {"entities": [(0, 5, "PRODUCT")]})

**Model training**, it is important to train only the relevant component (e.g. NER). To train a ner model, the model has 
to be looped over the data for sufficient number of iterations. The more the better but there is a trade-off (more 
iterations require more resources and time to complete). Before every iteration it iss a good practice to shuffle the 
data randomly. This will ensure the model does not make generalizations based on the order of the examples. 
Another typical process is to do the training in batches (please note that for the current demo this is 
omitted due to the low number of sample passed). When doing the training a dropout of 0.3 is selected. THe idea here is 
to force the algorithm to forget as we are setting at random 30 % of the data to 0.
At each word, the update() makes a prediction. It then checks with the annotations  if the prediction is right.
If not, it adjusts the weights so that the correct action will score higher next time. The idea is to minimize a loss 
function

**Model prediction**, after training the model is stored to the filestore. It is then called on out of sample data 
(the remaining data points) and predictions were stored in a list. The list contains the url and the recognized entities
As expected, the model does not perform well but this can be expected considering the above. The purpose of the 
established pipeline is to serve as a demo and to display what can be achieved. Therefore, these results should be 
considered as a baseline, and they can be significantly improved. In practice the performance
must be validated using annotated dataset and performance between prediction and ground truth can be made using classification
metrics (f1-score, recall and precision)