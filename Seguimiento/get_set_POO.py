class SegundaClase:
    
    _variable_protegida = 1
    __variable_privada = 2
    
    def __init__(self) :
    	
    	pass
    	
    	
    




if __name__ == "__main__":
    sc = SegundaClase()
    print(sc._variable_protegida)
    print(sc._SegundaClase__variable_privada)

   
      
class ListadoBebidas:

    def __init__(self):
        self._bebida = 'Test cola'
        self._bebidas_validas = ['Test cola', 'Cerveza']

    @property
    def bebida(self):
        return f'La bebida oficial es {self._bebida}'

    @bebida.setter
    def bebida(self, bebida):
        if bebida in self._bebidas_validas:
            self._bebida = bebida
        else:
            raise ValueError(f'La bebida {bebida} no está en el listado de bebidas válidas')
            
            	

if __name__ == "__main__":
    bebidas = ListadoBebidas()
    print(bebidas.bebida)
    bebidas.bebida = 'Limonada'   
    