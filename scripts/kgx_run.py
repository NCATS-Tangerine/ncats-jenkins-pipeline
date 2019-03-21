from kgx import ObanRdfTransformer, JsonTransformer, HgncRdfTransformer, PandasTransformer, RdfOwlTransformer
from kgx import clique_merge, make_valid_types

# parse hp.owl
t = RdfOwlTransformer()
t.parse('data/hp.owl')
t = JsonTransformer(t)
t.save('results/hp.json')

# parse mondo.owl
t = RdfOwlTransformer()
t.parse('data/mondo.owl')
t = JsonTransformer(t)
t.save('results/mondo.json')

# parse hgnc.ttl
t = HgncRdfTransformer()
t.parse('data/hgnc.ttl')
t = JsonTransformer(t)
t.save('results/hgnc.json')

# parse hpoa.ttl
t = ObanRdfTransformer()
t.add_ontology('data/mondo.owl')
t.add_ontology('data/hp.owl')
t.parse('data/hpoa.ttl')
t = JsonTransformer(t)
t.save('results/hpoa.json')


t = JsonTransformer()
t.parse('results/hp.json')
t.parse('results/mondo.json')
t.parse('results/hgnc.json')
t.parse('results/hpoa.json')

# clique merge
t.graph = clique_merge(t.graph)
make_valid_types(t.graph)

# save as CSV
csv_transformer = PandasTransformer(t)
csv_transformer.save('results/monarch.csv')
