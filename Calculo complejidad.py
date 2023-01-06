from radon.visitors import ComplexityVisitor
complejidad = ComplexityVisitor.from_code('''
def CalcularPago(): # (Inicio)
    horasTrabajadas = int(input("Digite las horas trabajadas: "))
    print("Categoria | Tarifa")    
    print("|    1:    | 12000")
    print("|    2:    | 17000")
    print("|    3:    | 22000")
    C = str(input("Seleccione la categoria: "))
    TarifaDePago = {"1":12000,"2":17000,"3":22000 }   
    if C in TarifaDePago: # Si la categoria esta en el diccionario (A)
      if(horasTrabajadas > 48): # Si las horas trabajadas son mayores a 48 (B)
          tarifa_extra = (TarifaDePago[C] * 0.20) + (TarifaDePago[C]) # (C)
          horas_extras = horasTrabajadas - 48; # (D)
          pago = horas_extras * tarifa_extra + 48 * TarifaDePago[C] # (E)
          return print("El pago es: ", pago)  # (F)
      elif(horasTrabajadas >= 24): # Si las horas trabajadas son mayores o iguales a 24 G
        subsidio=(TarifaDePago[C] * horasTrabajadas) * 0.10 # (H)
        pago = (TarifaDePago[C] * horasTrabajadas) + subsidio # (I)
        return print("El pago es: ", pago) # (J)
      else: # Si las horas trabajadas son menores a 24
        subsidio= (TarifaDePago[C] * horasTrabajadas) * 0.05 # (K)
        pago = (TarifaDePago[C] * horasTrabajadas) + subsidio # (L)
        return print("El pago es: ", pago)  # (M)
    else : # Si la categoria no esta en el diccionario
      print("La categoria no existe")  # (N)  
CalcularPago() # llamada a la funcion  Complejidad ciclomatica:  4 MOISES-CANARIA final
''')
print("Complejidad ciclomatica: ", complejidad.functions[0].complexity)