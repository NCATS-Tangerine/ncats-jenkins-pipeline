"""
Loads all the turtle files with their required ontologies and transforms them to
json. Then loads all these json files, along with the semmeddb edges.csv and
nodes.csv files, into a single NetworkX graph, and performs `clique_merge` on it.
Finally, saves the resulting NetworkX graph as `clique_merged.csv`
"""
import os

from kgx import ObanRdfTransformer, JsonTransformer, HgncRdfTransformer, RdfOwlTransformer, PandasTransformer
from kgx import clique_merge, make_valid_types

data = {
    'data/hp.owl' : RdfOwlTransformer,
    'data/mondo.owl' : RdfOwlTransformer,
    'data/go.owl' : RdfOwlTransformer,
    'data/so.owl' : RdfOwlTransformer,
    'data/ro.owl' : RdfOwlTransformer,
    'data/geno.owl' : RdfOwlTransformer,

    'data/hgnc.ttl' : HgncRdfTransformer,

    'data/orphanet.ttl' : ObanRdfTransformer,
    'data/hpoa.ttl' : ObanRdfTransformer,
    'data/omim.ttl' : ObanRdfTransformer,
    'data/clinvar.ttl' : ObanRdfTransformer,
}

def change_extention(filename, extention):
    while extention.startswith('.'):
        extention = extention[1:]
    return '{}.{}'.format(filename.split('.', 1)[0], extention)

for filename, constructor in data.items():
    out = change_extention(filename, 'csv.tar')
    if os.path.isfile(out):
        continue
    t = constructor()
    t.parse(filename)
    t = PandasTransformer(t)
    t.save(out)

t = PandasTransformer()

for filename in data.keys():
    filename = change_extention(filename, 'csv.tar')
    t.parse(filename)

t.merge_cliques()
t.clean_categories()

t.save('results/monarch.csv')
