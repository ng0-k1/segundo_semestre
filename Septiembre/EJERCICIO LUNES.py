class Estudiante():

    def __init__(self,notas):
        self.opc= " "
        self.datos=[]
        self.alumno=0
        self.estado=0
        self.codigo=0
        self.notas=notas
        self.promedio=0
        self.lista=[]
        self.nota1 = 0
        
    def ingresar(self,notas=1,suma=0,contador=0):
        self.codigo=int(input("digite el codigo del estudiante : "))
        self.alumno=input("digite el nombre del estudiante : ")
        self.notas=float(input("Ingrese la nota 1 del estudiante: "))
        self.nota1 = float(input('Ingrese la nota 2 del estudiante: '))
        self.lista.append([self.notas, self.nota1])
        suma+=self.nota1+self.notas
        
        
        print('\n')
        if contador==0:
            print("no digito ningun numero ")
        else: 
            self.promedio=suma/contador
        for e in self.lista:
            reg=[self.codigo,self.alumno,self.promedio, self.notas, self.nota1]
            self.datos=self.datos+[reg]
            
    def mostrar(self):
        for i in range(len(self.datos)):
            print(f"Estudiante {i+1}:",self.datos[i][1])
            
    def buscar(self):
        c=int(input("ingrese el código del estudiante: "))
        p=-1;
        for i in range(len(self.datos)):
            if c==self.datos[i][0]:
                p=i
                break   
        if p<0:
            print("estudiante no matriculado")
        else:             
                print("Nombre: ",self.datos[p][1])
                print("Promedio: ",self.datos[p][3])
                
    def matriculados(self):
        n=len(self.datos)
        print("cantidad de matriculados: ", n)
        
    def nota(self):
        c=int(input("ingrese el código del estudiante: "))
        p=-1;
        for i in range(len(self.datos)):
            if c==self.datos[i][0]:
                p=i
                break   
        if p<0:
            print("estudiante no matriculado")
        else:
            print(f'las notas son: {self.datos[p][3]} y {self.datos[p][4]}') 
            
    def promedios(self):
        c=int(input("ingrese el código del estudiante: "))
        p=-1;
        for i in range(len(self.datos)):
            if c==self.datos[i][0]:
                p=i
                break   
        if p<0:
            print("estudiante no matriculado")
        else:
            print(f"Estudiante: {self.datos[p][1]}")
            print(f"Promedio estudiante : {self.datos[p][2]}")
            
    def menu(self):
        estado=0
        while True:
            print()
            print("bienvenido al curso de programación I")
            print('\n')
            print("1) ingresar estudiante ")
            print("2) notas del estudiante ")
            print("3) promedio del estudiante ")
            print("4) lista de estudiantes ")
            print ("5) cantidad de inscritos")
            print ("6) Buscar estudiante ")
            print ("7) salir ")
            print('\n')
            x = input ("elija una opción ")
            print('\n')
            if x=='1':
                self.ingresar()
                estado = 1
            elif x=='2':
                if estado==1:
                    self.nota()
                else:
                    print("no se ingreso el estudiante")
            elif x=='3':
                if estado==1:
                    self.promedios()
                else:
                    print("no se ingreso el nombre o la nota ")
            elif x=='4':
                if estado==1:
                    self.mostrar()
                else:
                    print("no hay estudiantes para ver  ")
            elif x=='5':
                if estado==1:
                    self.matriculados()
                else:
                    print("no hay estudiantes para ver  ")
            elif x=='6':
                if estado==1:
                    self.buscar()
                else:
                    print("no hay estudiantes para ver  ")
            elif x=='7':
                print ("gracias, hasta pronto")
                break
#principal
lista=[]
obj=Estudiante(lista)
obj.menu()
