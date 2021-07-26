from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    'http://localhost:3030/ds/sparql')


def get_response_region():
    sparql.setQuery('''
        PREFIX rdf: <http://schema.org/>
        PREFIX morochao:<http://vivoweb.org/ontology/core/>
        PREFIX mo: <http://purl.org/ontology/mo/>
        SELECT ?subject ?predicate ?object
        WHERE {
             ?subject morochao:Publisher ?object
        }

    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres