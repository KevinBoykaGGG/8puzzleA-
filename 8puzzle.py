class Nodo:
    def __init__(self,data,level,fval):
        """ se inicializa el nodo con el dato, nivel del nodo y el valor de fvalor"""
        self.data = data
        self.level = level
        self.fval = fval

    def generar_hijos(self):
        """ Generar los nodos hijos desde el nodo dado moviendo el espacio en blanco
            ya sea en las cuatro direcciones {up,down,left,right} """
        x,y = self.encontrar(self.data,'_')
        """ val_list contiene valores de posición para mover el espacio en blanco en cualquiera de
            las 4 direcciones [up,down,left,right]"""
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        hijos = []
        for i in val_list:
            hijo = self.shuffle(self.data,x,y,i[0],i[1])
            if hijo is not None:
                nodo_hijo = Nodo(hijo,self.level+1,0)
                hijos.append(nodo_hijo)
        return hijos
        
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Mueve el espacio en blanco en la dirección dada y si el valor de posición está fuera
            de límites el retorno es  Ninguno """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            

    def copy(self,root):
        """ Copiar función para crear una matriz similar del nodo dado"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def encontrar(self,puz,x):
        """ Se utiliza específicamente para encontrar la posición del espacio en blanco """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,size):
        """ Inicialice el tamaño del puzzle por el tamaño especificado, listas abiertas y cerradas para vaciar """
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        """ Acepta el puzzle del usuario """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,start,goal):
        """ Función heurística para calcular el valor huerístico f (x) = h (x) + g (x)"""
        return self.h(start.data,goal)+start.level

    def h(self,start,goal):
        """ Calcula la diferencia entre los puzzles dados """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
        

    def process(self):
        """ acepta el estado del puzzle de inicio y objetivo"""
        print("Ingresar el estado inicial del puzzle \n")
        start = self.accept()
        print("Ingresar el estado final del puzzle \n")        
        goal = self.accept()

        start = Nodo(start,0,0)
        start.fval = self.f(start,goal)
        """ Pongo el nodo de inicio en la lista abierta"""
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            """ Si la diferencia entre el nodo actual y el objetivo es 0, hemos alcanzado el nodo objetivo."""
            if(self.h(cur.data,goal) == 0):
                break
            for i in cur.generar_hijos():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            """ ordenar la lista de apertura según el valor de f """
            self.open.sort(key = lambda x:x.fval,reverse=False)


puz = Puzzle(3)
puz.process()