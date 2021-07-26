import Conecxion as con

def types_command_dbpedia():
    qres = con.get_response_region()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name, ing,  image_url = result['name']['value'], result['res']['value'], result['image']['value']
        mensaje ='Nombre de la pizza : ' + name + " Ingredientes: " + ing +" asdsndoasnoaks " + image_url
        print(mensaje)
       