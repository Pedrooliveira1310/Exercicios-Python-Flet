# 🚀 Projetos de Interface de Usuário (Flet / Python)

Este repositório contém uma coleção de 4 atividades práticas desenvolvidas para demonstrar conceitos de desenvolvimento de interfaces de usuário (UI/UX), gerenciamento de estado, captura de inputs, manipulação de listas dinâmicas e estilização de componentes.

---

## 📌 Sumário das Atividades

| Atividade | Nome do Projeto | Descrição Resumida |
| :--- | :--- | :--- |
| **AT01** | [Tela de Boas-Vindas](#-at01---tela-de-boas-vindas) | Interface simples de apresentação com fundo customizado e tipografia. |
| **AT02** | [Cartão de Perfil / Contato](#-at02---cartão-de-perfil--contato) | Layout em formato de *Card* estruturado com ícones e dados de contato. |
| **AT03** | [Formulário Interativo](#-at03---formulário-interativo) | Formulário com campo de texto, checkbox de termos e resposta dinâmica. |
| **AT04** | [Gerenciador de Lista com Contadores](#-at04---gerenciador-de-lista-com-contadores) | Aplicação interativa para adição, alteração de quantidade e remoção de itens. |

---

## 💻 Detalhes das Atividades

### 🔹 AT01 - Tela de Boas-Vindas
**Descrição:**  
Desenvolvimento de uma interface inicial simples e limpa. O objetivo principal é trabalhar com a estruturação básica da tela, definição de cores de fundo, alinhamento de elementos e estilização de texto.

**Recursos e Conceitos Utilizados:**
- Estruturação inicial da janela/aplicação.
- Configuração de fundo colorido em tela cheia (*Full-screen background*).
- Formatação e hierarquia de texto (*Titles & Subtitles*).

- <img width="456" height="882" alt="image" src="https://github.com/user-attachments/assets/a9ab1037-9310-48e9-b528-89b4102520be" />


---

### 🔹 AT02 - Cartão de Perfil / Contato
**Descrição:**  
Criação de um componente visual no estilo *Card* (cartão centralizado), projetado para exibir informações estruturadas de perfil de usuário ou contato. 

> *Nota: A estrutura da interface é genérica e reutilizável para exibição de quaisquer dados de usuário.*

**Recursos e Conceitos Utilizados:**
- Utilização de blocos/containers com bordas arredondadas e sombra/contraste.
- Layout centralizado sobre um fundo neutro.
- Integração de ícones vetoriais (e-mail, telefone) alinhados a rótulos de texto.
- Organização em colunas e linhas (*Rows & Columns*).

- <img width="454" height="889" alt="image" src="https://github.com/user-attachments/assets/cdac5ea9-c447-4325-bcfa-b27703652bae" />


---

### 🔹 AT03 - Formulário Interativo
**Descrição:**  
Interface interativa de formulário de cadastro/confirmação. O usuário digita o nome em um campo de entrada com rótulo (*outlined input*), marca a caixa de aceite de termos e clica no botão para enviar, gerando uma mensagem de saudação personalizada na própria tela.

**Recursos e Conceitos Utilizados:**
- Captura de texto com `TextField`.
- Controle de estado booleano via `Checkbox`.
- Botões de ação (`ElevatedButton` / `Button`).
- Atualização dinâmica da interface em resposta a eventos de clique.

- <img width="444" height="875" alt="image" src="https://github.com/user-attachments/assets/695ade55-7f2e-46f4-9058-0ebcf03b52dd" />


---

### 🔹 AT04 - Gerenciador de Lista com Contadores
**Descrição:**  
Aplicação completa no estilo *Lista de Compras / Tarefas* com tema escuro (*Dark Theme*). Permite que o usuário adicione novos itens através de uma caixa de texto, ajuste dinamicamente a quantidade de cada item utilizando botões de incremento (`+`) e decremento (`-`), e remova itens da lista utilizando o ícone de lixeira.

**Recursos e Conceitos Utilizados:**
- Gerenciamento de estado complexo e coleções dinâmicas (listas de objetos).
- Operações de CRUD básico (Criar, Ler, Atualizar quantidade e Deletar).
- Componentes de controle individual de quantidade para cada linha.
- Estilização em tema escuro com destaques em cores vibrantes.

- <img width="723" height="971" alt="image" src="https://github.com/user-attachments/assets/e29f28cb-3c93-44a4-9343-8c17a5846e9f" />



---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 🐍
- **Framework de UI:** [Flet](https://flet.dev/) (baseado em Flutter)
- **Paradigma:** Desenvolvimento Declarativo de Interfaces

---

## ⚙️ Como Executar os Projetos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências necessárias (Flet):**
   ```bash
   pip install flet
   ```

3. **Execute cada atividade individualmente:**
   ```bash
   python at01.py
   python at02.py
   python at03.py
   python at04.py
   ```

---

📌 *Projeto desenvolvido para fins de aprendizado e prática de desenvolvimento de interfaces com Flet/Python.*
