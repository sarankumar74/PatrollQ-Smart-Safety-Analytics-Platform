# 🚔 PatrolIQ - Smart Safety Analytics Platform

> Empowering law enforcement and city administrators with data-driven insights for safer urban communities.

---

## 🧠 Problem Statement

Urban areas face significant challenges in efficient police deployment and crime prevention due to the lack of actionable insights from massive crime datasets.  

**PatrolIQ** is a comprehensive urban safety intelligence platform that leverages **unsupervised machine learning** techniques to analyze crime patterns and optimize police resource allocation.  

Imagine being a **crime intelligence analyst** at the Chicago Police Department — every day, officers ask:
- “Where should we patrol tonight?”
- “Which neighborhoods need more resources?”
- “When do most crimes occur?”

With **PatrolIQ**, these questions are answered through intelligent data analytics, helping prevent crimes and save lives.

---

## 🎯 Project Objectives

The platform aims to:
- 🗺️ Identify **crime hotspots** through geographic and temporal clustering  
- 📊 Simplify visualization of complex crime patterns using **dimensionality reduction**  
- ⚡ Provide **real-time analysis** of 500,000+ crime records from Chicago  
- 🧩 Enable **feature engineering** from 22 crime and location variables  
- 🧠 Integrate **MLflow** for model tracking and comparison  
- 🌐 Deliver a **Streamlit Cloud–based** interactive application for end-users  

---

## 💼 Business Use Cases

### 🏢 Police Departments
- Optimize patrol routes and reduce response time by **up to 60%**
- Identify **high-risk areas** requiring additional presence  
- Predict **crime patterns** for proactive prevention  
- Enable **evidence-based resource deployment** and budget optimization  

### 🏙️ City Administration
- Support **data-driven urban planning** for safer neighborhoods  
- Strategically place **surveillance systems and lighting**  
- Justify **public safety budget allocations** using concrete insights  
- Track **crime trends** across districts and time periods  

### 🕵️ Law Enforcement Analytics Firms
- Deliver **crime intelligence services** to multiple jurisdictions  
- Develop **predictive policing** products for client cities  
- Benchmark **safety performance** across urban areas  
- Generate **custom crime analysis reports** for stakeholders  

### 🚑 Emergency Response Systems
- Prioritize emergency calls via **risk-based assessment**  
- Optimize **ambulance and fire department** deployment  
- Enable **multi-agency coordination** in high-risk zones  
- Provide **real-time situational awareness** to first responders  

---

## 🧩 Skills & Technologies

**Domain:** Public Safety and Urban Analytics  
**Key Skills:**
- Python  
- Streamlit (Cloud Deployment)  
- Machine Learning (Unsupervised Learning, Clustering)  
- Data Analysis & Feature Engineering  
- Dimensionality Reduction  
- Geographic Data Analysis  
- Data Visualization  
- MLflow (Experiment Tracking)

---

## 🧭 Project Approach

### Step 1: Data Acquisition & Preprocessing
- Download and preprocess **7.8M+ crime records** from the Chicago dataset  
- Sample **500,000 recent records** for analysis  
- Clean and handle missing values  
- Extract **temporal features** (hour, day, month)  
- Conduct data validation and quality assessment  

### Step 2: Exploratory Data Analysis
- Analyze **33+ crime categories**  
- Study **geospatial patterns** (latitude/longitude)  
- Investigate **temporal trends** (hourly, daily, monthly, seasonal)  
- Examine **arrest rates** and **domestic incidents**  
- Generate **statistical summaries and visual dashboards**  

### Step 3: Feature Engineering
- Temporal features (hour of day, weekend flag, season)  
- Geographic features (district clustering, coordinate binning)  
- Crime severity scores  
- Categorical encoding and coordinate normalization  

### Step 4: Unsupervised Learning & Clustering
#### 📍 Geographic Crime Hotspot Clustering
Algorithms:
- **K-Means** → Identify 5–10 distinct geographic crime hotspots  
- **DBSCAN** → Detect high-density crime zones with noise filtering  
- **Hierarchical Clustering** → Build dendrograms for nested crime area analysis  

Evaluation Metrics:
- Silhouette Score (>0.5 target)
- Davies–Bouldin Index  
- Elbow Method  

#### ⏰ Temporal Pattern Clustering
- **K-Means** on temporal features (hour, day, month)  
- Identify 3–5 temporal crime patterns (e.g., late-night vs. rush-hour crimes)  
- Discover **high-risk time slots** for resource planning  
- Group **temporal behavior profiles** for each crime type  

---

## ⚙️ Deployment Architecture

- **Frontend:** Streamlit (deployed on Streamlit Cloud)
- **Backend:** Python (Pandas, Scikit-learn, Matplotlib, Plotly)
- **Experiment Tracking:** MLflow
- **Data Source:** Chicago Open Data Portal  
- **Storage:** Local/Cloud CSV integration

---

## 🧪 ML Workflow Overview

1. Data ingestion and cleaning  
2. Feature transformation and scaling  
3. Clustering model training (K-Means, DBSCAN, Hierarchical)  
4. Model evaluation and selection  
5. MLflow experiment tracking  
6. Visualization and Streamlit dashboard deployment  

---

## 🚀 Streamlit Application Features

- 🗺️ Interactive crime hotspot map  
- ⏰ Temporal crime pattern charts  
- 📊 Real-time crime statistics dashboard  
- 🧠 ML experiment tracking with MLflow  
- 🌐 Accessible deployment for law enforcement stakeholders  

---

## 🖼️ User Interface Overview

PatrolIQ’s **Streamlit dashboard** provides an intuitive interface for exploring real-time urban safety analytics.  

Below are key pages of the platform:

### 🧭 1. Dashboard Overview
Displays key metrics, total incidents, and safety insights.

![Dashboard Screenshot](<img width="1916" height="974" alt="Dashboard Overview" src="https://github.com/user-attachments/assets/ee06d611-7a40-408b-8948-911c1c78ad75"/>
)

---

### 🗺️ 2. Crime Hotspot Map
Visualizes geographic clustering and identifies high-risk zones.

![Crime Hotspot Map](<img width="1887" height="932" alt="Screenshot 2025-11-08 131015" src="https://github.com/user-attachments/assets/a0b936fd-8c9e-40d7-8b82-bb2c59a295c3"/>
)

---

### ⏰ 3. Temporal Pattern Analysis
Shows time-based crime trends, including peak hours and seasonal variations.

![Temporal Analysis](<img width="1919" height="1079" alt="Screenshot 2025-11-08 130930" src="https://github.com/user-attachments/assets/3384cb09-862f-47a0-beed-a1599cb83f3e"/>
)

---

> All visualizations are **interactive** and powered by **Streamlit**, **Plotly**, and **Scikit-learn**.

---
🧩 **Project Structure**

PatrolIQ/
│
├── clustering/
│   ├── clusters_main.ipynb        
│
├── patrollq_eda/
│   ├── patrollq_eda.ipynb     
│
│
├── app.py                 
│
├── plots/
│   ├── Cluster Visual by Month, Day                 
│   ├── Clusters by Longitude, Latitude, Behavioral + Spatial Crime          
│   ├── Clusters Visuals by Ward-Community
│   ├── Crime Cluster Centers (Latitude & Longitude)
│   ├── Spatio-Temporal Crime Clusters (Location-based)
│   ├── X Coordinate, Y Coordinate, Month, Year, Day
│
├── requirements.txt                     

