function CalcularPago() {
    let pago = document.getElementById("pago");
    var horasTrabajadas = document.getElementById("horasTrabajadas").value;
    let TarifaDePago = document.getElementById("TarifaDePago");
    let extra = document.getElementById("extra");
    let horas_extras = 0;
    let tarifa_extra = 0;
    categoria1.checked == true ? TarifaDePago.value = 12000 : categoria2.checked == true ? TarifaDePago.value = 17000 : categoria3.checked == true ? 
    TarifaDePago.value = 22000 : TarifaDePago.value = 0
    if (horasTrabajadas > 48) {
        tarifa_extra = (TarifaDePago.value * 0.20) + parseInt(TarifaDePago.value);
        horas_extras = horasTrabajadas - 48; 
        pago.textContent = `Pago:  $ ${horas_extras * tarifa_extra + 48 * TarifaDePago.value} `;  extra.innerHTML = "Extra del 20%";
    }
     else if (horasTrabajadas >= 24) {
        let subsidio = (TarifaDePago.value * horasTrabajadas) * 0.10; pago.textContent = `Pago: $ ${(TarifaDePago.value * horasTrabajadas) + subsidio}  `; extra.innerHTML = "Extra del 10%";
    }
     if (horasTrabajadas < 24) {
        let subsidio = (TarifaDePago.value * horasTrabajadas) * 0.05; pago.textContent = `Pago: $ ${(TarifaDePago.value * horasTrabajadas) + subsidio}  `; extra.innerHTML = "Extra del 5%";
    }
}
