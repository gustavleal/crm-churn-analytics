import pandas as pd
import json
import datetime
# import requests
# import boto3

def fetch_crm_data_mock():
   
    print("[1/3] Estabelecendo conexão com a API do CRM...")
    
    payload_mock = """
    {
        "status": 200,
        "data": [
            {"customer_id": "C-1001", "signup_date": "2025-01-15", "last_purchase": "2026-03-10", "total_spent": 1500.50, "status": "Active"},
            {"customer_id": "C-1002", "signup_date": "2025-02-20", "last_purchase": "2025-11-05", "total_spent": 350.00, "status": "Inactive"},
            {"customer_id": "C-1003", "signup_date": "2025-06-10", "last_purchase": "2026-04-12", "total_spent": 4200.00, "status": "Active"},
            {"customer_id": "C-1004", "signup_date": "2025-08-01", "last_purchase": "2025-09-15", "total_spent": 120.00, "status": "Inactive"}
        ]
    }
    """
    return json.loads(payload_mock)

def process_and_clean_data(json_data):
   
    print("[2/3] Realizando parsing do JSON e engenharia de features...")
    
    df = pd.DataFrame(json_data['data'])
    
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['last_purchase'] = pd.to_datetime(df['last_purchase'])
    
    data_atual = pd.to_datetime('2026-04-15')
    df['days_since_last_purchase'] = (data_atual - df['last_purchase']).dt.days
    
    df['status'] = df['status'].str.upper()
    
    return df

def load_to_datalake(df):
    Simula o particionamento e envio dos dados limpos para um bucket AWS S3.
    print("[3/3] Simulando carga (Load) no Data Lake AWS S3...")
    
    s3_path = "s3://datalake-corp/gold/crm_customer_base/data.parquet"
    
    # upload via boto3 / awswrangler
    # wr.s3.to_parquet(df=df, path=s3_path, dataset=True)
    
    print(f"-> Dados salvos com sucesso em: {s3_path}")
    print("-> Tabela disponibilizada para análise SQL: analytics_db.crm_customer_base")

    # Execução do Pipeline (Main)
if __name__ == "__main__":
    print("--- INICIANDO PIPELINE DE EXTRAÇÃO CRM ---")
    
    raw_data = fetch_crm_data_mock()
    df_clean = process_and_clean_data(raw_data)
    
    print("\nAmostra dos dados processados:")
    print(df_clean[['customer_id', 'days_since_last_purchase', 'status']].head())
    print("\n")
    
    load_to_datalake(df_clean)
    
    print("--- PIPELINE FINALIZADO ---")
