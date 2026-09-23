import pandas as pd
import json
import os

def testar_carregamento():
    caminho = "data/" 
    
    if not os.path.exists(caminho):
        print(f"ERRO: A pasta '{caminho}' nao foi encontrada.")
        return

    arquivos_json = ["entregas.json", "produtos.json", "regras_loja.json"]
    
    try:
        print("--- Iniciando Teste de Carga ---")
        
        # 1. Testando CSV - Usando o separador ';' identificado no seu arquivo
        print(f"Tentando ler: {caminho}pedidos.csv...")
        pedidos = pd.read_csv(f'{caminho}pedidos.csv', sep=';')
        print(f"SUCESSO: pedidos.csv carregado! Linhas: {len(pedidos)}")
        
        # 2. Testando cada JSON individualmente
        for arq in arquivos_json:
            full_path = os.path.join(caminho, arq)
            print(f"Tentando ler: {full_path}...")
            
            if os.path.getsize(full_path) == 0:
                print(f"ERRO: O arquivo '{arq}' esta VAZIO.")
                continue
                
            with open(full_path, 'r', encoding='utf-8') as f:
                json.load(f)
                print(f"SUCESSO: {arq} carregado!")

    except Exception as e:
        print(f"\nOCORREU UM ERRO: {str(e)}")

if __name__ == "__main__":
    testar_carregamento()