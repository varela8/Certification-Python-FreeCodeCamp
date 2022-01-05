

def arithmetic_arranger (*args):
    entrada = []
    results = False
    for arg in args:
        if arg == False:
            continue
        if arg == True:
            results = True
            continue
        entrada = arg
    
    #Errores de nº argumentos
    if len(entrada) > 5:
        return 'Error: Too many problems.'
        

    #Inicializa variables
    numeradores = []
    signos = []
    denominadores = []
    resultados = []
    n_operaciones = len(entrada)

    #Separa numeradores, denominadores y signos en 3 listas
    for i in entrada:
        nl = i.split(' ')
        numeradores.append(nl[0])
        signos.append(nl[1])
        denominadores.append(nl[2])
    
    #Compruebo que no sean de más de 4 cifras
    for ele in numeradores:
        if len(ele) > 4:
            return 'Error: Numbers cannot be more than four digits.' 
    for ele in denominadores:
        if len(ele) > 4:
            return 'Error: Numbers cannot be more than four digits.' 

 
    #Hago una copia del original 
    ori_numeradores = numeradores.copy()
    ori_denominadores = denominadores.copy()
    ori_signos = signos.copy()


    #Calculo el resultado y activo errores posibles
    for ele in range(n_operaciones):
        if ori_signos[ele] == '+':
            try:
                resultado = int(ori_numeradores[ele])+ int(ori_denominadores[ele])
            except:
                return 'Error: Numbers must only contain digits.'
                
            resultados.append(str(resultado))
            continue
        if ori_signos[ele] == '-':
            try:
                resultado = int(ori_numeradores[ele])- int(ori_denominadores[ele])
            except:
                return'Error: Numbers must only contain digits.'
                
            resultados.append(str(resultado))
            continue
        else:
            return "Error: Operator must be '+' or '-'."
            


    def poner_espacios(argumentos):
        '''Función que agrega los espacios necesarios'''
        for n in range(n_operaciones):                    
            huecos = max(len(ori_numeradores[n]),len(ori_denominadores[n])) + 2
            if argumentos is numeradores:
                espacios = huecos - len(argumentos[n])
            if argumentos is denominadores:
                espacios = huecos - len(argumentos[n])-2
            if argumentos is resultados:
                espacios = huecos - len(argumentos[n])
            argumentos[n] = ' ' * espacios + argumentos[n]
        return argumentos

    poner_espacios(numeradores)
    poner_espacios(denominadores)
    poner_espacios(resultados)

    #Diseño de la salida por pantalla
    top = []
    bottom = []
    dash = []
    res = []
    imp =''


    for s in range (n_operaciones):
        denominadores[s] = signos[s] +' '+denominadores[s]
        dash.append('-'*len(denominadores[s]))
        if s != n_operaciones-1:
            dash.append('    ')
        top.append(numeradores[s])
        if s != n_operaciones-1:
            top.append('    ')
        bottom.append(denominadores[s])
        if s != n_operaciones-1:
            bottom.append('    ')
        res.append(resultados[s])
        if s != n_operaciones-1:
            res.append('    ')

    top.append('\n')
    bottom.append('\n')
    

    if results == True:
        dash.append('\n')
        final = top + bottom + dash + res
        imp= ''.join(final)

        
    else:
        final = top + bottom + dash
        imp= ''.join(final)

    return imp
