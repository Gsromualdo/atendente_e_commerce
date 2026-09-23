# atendente_e_commerce

#  Luna - Assistente Virtual Inteligente para E-Commerce

A **Luna** é uma assistente virtual focada no atendimento ao cliente para e-commerce. Ela utiliza uma arquitetura baseada em **RAG (Retrieval-Augmented Generation)** com modelos de linguagem locais (via **Ollama**) para responder dúvidas sobre produtos, status de pedidos e políticas da loja em tempo real, garantindo respostas precisas e sem alucinações.

---

##  Funcionalidades

-  **Consulta de Produtos:** Busca informações sobre catálogo e disponibilidade em tempo real.
-  **Rastreamento de Pedidos:** Verifica o status de entregas e pedidos ativos.
-  **Políticas da Loja:** Responde a dúvidas frequentes sobre trocas, devoluções e frete.
- **Execução 100% Local:** Processamento e inferência realizados localmente via **Ollama**, priorizando privacidade e custo zero de API.
-  **Interface Interativa:** Interface amigável e conversacional construída em **Streamlit**.

---

##  Tecnologias Utilizadas

- **Linguagem:** Python
- **Interface Gráfica:** Streamlit
- **LLM / Inferência Local:** Ollama
- **Arquitetura de Dados:** RAG (Retrieval-Augmented Generation)
- **Base de Conhecimento:** Arquivos de dados em formato `JSON` e `CSV` (`produtos.json`, `pedidos.csv`, `entregas.json`, `regras.json`)

---

## 📁 Estrutura do Projeto

```text
├── data/
│   ├── produtos.json    # Catálogo de produtos
│   ├── pedidos.csv      # Histórico e detalhes de pedidos
│   ├── entregas.json    # Status de rastreamento
│   └── regras.json      # Políticas e FAQs da loja
├── app.py               # Interface principal em Streamlit e lógica do RAG
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto
