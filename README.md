📚 Projeto 4: Agendador de Espaços e Laboratórios (CampusReserve)
 
🧩 Contexto
Em um campus universitário, gerenciar espaços de estudo e laboratórios é um desafio constante.

O sistema CampusReserve permite que alunos e professores montem um pedido de reserva customizado para projetos, podendo incluir:
- Equipamentos específicos (ex: máquinas com GPU para IA)
- Necessidades de acessibilidade

🎯 Objetivo Didático
- Aplicar padrões de construção passo a passo (Builder)
- Trabalhar com interfaces pequenas (ISP)
- Desenvolver interfaces simples e objetivas

📋 Requisitos Funcionais (RF)
- RF01: O sistema deve possuir um formulário para iniciar uma reserva, onde o usuário (aluno/professor) escolhe o tipo de espaço:
Sala de Estudo
Laboratório
Auditório
- RF02: O sistema deve permitir a adição de requisitos específicos à reserva de forma incremental:
Projetor
Computadores com GPU
Acesso para cadeira de rodas
- RF03: O sistema deve gerar e exibir um Card de Reserva contendo todos os detalhes selecionados
- RF04: O usuário deve poder:
Exportar o comprovante da reserva em JSON
Ou visualizar os dados na tela

⚙️ Requisitos Não Funcionais (RNF)
- RNF01: O inventário do campus (salas e recursos disponíveis) deve ser carregado a partir de:
Dados estáticos
Ou dados em memória

🚧 Restrições Técnicas (Obrigatórias)
🏗️ Arquitetura
O sistema deve seguir o modelo de Arquitetura em Camadas

🧱 Design Pattern: Builder
A criação da reserva deve utilizar o padrão Builder, permitindo construção passo a passo com métodos encadeados.

🧩 SOLID - ISP (Interface Segregation Principle)
Ao invés de uma interface única e extensa (IReservation), devem ser utilizadas interfaces menores e específicas, como:
IEquipmentRequirements
ISpatialRequirements
IAccessibilityNeeds

🧹 Clean Code - Guard Clauses (Early Return)
O sistema deve evitar estruturas complexas com múltiplos if/else aninhados.

Validações devem ser feitas com retorno antecipado, por exemplo:
Verificar dados obrigatórios
Validar entradas inválidas (ex: datas no passado)

📌 Nível do Projeto
Simples
