from kgx import RedSparqlTransformer, PandasTransformer

t = RedSparqlTransformer()

t.load_edges(limit = 1_000_000)

t.report()

t = PandasTransformer(t)
t.save('results/red.csv')
