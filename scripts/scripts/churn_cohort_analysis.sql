-- Análise de Retenção, Risco de Churn e Cohort de Clientes
-- Objetivo: Identificar clientes em risco de abandono e calcular o LTV (Lifetime Value)

-- CTE 1: Classificando o Risco de Churn baseado na Recência de Compra
WITH CustomerRisk AS (
    SELECT 
        customer_id,
        signup_date,
        last_purchase,
        total_spent,
        days_since_last_purchase,
        CASE
            WHEN days_since_last_purchase <= 30 THEN 'Low Risk (Active)'
            WHEN days_since_last_purchase BETWEEN 31 AND 90 THEN 'Medium Risk (Warning)'
            WHEN days_since_last_purchase > 90 THEN 'High Risk (Churned)'
        END AS churn_risk_segment
    FROM analytics_db.crm_customer_base
),

-- CTE 2: Agrupando clientes por Safra (Mês e Ano de Entrada) para análise de Cohort
CohortGrouping AS (
    SELECT 
        DATE_TRUNC('month', signup_date) AS cohort_month,
        churn_risk_segment,
        COUNT(customer_id) AS total_customers,
        SUM(total_spent) AS cohort_revenue
    FROM CustomerRisk
    GROUP BY DATE_TRUNC('month', signup_date), churn_risk_segment
)

-- Query Final: Visão Executiva para o Dashboard (Looker Studio / Power BI)
SELECT 
    cg.cohort_month,
    cg.churn_risk_segment,
    cg.total_customers,
    cg.cohort_revenue,
    -- Calculando o ticket médio (LTV parcial) daquele segmento
    ROUND(cg.cohort_revenue / NULLIF(cg.total_customers, 0), 2) AS avg_ltv_per_customer,
    
    -- Window Function para calcular o % que esse grupo representa na receita total da safra
    ROUND(cg.cohort_revenue / SUM(cg.cohort_revenue) OVER(PARTITION BY cg.cohort_month) * 100, 2) AS pct_of_cohort_revenue

FROM CohortGrouping cg
ORDER BY cg.cohort_month DESC, cg.cohort_revenue DESC;
