# CRM Analytics: Pipeline de Integração e Análise de Churn

## Visão Geral do Projeto
Este projeto simula um cenário real de inteligência de clientes, cobrindo desde a integração com sistemas de terceiros (CRM) até a modelagem de dados para identificação de risco de evasão (Churn).

O objetivo de negócio é extrair dados de clientes via API, higienizá-los e aplicar regras de negócio em SQL para criar uma análise de safra (Cohort) e segmentar clientes pelo risco de abandono (Recência).

## Stack Tecnológica
* **Linguagem:** Python & SQL Avançado.
* **Conceitos Aplicados:** Integração de APIs REST, Parsing de arquivos JSON, ETL/ELT, Análise de Cohort, Engenharia de Features.
* **Ecossistema:** Simulação de extração de CRMs corporativos (ex: HubSpot/Salesforce) e carga em ambiente Cloud (AWS S3/Glue).

## Estrutura do Repositório

### 1. Extração via API e Prep (`scripts/api_extraction_and_prep.py`)
Script em Python responsável por simular a comunicação com uma API REST corporativa utilizando a arquitetura de *request* e *headers* de autenticação.
* **O que foi feito:** Leitura do payload JSON, conversão para DataFrame (Pandas), tratamento de tipagens temporais e criação da métrica estratégica `days_since_last_purchase`.

### 2. Modelagem e Retenção (`scripts/churn_cohort_analysis.sql`)
Modelagem projetada para rodar em um Data Warehouse, gerando os indicadores que alimentarão dashboards estratégicos (Looker Studio / Power BI).
* **O que foi feito:** Classificação dinâmica do risco de Churn (Baseado em recência), agrupamento por safras (Cohorts) e cálculo do valor de ciclo de vida (LTV) por segmento usando funções de janela (*Window Functions*).

## Impacto Estratégico
Painéis construídos com base nesta modelagem permitem que as equipes de Sucesso do Cliente (CS) e Vendas atuem de forma proativa. Ao identificar grupos de alto risco de *churn* antes que o cancelamento ocorra, a empresa pode criar campanhas de retenção direcionadas e projetar a perda de receita com maior precisão.
