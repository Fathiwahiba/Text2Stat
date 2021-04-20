#pip install -U spacy
#spacy.cli.download("en_core_web_sm")
import spacy 
nlp = spacy.load("en_core_web_sm")
text = ("March 26, 2021"
        "Shortlisted candidates will be invited to present their project ideas to a Jury made up of experts who will be in charge of selecting the finalists. "
        "The announcement of the Regional results will be made at the end of the selection. "
        " Presentation of project ideas to the National Selection Jury in April 2021"
        "The Regional finalists will compete against each other to determine the national winners."
        "Thus, they will be invited to present their revised and improved projects to the National Jury. "
        "National Trophy Ceremony in April 2021"
         "The best project ideas will be awarded at the National Trophies ceremony." )
doc = nlp(text)
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
