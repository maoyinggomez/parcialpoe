import threading
import time

class JuegoDeNumeros:

    def contarPares(self):
        for i in range(1, 11):
            if i % 2 == 0:
                print(f"Par: {i}")
                time.sleep(0.5)

    def contarImpares(self):
        for i in range(1, 11):
            if i % 2 != 0:
                print(f"Impar: {i}")
                time.sleep(0.5)
    
    def iniciar(self):
        hiloPares = threading.Thread(target=self.contarPares)
        hiloImpares = threading.Thread(target=self.contarImpares)
        hiloPares.start()
        hiloImpares.start()
        hiloPares.join()
        hiloImpares.join()
     
juego = JuegoDeNumeros()
juego.iniciar()
print("Conteo finalizado") 