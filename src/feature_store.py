# Construção de Feature Store e Aplicação de Engenharia de Atributos 
# Módulo de Deploy do Pipeline

# Imports
import os
import json
import time
import cria_feature_store
import treina_modelo
import salva_modelo
import explora_dados

def main():

    print("\nIniciando a Execução do Pipeline!")

    # Pausa a execução por 5 segundos
    time.sleep(5)

    # Cria um diretório para armazenar os recursos, se não existir
    os.makedirs('feature_store', exist_ok = True)
    
    # Cria um diretório para armazenar informações das execuções do pipeline, se não existir
    os.makedirs('pipeline_runs', exist_ok = True)

    # Chama a função para criar o armazenamento de recursos (feature store)
    features_df = cria_feature_store.sil_cria_feature_store()
    
    # Define o caminho para salvar o arquivo de recursos
    feature_store_path = 'feature_store/features.csv'
    
    # Salva o DataFrame de recursos como CSV no caminho especificado sem incluir o índice
    features_df.to_csv(feature_store_path, index = False)

    # Chama a função para explorar os dados
    explora_dados.analisa_dados(features_df)

    # Chama a função para treinar e avaliar o modelo, retornando várias informações relevantes
    modelo, X_teste, y_teste, previsoes, acuracia, class_report = treina_modelo.treina_avalia_modelo(features_df)

    # Define o caminho para salvar o modelo treinado
    caminho_modelo = 'pipeline_runs/random_forest_sil.joblib'
    
    # Define o caminho para salvar as previsões
    caminho_previsoes = 'pipeline_runs/previsoes.csv'
    
    # Define o caminho para salvar informações de execução (run) do pipeline
    pipeline_run_info_path = 'pipeline_runs/pipeline_run_info.json'

    # Salva o modelo treinado no caminho especificado
    salva_modelo.salva_modelo(modelo, caminho_modelo)
    
    # Salva as previsões e os valores reais de teste em um arquivo CSV
    salva_modelo.salva_previsoes(previsoes, y_teste, caminho_previsoes)

    # Cria um dicionário com informações sobre a execução do pipeline
    pipeline_run_info = {
        'tipo_modelo': 'RandomForestClassifier',
        'caminho_modelo': caminho_modelo,
        'caminho_feature_store': feature_store_path,
        'acuracia_modelo': acuracia,
        'caminho_previsoes': caminho_previsoes
    }
    
    # Salva as informações da execução do pipeline em um arquivo JSON
    salva_modelo.salva_info(pipeline_run_info, pipeline_run_info_path)

    # Imprime a acurácia do modelo na tela
    print(f"\nAcurácia: {acuracia}")
    
    # Imprime o relatório de classificação
    print("\nClassification Report:")
    print(class_report)
    
    print("\n")

    # Abre o arquivo JSON com as informações da execução do pipeline
    with open(pipeline_run_info_path, 'r') as file:
        data = json.load(file)

    # Converte os dados para uma string JSON formatada de forma legível
    formatted_json = json.dumps(data, indent=4)

    # Imprime as informações de execução formatadas de forma legível
    print(f"Resumo da Execução do Pipeline:\n{formatted_json}")

    print("\n Concluído com Sucesso!\n")
    
if __name__ == "__main__":
    # Executa a função principal se o script for o ponto de entrada do programa
    main()
