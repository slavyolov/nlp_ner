# # Remove text before ! sign
#
# # for i in okolo:
# #     print(i[0])
# #
#
# # spacy.explain("PRODUCT")
# # 'Objects, vehicles, foods, etc. (not services)'
# # import spacy
# # from spacy import displacy
# #
# # NER = spacy.load("en_core_web_sm")
# #
# # raw_text="The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
# # text1= NER(raw_text)
# #
# # for word in text1.ents:
# #     print(word.text, word.label_)
#
#
# # Annotated text :
#
# TRAIN_DATA = [
#     (self.input_df["texts"][0],
#     {"entities": [(111, 120, "Product"), (140, 150, "Product")]}
# )]
#         # "id": 2,
#         # "label": [
#         #     {
#         #         "start": 111,
#         #         "end": 120,
#         #         "text": "Furniture",
#         #         "labels": [
#         #             "Product"
#         #         ]
#         #     },
#         #     {
#         #         "start": 140,
#         #         "end": 150,
#         #         "text": "Bed Frames",
#         #         "labels": [
#         #             "Product"
#         #         ]
#         #     }
#         # ],
#         # "annotator": 1,
#         # "annotation_id": 1,
#         # "created_at": "2023-11-03T23:26:04.487203Z",
#         # "updated_at": "2023-11-03T23:26:04.487231Z",
#         # "lead_time": 145.324
#     # }
# # ]
#
# from pathlib import Path
# # Define our variables
# model = None
# output_dir = Path("/Users/syol07091/PycharmProjects/nlp_ner/data/output") # to be model
# n_iter = 100
#
# import spacy
# if model is not None:
#     nlp1 = spacy.load(model)  # load existing spaCy model
#     print("Loaded model '%s'" % model)
# else:
#     nlp1 = spacy.blank('en')  # create blank Language class
#     print("Created blank 'en' model")
#
# # create the built-in pipeline components and add them to the pipeline
# # nlp.create_pipe works for built-ins that are registered with spaCy
# if 'ner' not in nlp1.pipe_names:
#     # ner = nlp1.create_pipe('ner')
#     # nlp1.add_pipe(ner, last=True)
#     nlp1.add_pipe('ner')
# # otherwise, get it so we can add labels
# else:
#     ner = nlp1.get_pipe('ner')
#
# import random
# # add labels
# for _, annotations in TRAIN_DATA:
#     for ent in annotations.get('entities'):
#         # nlp1.add_label(ent[2])
#         ner.add_label(ent[2])
#
# other_pipes = [pipe for pipe in nlp1.pipe_names if pipe != 'ner']
# with nlp1.disable_pipes(*other_pipes):  # only train NER
#     optimizer = nlp1.begin_training()
#     for itn in range(n_iter):
#         random.shuffle(TRAIN_DATA)
#         losses = {}
#         examples = []
#         for text, annotations in tqdm(TRAIN_DATA):
#             from spacy.training.example import Example
#             example = Example.from_dict(nlp1.make_doc(text), annotations)
#             examples.append(example)
#             # nlp1.update(
#             #     [text],  # batch of texts
#             #     [annotations],  # batch of annotations
#             #     drop=0.5,  # dropout - make it harder to memorise data
#             #     sgd=optimizer,  # callable to update weights
#             #     losses=losses)
#             print(losses)
#
# nlp1.update(examples, drop=0.5, losses={})
#
# # test the trained model
# for text, _ in TRAIN_DATA:
#     doc = nlp1(text)
#     print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
#
# docsy = spacy.displacy.render(doc, style='ent', jupyter=False)
# with open("/Users/syol07091/PycharmProjects/nlp_ner/data/output/data.html", "w") as file:
#     file.write(docsy)
# # For spaCy v2, the normal way to add an entity ruler looked like this:
# #
# # ruler = EntityRuler(nlp)
# # nlp.add_pipe(ruler)
# # ruler.add_patterns(...)
# # For spaCy v3, you just want to add it with its string name and skip instantiating the class separately:
# #
# # ruler = nlp.add_pipe("entity_ruler")
# # ruler.add_patterns(...)
#
#
# print("Done!")

# NER steps
# During the tokenization stage, the text is split into individual words or phrases.
# Part of speech tagging
# Finally, in the feature extraction stage, the model extracts relevant features such as the surrounding words, the position of the word within the sentence, and the part of speech.



# TODO: text lowercsing ?


"~~hey guys, i got this switch up for grabs, the website is my switch patched shows that it is hackable, but i believe the latest update has been applied so may not be hackable anymore? i dont really know.\n\nI had given this to my son last xmass but then he asked for a laptop so in part payment he gave me the switch. under his possession he always had a screen protector in it. It does however have like 3 or 4 small scratches that are not visible while playing. The body overall has normal signs of use like light scratches and what not but nothing crazy. The games included are Smash Ultimate, Mariokart 8 Deluxe and Minecraft. It does have a new pair of joy cons because the old left one the bumper is bad, maybe an easy fix, but didn't bother and just bought another set. The old are included too. The battery seems to be holding a charge just fine. I just dont use it, rather play games on my pc as well.\n\nI do have the original box, and what i think is most of the accessories check pics for all the is included. \n\npictures: https://imgur.com/a/Rr3jRoJ\n\nLooking for 280  locally (HOUSTON- GALVESTON area) \n\nshipped looking for about 300 to cover shipping.  Rather sell locally so sort of firm on the shipped price.~~\n\nSOLD"



# Data annotation :

# xxx = [(m.start(0), m.end(0)) for m in re.finditer('switch', x)]


# https://www.johnsnowlabs.com/using-rules-and-pretrained-models-in-text-annotation-projects-2-3/


[
    "Who is Shaka Khan?",
    {
      "entities":[
        [
          7,
          17,
          "PERSON"
        ]
      ]
    }
  ]


@staticmethod
def _extract_from_url(url: str) -> str:
    """
    Extract full content of a given url

    Args:
        url: url address stored as string

    Returns:
        Extracted text from the url

    """
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    return soup.body.get_text(' ', strip=True)

@staticmethod
def _remove_duplicated_text(text: str) -> str:
    """
    Remove duplicated text.

    Example :
        Raw : She is cute. She is famous
        Returned : She is cute. famous
    Args:
        text:

    Returns:

    """
    text = text.split(" ")
    unique_words = Counter(text)
    return " ".join(unique_words.keys())


@staticmethod
def _get_most_common_words_in_string(text: str):
    return Counter(text.split()).most_common()
