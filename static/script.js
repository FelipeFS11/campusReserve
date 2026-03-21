let reservaAtual = null;

// SUBMIT DO FORMULÁRIO
document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("formularioReserva");


    formulario.addEventListener("submit", async function (evento) {
        evento.preventDefault();

        const tipoSala = document.getElementById("tipo_sala").value;

        const equipamentos = Array.from(
            document.querySelectorAll("input[name='equipamentos']:checked")
        ).map(el => el.value);

        const acessibilidade = document.getElementById("acessibilidade").checked;

        const dados = {
            tipo_sala: tipoSala,
            equipamentos: equipamentos,
            acessibilidade: acessibilidade
        };

        try {
            const resposta = await fetch("/reservas", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(dados)
            });

            const resultado = await resposta.json();

            // Salva o JSON
            reservaAtual = resultado;

            // Exibe na tela
            document.getElementById("resultado").textContent =
                mostrarReservaFormatada(resultado); 

        } catch (erro) {
            alert("Erro ao criar reserva.");
            console.error(erro);
        }
    
    });

});

// EXPORTAÇÃO
function exportarJSON() {
    if (!reservaAtual || reservaAtual.erro) {
        alert("Crie uma reserva válida antes de exportar.");
        return;
    }

    const jsonString = JSON.stringify(reservaAtual, null, 4);

    const blob = new Blob([jsonString], { type: "application/json" });
    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = "reserva.json";
    link.click();

    URL.revokeObjectURL(url);

}

function mostrarReservaFormatada(reserva) {
    if (reserva.erro) return;

    document.getElementById("reservaFormatada").style.display = "block";

    document.getElementById("viewTipo").textContent = reserva.tipo_sala;

    // Equipamentos
    const lista = document.getElementById("viewEquipamentos");
    lista.innerHTML = "";

    reserva.equipamentos.forEach(eq => {
        const li = document.createElement("li");
        li.textContent = eq;
        lista.appendChild(li);
    });

    // Acessibilidade
    document.getElementById("viewAcessibilidade").textContent =
        reserva.acessibilidade ? "Sim" : "Não";
}