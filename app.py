from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# ENTIDADE
class Reserva:
    def __init__(self):
        self.tipo_sala = None
        self.equipamentos = []
        self.acessibilidade = False

    def para_dict(self):
        return {
            "tipo_sala": self.tipo_sala,
            "equipamentos": self.equipamentos,
            "acessibilidade": self.acessibilidade
        }

# INTERFACES (ISP)
class IRequisitosEquipamento:
    def adicionar_equipamento(self, equipamento: str):
        pass

class IRequisitosAcessibilidade:
    def definir_acessibilidade(self, necessita: bool):
        pass

class IRequisitosEspaco:
    def definir_tipo_sala(self, tipo_sala: str):
        pass

# BUILDER
class ConstrutorReserva(
    IRequisitosEquipamento,
    IRequisitosAcessibilidade,
    IRequisitosEspaco
    ):

    def __init__(self):
        self.reserva = Reserva()

    def definir_tipo_sala(self, tipo_sala: str):
        self.reserva.tipo_sala = tipo_sala
        return self

    def adicionar_equipamento(self, equipamento: str):
        self.reserva.equipamentos.append(equipamento)
        return self

    def definir_acessibilidade(self, necessita: bool):
        self.reserva.acessibilidade = necessita
        return self

    def construir(self):
        # Guard Clause
        if not self.reserva.tipo_sala:
            raise ValueError("O tipo de sala é obrigatório")
        
        return self.reserva

# SERVICE (CAMADA DE APLICAÇÃO)
class ServicoReserva:
    def criar_reserva(self, dados):
        # Guard Clause
        if "tipo_sala" not in dados:
            raise ValueError("tipo_sala é obrigatório")

        construtor = ConstrutorReserva()

        construtor.definir_tipo_sala(dados["tipo_sala"])

        for eq in dados.get("equipamentos", []):
            construtor.adicionar_equipamento(eq)

        construtor.definir_acessibilidade(
            dados.get("acessibilidade", False)
        )

        return construtor.construir()
    
servico = ServicoReserva()

# DADOS ESTÁTICOS (RNF)
SALAS = ["Sala de Estudo", "Laboratório", "Auditório"]
EQUIPAMENTOS = ["Projetor", "GPU", "Computadores", "Quadro Branco"]

# ROTAS
@app.route("/")
def inicio():
    return render_template(
        "index.html",
        rooms=SALAS,
        equipments=EQUIPAMENTOS
    )

@app.route("/reservas", methods=["POST"])
def criar_reserva():
    try:
        dados = request.json
        reserva = servico.criar_reserva(dados)
        return jsonify(reserva.para_dict()), 201

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400

# EXPORTAÇÃO JSON
@app.route("/exportar", methods=["POST"])
def exportar():
    dados = request.json
    return json.dumps(dados, indent=4), 200, {
        "Content-Type": "application/json"
    }

if __name__ == "__main__":
    app.run(debug=True)