################# Historique de calculs #######################
historique = []

#fonction ajouter calcul aprés chaque calcul effectuer 
def ajouter_calcul(calcul):
    historique.append(calcul)


#fonction de l'affichage de l'historique 
def afficher_historique():
    print("Historique des calculs :")
    for calcul in historique:
        print(calcul)
        
    
#fonction pour effacer l'historique     
def effacer_historique():
    historique.clear()




############# Calculs ##################
#function pour l'addition
def addition(a, b):
    result = a + b
    calcul = f"{a} + {b} = {result}"
    ajouter_calcul(calcul)
    return result

#fonction pour la soustraction
def soustraction(a, b):
    result = a - b
    calcul = f"{a} - {b} = {result}"
    ajouter_calcul(calcul)
    return result

#fonction pour la multiplication
def multiplication(a, b):
    result = a * b
    calcul = f"{a} * {b} = {result}"
    ajouter_calcul(calcul)
    return result

#fonction pour la division
def division(a, b):
    if b == 0:
        print("Division par zéro impossible")
    else:
        result = a / b
        calcul = f"{a} / {b} = {result}"
        ajouter_calcul(calcul)
    return result




#verification de la validité de  l'expression saisie 
def evaluer_expression(expression):
    op = ""
    for char in expression:
        if char in ["+", "-", "*", "/","%"]:
            op = char
            break

    if op == "":
       print("Opération non valide")
       arguments()


    operands = expression.split(op)
    if len(operands) != 2:
        raise ValueError("Expression non valide")
    
    try:
        a = float(operands[0])
        b = float(operands[1])

        if op == "+":
            return addition(a, b)
        elif op == "-":
            return soustraction(a, b)
        elif op == "*":
            return multiplication(a, b)
        elif op == "/":
            return division(a, b)
    except ValueError:
        print("Nombres non valides")
    



#récuperer les inputs
def arguments():
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    op = input("Entrez l'opération souhaitée (+, -, *, /) : ")
    expression= str(a)+ op +str(b)
    return expression


#affichage de resultat
expression=arguments()
resultat= evaluer_expression(expression)
print("Résultat : ", expression, "=", resultat)


#effectuer une nouvelle opération à la demmande de l'utilisateur
bool= True
while bool==True:
    reponse=input("voulez vous effectuer une autre opération ? [O]:OUI , [N]:NON , [H]:afficher l'historique , [del]:effacer l'historique  ")

    if reponse=='H':
        afficher_historique()

    elif reponse=='del' :   
        effacer_historique()

    elif reponse== 'N':
        bool==False
    else :
        expression=arguments()
        resultat= evaluer_expression(expression)
        print("Résultat : ", expression, "=", resultat)
