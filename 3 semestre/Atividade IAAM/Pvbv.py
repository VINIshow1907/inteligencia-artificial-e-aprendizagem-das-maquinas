import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    print("--- Sistema Empresarial: Leitura de Excel e Previsão ---")

    # 1. LENDO O ARQUIVO EXCEL
    # O engine='openpyxl' é necessário para ler arquivos .xlsx modernos
    nome_arquivo = "vendas_empresa.xlsx"
    
    try:
        print(f"Lendo arquivo '{nome_arquivo}'...")
        df = pd.read_excel(nome_arquivo, engine='openpyxl')
    except FileNotFoundError:
        print(f"ERRO: Não encontrei o arquivo '{nome_arquivo}'.")
        print("Certifique-se que ele está na mesma pasta do código.")
        return

    print("\n1. Dados Carregados do Excel (Primeiras linhas):")
    print(df.head())

    # 2. PREPARANDO OS DADOS
    # Usamos os nomes das colunas que você colocou no Excel
    try:
        X = df[['Investimento']] 
        y = df['Vendas']
    except KeyError:
        print("ERRO: As colunas do Excel devem se chamar 'Investimento' e 'Vendas'.")
        return

    # Separação Treino/Teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. TREINAMENTO
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    print(f"\n2. Inteligência Calibrada!")
    # Mostra quanto retorna para cada 1 real investido
    print(f"   Para cada R$ 1,00 investido, o retorno extra é de: R$ {modelo.coef_[0]:.2f}")

    # 4. PREVISÃO (SIMULAÇÃO)
    # Vamos simular um valor alto que NÃO está no Excel (ex: 25.000)
    valor_investimento = 25000
    novo_investimento = pd.DataFrame({'Investimento': [valor_investimento]})
    previsao = modelo.predict(novo_investimento)

    print(f"\n3. CENÁRIO FUTURO:")
    print(f"   Se a empresa investir: R$ {valor_investimento:,.2f}")
    print(f"   Previsão de Vendas:    R$ {previsao[0]:,.2f}")

    # 5. GRÁFICO
    plt.figure(figsize=(10, 6)) # Aumenta o tamanho da janela
    plt.scatter(X, y, color='blue', s=100, label='Histórico (Excel)') # Bolinhas maiores
    plt.plot(X, modelo.predict(X), color='red', linewidth=3, label='Linha de Tendência')
    
    # Ponto da previsão (Verde)
    plt.scatter(valor_investimento, previsao, color='green', marker='*', s=300, label='Previsão R$ 25k')

    plt.title('Análise de Retorno sobre Investimento (ROI)')
    plt.xlabel('Investimento em Marketing (R$)')
    plt.ylabel('Vendas Totais (R$)')
    plt.legend()
    plt.grid(True, linestyle='--')
    
    print("\nGerando gráfico... Confira a janela.")
    plt.show()

if __name__ == "__main__":
    main()