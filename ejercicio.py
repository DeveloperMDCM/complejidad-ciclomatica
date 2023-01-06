#Validar que un empleado no puede trabajar miles de horas aqui no esta eso
def CalcularPago(): # (Inicio)
    pago = 0
    horasTrabajadas = int(input("Digite las horas trabajadas: "))
    C = str(input("Seleccione la categoria: \n|    1:    | 12000\n|    2:    | 17000\n|    3:    | 22000\n\n:"))
    TarifaDePago = {"1":12000,"2":17000,"3":22000 }   
    if C in TarifaDePago: # Si la categoria esta en el diccionario (A)
      if(horasTrabajadas > 48): # Si las horas trabajadas son mayores a 48 (B)
          tarifa_extra = (TarifaDePago[C] * 0.20) + (TarifaDePago[C]) # (C)
          horas_extras = horasTrabajadas - 48; # (D)
          pago = horas_extras * tarifa_extra + 48 * TarifaDePago[C] # (E)       
      elif(horasTrabajadas >= 24): # Si las horas trabajadas son mayores o iguales a 24 (F)
        subsidio=(TarifaDePago[C] * horasTrabajadas) * 0.10 # (G)
        pago = (TarifaDePago[C] * horasTrabajadas) + subsidio # (H)
      else: # Si las horas trabajadas son menores a 24
        subsidio= (TarifaDePago[C] * horasTrabajadas) * 0.05 # (I)
        pago = (TarifaDePago[C] * horasTrabajadas) + subsidio # (J)      
    else : # Si la categoria no esta en el diccionario
      print("La categoria no existe")  # (K)
    return print("El pago es: ", pago)     
CalcularPago() # llamada a la funcion  Complejidad ciclomatica:  4 MOISES-CANARIA final

