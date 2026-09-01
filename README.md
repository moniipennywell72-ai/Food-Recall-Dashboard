# Food-Recall-Dashboard
🍎 FDA Food Recall Analytics Dashboard

An interactive data analytics dashboard built with Python, Streamlit, Plotly, and the FDA OpenFDA API to monitor, analyze, and visualize food recall events across the United States. This project transforms real-world FDA Food Enforcement data into actionable insights through dynamic dashboards, trend analysis, contamination tracking, geographic mapping, and critical recall alerts.

🚀 Features
Real-time FDA Food Enforcement data integration
Executive KPI dashboard for recall monitoring
Monthly and yearly recall trend analysis
Contamination and recall reason categorization
Interactive U.S. geographic heat map
Class I critical recall alert monitoring
Product name search functionality
Year and recall classification filters
Interactive Plotly visualizations
Responsive Streamlit user interface

📊 Dashboard Tabs
1. Overview
Total recalls
Critical (Class I) recalls
Ongoing recalls
Affected firms
Recall classification distribution
2. Trends
Monthly recall trends
Recall frequency analysis
Historical pattern monitoring
3. Contamination Types
Common contamination categories
Top recall reasons
Food safety risk analysis
4. Geographic Impact
Interactive U.S. choropleth map
State-level recall distribution
Geographic risk assessment
5. Critical Alerts
High-risk Class I recalls
Product details
Recall status and distribution information

🛠️ Technology Stack
Python
Streamlit
Pandas
Plotly
Requests
FDA OpenFDA API
Git & GitHub
🎯 Business Value

This dashboard helps food safety professionals, retailers, supply chain managers, and regulatory analysts identify critical food safety risks, monitor recall trends, evaluate geographic impact, and improve decision-making through data-driven insights.

📥 Installation
Shell
1
git clone https://github.com/your-username/food-recall-dashboard.git
2
 
3
cd food-recall-dashboard
4
 
5
pip install -r requirements.txt
6
 
7
streamlit run app.py
Show more lines
📡 Data Source

Food recall data is sourced from the FDA Food Enforcement Reports dataset through the OpenFDA API, which provides publicly available recall information for FDA-regulated food products. Access to the dataset and API is provided by the FDA OpenFDA program.

📈 Future Enhancements
Recall forecasting using machine learning
Supply chain risk scoring
State-level trend comparisons
Real-time notification system
Advanced contamination analytics
