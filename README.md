Este projeto implementa um sistema simples para gerenciamento de empréstimos e devoluções de livros em uma biblioteca.
O sistema permite o cadastro de usuários e controle de empréstimos com base em uma fila de prioridade.
Os usuários são categorizados em tipos que definem a prioridade no atendimento, como professores, alunos, funcionários, terceirizados e visitantes.
Cada livro possui um status que indica se está disponível ou emprestado.
Quando um usuário solicita um livro disponível, o empréstimo é realizado imediatamente.
Se o livro estiver emprestado, o usuário é inserido em uma fila de espera para aquele livro.
As filas são organizadas considerando a prioridade dos usuários, atendendo primeiro os tipos com maior prioridade.
A fila de espera é implementada usando a estrutura deque do Python, que permite operações eficientes de inserção e remoção.
O sistema utiliza dicionários para armazenar as filas de espera, o status dos livros e o histórico de empréstimos dos usuários.
Cada operação do sistema é realizada por funções específicas para manter o código organizado.
O programa apresenta um menu interativo via terminal para o usuário escolher entre as opções disponíveis.
É possível cadastrar novos usuários informando nome e tipo de usuário.
A função de empréstimo verifica a disponibilidade do livro e atualiza os registros correspondentes.
Quando um livro é devolvido, seu status é atualizado para disponível.
Após a devolução, o sistema verifica se existem usuários na fila de espera para aquele livro.
Caso haja fila, o próximo usuário com maior prioridade é atendido automaticamente e o empréstimo é realizado.
As filas respeitam a ordem de chegada dentro de cada categoria de prioridade.
O sistema mantém um histórico dos livros emprestados por cada usuário.
A verificação do histórico impede que um usuário faça múltiplos empréstimos do mesmo livro.
As informações são armazenadas apenas em memória durante a execução do programa.
O sistema não possui persistência de dados, ou seja, os registros são perdidos após o encerramento.
Os livros são identificados por um código único para facilitar a consulta e controle.
A interface de texto apresenta mensagens claras sobre o resultado das operações.
O código é modularizado para facilitar a manutenção e eventuais alterações.
As funções são pequenas e focadas em tarefas específicas.
O uso do deque melhora a eficiência na manipulação das filas.
O sistema permite visualizar as filas de espera para cada livro e seus usuários.
O histórico do usuário pode ser consultado para verificar os livros atualmente emprestados.
O cadastro impede a criação de usuários com nomes duplicados.
O sistema valida as entradas do usuário para evitar dados inválidos.
A lista de tipos de usuário é fixa e define a prioridade para empréstimos.
O programa executa em loop até que o usuário escolha sair.
A simplicidade do sistema o torna adequado para aprendizado e experimentação.
O código usa apenas bibliotecas padrão do Python.
O sistema controla o estado dos livros para evitar inconsistências.
O atendimento automático após devolução ajuda a reduzir o tempo de espera.
O programa evita que um usuário esteja em múltiplas filas para o mesmo livro.
O menu inclui opções para cadastrar usuário, solicitar empréstimo, devolver livro, mostrar filas e consultar histórico.
As filas são atualizadas dinamicamente conforme as operações são realizadas.
O programa registra os dados dos usuários em um dicionário com nome como chave.
Os livros são armazenados em um dicionário separado com informações detalhadas.
O sistema considera cinco tipos de usuários com prioridades decrescentes.
O uso de dicionários e listas garante acesso rápido às informações.
O programa não possui interface gráfica, funcionando apenas em modo texto.
A estrutura do código facilita a adaptação para novos requisitos.
O sistema é uma base para implementação de funcionalidades mais complexas.
Os dados temporários permitem a simulação do funcionamento real do sistema.
A implementação do sistema prioriza clareza e organização do código.
O programa inclui tratamento básico de erros e validação de entradas.
A fila de espera para cada livro é uma estrutura separada para garantir isolamento dos dados.
O programa controla a quantidade de livros emprestados por usuário.
O sistema não permite múltiplos empréstimos simultâneos do mesmo livro por um usuário.
A devolução atualiza o status do livro e remove o usuário do histórico.
O atendimento automático verifica a fila e atualiza os registros quando possível.
O código mantém a separação clara entre dados de usuários e de livros.
As operações são realizadas com controle de exceções simples.
O programa exibe mensagens de erro para entradas inválidas ou operações impossíveis.
A execução em loop permite múltiplas operações sem reiniciar o sistema.
O sistema é compatível com versões recentes do Python 3.
A documentação inline explica as funções e sua finalidade.
O código foi testado para evitar erros comuns de lógica.
O uso do deque permite controle eficiente das filas de espera.
O programa permite consultar os livros disponíveis a qualquer momento.
O cadastro exige informações mínimas para identificação do usuário.
O sistema facilita o acompanhamento do status dos livros em tempo real.
O programa tem estrutura que permite a expansão para banco de dados.
O sistema mantém a integridade dos dados durante as operações.
O código pode ser utilizado como base para projetos acadêmicos.
O sistema não possui recursos avançados, focando no básico.
O programa é de fácil execução em ambiente local.
O menu principal é claro e direciona o usuário para as ações disponíveis.
As funções são independentes e podem ser chamadas separadamente.
O sistema utiliza variáveis globais para armazenar dados temporários.
O código segue um padrão simples de nomenclatura para facilitar leitura.
A manipulação dos dados é feita de forma estruturada e controlada.
O sistema impede cadastro duplicado de usuários.
O programa verifica disponibilidade antes de efetuar empréstimos.
A fila de espera mantém a ordem correta segundo prioridade e chegada.
O código trata os diferentes tipos de usuário de forma consistente.
O sistema mantém o registro atualizado do status dos livros.
O programa registra empréstimos e devoluções corretamente.
O atendimento automático evita que livros fiquem parados sem usuário esperando.
O sistema exibe as filas com a ordem dos usuários para transparência.
O programa é organizado em blocos de funções para facilitar entendimento.
O código utiliza estruturas padrão do Python para eficiência.
O sistema realiza validações para evitar ações inválidas.
O programa oferece informações claras após cada operação.
O sistema controla o número de livros emprestados simultaneamente.
O programa mantém uma lista de prioridades fixa para o atendimento.
O código pode ser adaptado para incluir novas funcionalidades.
O sistema limita empréstimos para evitar conflitos.
O programa permite o controle dos usuários e livros de forma clara.
O sistema funciona com operações básicas de cadastro, empréstimo e devolução.
O código apresenta simplicidade e organização adequadas para o objetivo.
O programa pode ser executado em qualquer ambiente com Python instalado.
O sistema mantém dados temporários, sem persistência externa.
O programa apresenta uma estrutura lógica para o fluxo das operações.
O sistema permite consultar os dados dos usuários e dos livros facilmente.
O código evita redundâncias e facilita manutenção.
O programa realiza o controle das filas de forma eficiente.
O sistema verifica corretamente a prioridade dos usuários na fila.
O programa registra as operações para controle temporário.
O sistema controla as filas para evitar perda de ordem.
O programa utiliza estruturas eficientes para listas e filas.
O sistema mantém a integridade dos dados em todas as operações.
O código está estruturado para facilitar futuras melhorias.
O programa apresenta mensagens adequadas para interação.
O sistema não permite ações que comprometam a lógica do sistema.
O programa controla o empréstimo para evitar duplicidade.
O sistema realiza devoluções com atualização imediata dos dados.
O programa exibe status atualizados após cada ação.
O sistema utiliza filas de prioridade para controle de espera.
O programa impede que um usuário entre na mesma fila várias vezes.
O sistema controla empréstimos e devoluções de forma automatizada.
O programa possui estrutura clara para armazenamento dos dados.
O sistema mantém registros atualizados para uso durante a execução.
O programa é escrito em Python e utiliza recursos básicos da linguagem.
O sistema pode ser expandido com persistência para uso real.
O programa apresenta uma base sólida para projetos similares.
O sistema é útil para demonstrar conceitos de filas e controle de acesso.
O programa mantém a consistência entre usuários, livros e filas.
O sistema realiza o atendimento automático quando possível.
O programa controla o fluxo de empréstimos e devoluções com eficiência.
O sistema é adequado para simulação e aprendizado.
O programa mantém o controle das filas em tempo real.
O sistema pode ser adaptado para diferentes políticas de prioridade.
O programa registra dados para controle durante a execução.
O sistema evita inconsistências com validação e checagens.
O programa é modular e organizado.
O sistema é funcional e atende aos requisitos básicos do trabalho.
O programa utiliza estrutura de dados adequadas.
O sistema apresenta interface simples e clara.
O programa pode ser utilizado para fins acadêmicos.
O sistema mantém dados em memória durante a execução.
O programa realiza as operações solicitadas pelo usuário.
O sistema valida entradas para garantir integridade.
O programa exibe mensagens informativas e de erro.
O sistema controla o acesso aos livros de forma organizada.
O programa pode ser melhorado com funcionalidades extras.
O sistema registra o histórico dos usuários.
O programa mantém o estado dos livros atualizado.
O sistema gerencia filas respeitando prioridades.
O programa realiza operações de forma consistente.
O sistema permite a consulta dos dados disponíveis.
O programa evita operações inválidas.
O sistema mantém controle sobre múltiplos usuários.
O programa é executado em terminal.
O sistema utiliza apenas bibliotecas padrão.
O programa mantém a ordem das filas.
O sistema permite visualização clara dos dados.
O programa pode ser integrado com outras ferramentas.
O sistema funciona sem dependências externas.
O programa utiliza Python 3.
O sistema tem estrutura organizada.
O programa pode ser utilizado para aprendizado de programação.
O sistema oferece funcionalidades básicas de biblioteca.
O programa controla empréstimos de forma simples.
O sistema pode ser expandido no futuro.
O programa é estruturado para fácil manutenção.
O sistema atende às especificações do trabalho.
O programa realiza todas as operações propostas. 