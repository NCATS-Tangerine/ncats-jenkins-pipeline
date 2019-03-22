from kgx import RedSparqlTransformer, PandasTransformer
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

BIOLINK = 'http://w3id.org/biolink/vocab/'

associations = [
    'http://w3id.org/biolink/vocab/GeneToGoTermAssociation',
    'http://w3id.org/biolink/vocab/ChemicalToThingAssociation',
    'http://w3id.org/biolink/vocab/ChemicalToGeneAssociation',
    'http://w3id.org/biolink/vocab/ChemicalToPathwayAssociation',
    'http://w3id.org/biolink/vocab/PairwiseGeneToGeneInteraction',
    'http://w3id.org/biolink/vocab/Association',
    'http://w3id.org/biolink/vocab/meta/mixin',
    'http://w3id.org/biolink/vocab/PairwiseInteractionAssociation',
    'http://w3id.org/biolink/vocab/GeneToThingAssociation',
    'http://w3id.org/biolink/vocab/GeneToGeneAssociation',
    'http://w3id.org/biolink/vocab/TranscriptToGeneRelationship',
    'http://w3id.org/biolink/vocab/GeneToGeneHomologyAssociation',
    'http://w3id.org/biolink/vocab/GenomicSequenceLocalization',
]

t = RedSparqlTransformer()
for association in associations:
    association = association.replace(BIOLINK, 'bl:')
    print('Loading {} edges'.format(association))
    try:
        t.load_edges(association=association, limit=1000)
    except:
        try:
            print('Exception thrown, sleeping and trying again')
            time.sleep(5)
            t.load_edges(association=association, limit=1000)
        except:
            print('Exception thrown again, saving up to just before {}'.format(association))
            break

t.report()

t = PandasTransformer(t)
t.save('results/red.csv')
