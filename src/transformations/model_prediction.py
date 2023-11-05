def predict(self):
    """
    Predictions using already trained model

    Returns:

    """
    doc = self.nlp("I was driving a Alto")
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])