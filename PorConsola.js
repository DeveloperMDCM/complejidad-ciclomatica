function CalcularPago2() {
    let pago = 0;
    let subsidio = 0;
    let horasTrabajadas = prompt("Ingrese las horas trabajadas ");
    let TarifaDePago = { 1: 12000, 2: 17000, 3: 22000 };
    C = prompt("Seleccione la categoria: \n|    1:    | 12000\n|    2:    | 17000\n|    3:    | 22000\n\n");
    if (C in TarifaDePago) { // (A) 
        if (horasTrabajadas > 48) { // (B)
            var tarifa_extra = (TarifaDePago[C] * 0.20) + (TarifaDePago[C]);  // (C)
            var horas_extras = horasTrabajadas - 48; // (D)
            pago = `${horas_extras * tarifa_extra + 48 * TarifaDePago[C]} `; // (E) 
        }
        else if (horasTrabajadas >= 24) { // (F)
            subsidio = (TarifaDePago[C] * horasTrabajadas) * 0.10; // (G)   
            pago = `${(TarifaDePago[C] * horasTrabajadas) + subsidio}`; // (H)  
        }
        else{
            subsidio = (TarifaDePago[C] * horasTrabajadas) * 0.05; // (I) 
            pago = `${(TarifaDePago[C] * horasTrabajadas) + subsidio}`; // (J)     
        }
    } else {
        alert("Categoria " + C + " no valida"); // (K) 
    }
    alert("Pago: " + pago);
}
