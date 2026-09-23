import pandas as pd
import json
import requests
import streamlit as st

# Configuração da página deve ser a PRIMEIRA linha de comando Streamlit
st.set_page_config(page_title="Luna - Loja Virtual")
st.title("🛍️ Luna - Loja Virtual")

# Função para carregar dados de forma segura
@st.cache_data
def carregar_base_conhecimento():
    try:
        # Ajuste o caminho conforme sua pasta real (ex: 'data/' ou '.data/')
        caminho = "data/" 
        pedidos = pd.read_csv(f'{caminho}pedidos.csv', sep=';')
        entregas = json.load(open(f'{caminho}entregas.json', encoding='utf-8'))
        produtos = json.load(open(f'{caminho}produtos.json', encoding='utf-8'))
        regras = json.load(open(f'{caminho}regras_loja.json', encoding='utf-8'))
        return pedidos, entregas, produtos, regras
    except Exception as e:
        st.error(f"Erro crítico ao carregar base de dados: {e}")
        return None

dados = carregar_base_conhecimento()

if dados:
    pedidos, entregas, produtos, regras = dados
    OLLAMA_URL = "http://localhost:11434/api/generate"
    MODELO = "gpt-oss"

    # Simulação de cliente
    perfil_cliente = {"nome": "João Silva", "localização": "Sudeste"}
    pedidos_usuario = pedidos[pedidos['id_pedido'] == 1002]

    # Montagem do Contexto
    contexto_loja = f"""
    CLIENTE: {perfil_cliente['nome']} | LOCALIZAÇÃO: {perfil_cliente['localização']}
    PEDIDOS: {pedidos_usuario.to_string(index=False)}
    POLÍTICAS: {json.dumps(regras, ensure_ascii=False)}
    PRODUTOS: {json.dumps(produtos, ensure_ascii=False)}
    """

    SYSTEM_PROMPT = f"""Você é um agente virtual de atendimento ao cliente de uma loja.
Seu objetivo é auxiliar clientes com dúvidas sobre produtos, pedidos, entregas, trocas, devoluções e políticas da loja, utilizando exclusivamente as informações disponíveis na base de conhecimento fornecida.

Regras obrigatórias:

Nunca invente informações que não estejam na base de conhecimento

Caso não encontre a resposta, informe claramente a limitação

Seja educado, claro, objetivo e consultivo

Antecipe necessidades quando possível (ex: sugerir rastreio ou política de troca)

Em situações sensíveis ou de insatisfação, mantenha tom empático

Sempre priorize respostas seguras e verificáveis. Use o contexto abaixo para responder:
    {contexto_loja}"""

    def perguntar(msg):
        prompt_final = f"{SYSTEM_PROMPT}\n\nPergunta do cliente: {msg}"
        try:
            r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt_final, "stream": False}, timeout=60)
            return r.json().get('response', "Erro na resposta.")
        except Exception as e:
            return f"Erro de conexão com Ollama: {e}"

    # Interface de Chat
    if pergunta := st.chat_input("Dúvidas sobre produtos ou entregas?"):
        st.chat_message("user").write(pergunta)
        with st.spinner("Luna consultando base de dados..."):
            resposta = perguntar(pergunta)
            st.chat_message("assistant").write(resposta)