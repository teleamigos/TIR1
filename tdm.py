

class TDM:
    def __init__(self):

        self.entradas=2
        self.mensajes=[]
        """for i in range(0,self.entradas):
            self.mensajes.append("Hola")"""

        self.sync = [0,1,1,0]
        self.uni=32 #bits

    def add_msj(self,msj):
        self.mensajes.append(msj)

    def add_sources(self,ent):
        self.entradas=ent

    def str_to_bit(self,cadena):
        ret=[]
        for c in cadena:
            for i in range(0,8):
                ret.append((ord(c)>>(7-i))&0x01)
                """Corrimiento de la cadena haciendo enmascarado"""

        return ret

    def max_len(self,arr):
        ret=-1
        for a in arr:
            if len(a)>ret:
                ret=len(a)
        return ret

    def padding (self,msj,maxlen):
        """Llena de ceros"""
        for m in msj:
            mlen=len(m)
            for i in range(mlen,maxlen):
                m.append(0)

    def mux(self):
        ret=[]
        msj=[]
        for m in self.mensajes:
            msj.append(self.str_to_bit(m))
        maxim=self.max_len(msj)
        if  (self.max_len(msj)%self.uni !=0):
            maxim += self.uni -self.max_len(msj) % self.uni
        self.padding(msj,maxim)
        i=0
        while i< self.max_len(msj):
            for m in msj:#Recorre la lista
                for j in range(i,i+self.uni):
                    ret.append(m[j])
            for s in self.sync:
                ret.append(s)
            i += self.uni
        return ret
