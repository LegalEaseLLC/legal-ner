from spacy.symbols import ORTH, LEMMA, POS, TAG

# https://spacy.io/usage/linguistic-features#adding-patterns-attributes

stakeholder = [[{LEMMA: 'Kläger'}],
               [{LEMMA: 'Beklagte'}]]

cause = [[{ORTH: 'weil'}],
         [{ORTH: 'denn'}],
         [{ORTH: 'da'}]]
