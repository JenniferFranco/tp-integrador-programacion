# Importar la librería Colorama para darle color a la consola
from colorama import init, Fore, Style

#Definimos clase Nodo: representa cada pregunta o diagnostico final del arbol de decision
class Nodo:
    def __init__(self, texto, hijo_si=None, hijo_no=None): 
        self.texto = texto          #texto de la pregunta diagnostico
        self.hijo_si = hijo_si      #rama del arbol en caso de la respuesta "si"
        self.hijo_no = hijo_no      #rama del arbol en caso de la respuesta "no"
        
#Definimos la clase ArbolDeDecision: implementa el arbol binario de decision 
class ArbolDeDecision: 
    def __init__(self):
        
        #Diagnosticos finales (nodos hoja)
        diag_covid = Nodo(f'{Fore.RED}Diagnóstico:{Style.RESET_ALL} ' + 'Caso compatible con COVID-19 moderado o severo. Consulte al médico.')
        diag_posible_covid = Nodo(f'{Fore.YELLOW}Diagnóstico:{Style.RESET_ALL} ' + 'Posible caso de COVID-19. Controle síntomas.')
        diag_covid_poco_probable =Nodo(f'{Fore.YELLOW}Diagnóstico:{Style.RESET_ALL} ' + 'Poco probable que sea COVID-19.')
        diag_no_concluyente = Nodo(f'{Fore.YELLOW}Diagnóstico:{Style.RESET_ALL} ' + 'Síntomas no concluyentes. Controle temperatura y síntomas.')
        diag_posible_resfriado = Nodo(f'{Fore.GREEN}Diagnóstico:{Style.RESET_ALL} ' + 'Posible resfriado común. Siga controlando.')
        
        # Preguntas (nodos intermedios)
        nodo_tos = Nodo('¿Tiene tos seca?', diag_posible_covid, diag_no_concluyente)
        nodo_respiratorio = Nodo('¿Tiene dificultad para respirar?', diag_covid, diag_posible_covid)
        nodo_olfato = Nodo('¿Perdió el olfato?', nodo_respiratorio, nodo_tos)
        nodo_garganta = Nodo('¿Tiene dolor de garganta?', diag_posible_resfriado, diag_covid_poco_probable)
        
        nodo_fiebre = Nodo('¿Tiene fiebre?', nodo_olfato, nodo_garganta)
        
        # Nodo Raiz del árbol
        self.raiz = nodo_fiebre
        
    def iniciar_diag (self):
        nodo_actual = self.raiz #Comienza desde la raiz del arbol 
        #Mientras el Nodo tenga hijos continuara haciendo preguntas
        while nodo_actual.hijo_si or nodo_actual.hijo_no:
            respuesta = input(nodo_actual.texto +  " (si/no): ").strip().lower() 
            #Validar las respuestas del usuario
            while respuesta not in ("si", "no"): 
                print("Por favor, responda 'sí' o 'no'.")
                respuesta = input(nodo_actual.texto + " (si/no): ").strip().lower()
                
            #Avanza al siguiente Nodo segun la respuesta
            if respuesta == "si":
                nodo_actual = nodo_actual.hijo_si 
            else:
                nodo_actual = nodo_actual.hijo_no 

        #Imprime el diagnostico final (Nodo hoja)            
        print("\n" + nodo_actual.texto)

#Programa principal        
print(f"{Fore.CYAN}Sistema Simplificado de Diagnóstico COVID-19\n{Style.RESET_ALL}")
arbol = ArbolDeDecision()
arbol.iniciar_diag()
print(f"\n{Fore.GREEN}Gracias por utilizar el sistema. ¡Cuídese!{Style.RESET_ALL}")