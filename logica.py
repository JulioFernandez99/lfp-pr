import tkinter


class Opciones:
    def __init__(self):
        self.tipo = None
        self.doc = None
        self.file = None
        self.lines = None
        self.data = None
        self.matriz = None
        self.carga_exitosa=None

    def continuar(self):
        return self.carga_exitosa

    def cargar(self, ruta):
        self.tipo = ruta.split('.')
        # print(self.tipo[0])

        if self.tipo[1].lower() == 'csv':
            self.doc = open(f'{ruta}','r',encoding='utf-8')
            self.file = self.doc.read()
            self.doc.close()

            self.lines = self.file.split('\n')

            self.data = [
                ['Codigo', 'Nombre', 'Prerequisitos', 'Obligatorio',
                 'Semestre', 'Creditos', 'Estado'
                 ]
            ]

            for datos in self.lines:
                ar = datos.split(',')
                # ar[2]=ar[2].split(',')
                # print(ar)
                self.data.append(ar)

            self.matriz = []

            #Verifica que no hayan cursos con el mismo nombre
            for f in self.data:
                if f not in self.matriz:
                    self.matriz.append(f)

            #Elimina filas en blanco
            for dt in self.matriz:
                if dt[0] == "":
                    self.matriz.remove(dt)


            # -----------------Borrando filas repetidas----------------------------------
            tm = len(self.matriz)
            f_rep = []
            # Busca si un curso se repide en toda la columna
            for f in range(tm):
                f += 1
                for s in range(tm):
                    s += 2
                    if f < tm and s < tm and s > f:
                        m = self.matriz[f][0].strip()
                        n = self.matriz[s][0].strip()
                        # print(m,n)
                        if m == n:  # and not (mat[s] in f_rep)
                            if self.matriz[f] in self.matriz:
                                f_rep.append(self.matriz[f])

            # Lista de repetidos
            f_Eliminar = []
            for item in f_rep:
                if item not in f_Eliminar:
                    f_Eliminar.append(item)
            # Borrando repetidos
            for dl in f_Eliminar:
                if dl in self.matriz:
                    self.matriz.remove(dl)

            tkinter.messagebox.showinfo(title="Mensaje", message="Documento cargado con exito")
            self.carga_exitosa=True
            # self.mostrarMatriz()
        else:
            tkinter.messagebox.showerror(title="Error de carga",
                                         message="Documento con el formato incorrecto")
            self.carga_exitosa=False

    def mostrarMatriz(self):
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz[0])):
                print(self.matriz[f][c], end=" ")
            print("\n")

    def mostrarCurso(self, codigo):
        for fila in self.matriz:
            if fila[0] == str(codigo):
                return fila
        return False

    def agregarCurso(self, codigo, Nombre, Pre, semestre, opcional, creditos, estado):
        lista = [codigo, Nombre, Pre, semestre, opcional, creditos, estado]
        # self.matriz.append(lista)

        c = 0
        for f in self.matriz:
            if codigo == f[0]:
                self.matriz[c] = lista
                return True
            c += 1

        self.matriz.append(lista)
        return True

    def editarCurso(self, codigo, Nombre, Pre, semestre, opcional, creditos, estado):
        lista = [codigo, Nombre, Pre, semestre, opcional, creditos, estado]
        c = 0
        for i in self.matriz:
            if i[0] == str(codigo):
                self.matriz[c] = lista
                return True
            c += 1

        return False

    def elimiarCurso(self, codigo):
        c = 0
        existe = False
        for i in self.matriz:
            if i[0] == str(codigo):
                existe = True
                self.matriz.pop(c)
                return True
            c += 1
        return False

    def creditosAprobados(self):
        suma = 0
        for cr in self.matriz:
            if cr[6] == "0":
                suma += int(cr[5])
        return suma

    def creditosCursando(self):
        suma = 0
        for cr in self.matriz:
            if cr[6] == "1":
                suma += int(cr[5])
        return suma

    def creditosPendientes(self):
        suma = 0
        for cr in self.matriz:
            if cr[3] == "1":
                suma += int(cr[5])
        return suma

    def creditosHasta(self, semestre):
        suma = 0
        for cr in self.matriz[1:]:
            if int(cr[4]) <= int(semestre):
                suma += int(cr[5])
        return suma

    def creditosSemestre(self,semestre):
        suma=0
        for cr in self.matriz[1:]:
            if int(cr[4])==int(semestre) and (cr[6]=="1" or cr[6]=="0"):
                suma+=int(cr[5])
        return suma


# Borrar comentario de fila 70
#obj = Opciones()
#obj.cargar('C:/Users/Lenovo/Desktop/Lenguajes/Laboratorio/Practica1/docPrueba2.LFP')
# print("Creditos Aprobados: ",obj.creditosAprobados())
# print("Creditos Cursando: ",obj.creditosCursando())
#print("Creditos Pedientes: ",obj.creditosPendientes())
#print("Creditos sem: ",obj.creditosSemestre(8))
#print(obj.creditosHasta(2))
# print(obj.mostrarCurso("071"))
# obj.mostrarMatriz()
# obj.agregarCurso("071","compi 1","","2","0","4","-1")
# if obj.editarCurso("666","cjufer","1;2","2","0","4","23"):
# print("Curso modificado")
# print("------------------")
# print(obj.elimiarCurso("661"))
# obj.mostrarMatriz()
