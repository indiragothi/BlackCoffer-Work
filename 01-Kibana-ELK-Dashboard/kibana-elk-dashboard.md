# Project: Building a Kibana Dashboard with Elasticsearch Queries on a Sample Dataset (Using ELK Stack)

## Introduction
In this project, I learn how to install and configure the ELK Stack (Elasticsearch, Logstash, Kibana) on a Windows machine, ingest sample datasets provided by Kibana, run basic Elasticsearch queries, and create interactive dashboards for data visualization. By the end of this project, I have a working ELK setup on Windows and a custom Kibana dashboard based on real-world data.

## Pre-requisites
- Basic understanding of web applications and data visualization.
- Familiarity with Windows OS and Command Prompt.
- Java JDK installed on the machine.

## Setup and Tools
- Windows 10/11
- [Java JDK (LTS version)](https://www.oracle.com/java/technologies/javase-downloads.html) installed
- [Elasticsearch for Windows](https://www.elastic.co/downloads/elasticsearch)
- [Kibana for Windows](https://www.elastic.co/downloads/kibana)
- (Optional) [Logstash for Windows](https://www.elastic.co/downloads/logstash)

---

## Exercises

### Exercise 1: Installing Java

**Steps:**
1. Download and install the latest LTS Java JDK from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html) or [OpenJDK](https://adoptium.net/).
2. During installation, ensure the option **"Set JAVA_HOME environment variable"** is selected (if available).
3. After installation, verify Java installation by running the following command in Command Prompt:
    ```bash
    java -version
    ```

**Expected Output:**
- Java version is displayed successfully in the Command Prompt.

---

### Exercise 2: Installing Elasticsearch

**Steps:**
1. Download Elasticsearch for Windows from [Elastic Downloads](https://www.elastic.co/downloads/elasticsearch).
2. Extract the ZIP file to `C:\elasticsearch`.
3. Open Command Prompt and navigate:
    ```bash
    cd C:\elasticsearch\bin
    ```
4. Start Elasticsearch:
    ```bash
    elasticsearch.bat
    ```
5. Verify that Elasticsearch is running:
    - Open a browser and visit:  
      `http://localhost:9200`

**Expected Output:**
- JSON response with Elasticsearch server information.

---

### Exercise 3: Installing Kibana

**Steps:**
1. Download Kibana for Windows from [Elastic Downloads](https://www.elastic.co/downloads/kibana).
2. Extract the ZIP file to `C:\kibana`.
3. Configure Kibana:
    - Open `C:\kibana\config\kibana.yml` in a text editor.
    - Uncomment and ensure the following settings:
    ```yaml
    server.port: 5601
    server.host: "localhost"
    elasticsearch.hosts: ["http://localhost:9200"]
    ```
4. Open Command Prompt and navigate:
    ```bash
    cd C:\kibana\bin
    ```
5. Start Kibana:
    ```bash
    kibana.bat
    ```
6. Access Kibana:
    - Open a browser and go to:  
      `http://localhost:5601`

**Expected Output:**
- Kibana dashboard home page loaded successfully.

---

### Exercise 4: (Optional) Installing Logstash

**Steps:**
1. Download Logstash for Windows from [Elastic Downloads](https://www.elastic.co/downloads/logstash).
2. Extract Logstash to `C:\logstash`.

*(Not required if you are directly loading Kibana sample data.)*

---

### Exercise 5: Load Sample Data in Kibana

**Steps:**
1. Open Kibana:  
   `http://localhost:5601`
2. On the home page, under **"Add Data to Kibana"**, click:
    - **Try our sample data**.
3. Choose a dataset:
    - Example options:
        - Sample web logs
        - Sample eCommerce orders
        - Sample flight data
4. Click **Add data**.

**Expected Output:**
- Sample datasets added and ready for exploration.

---

### Exercise 6: Creating a Kibana Dashboard

**Steps:**

1. In Kibana, go to **Discover**:
   - Select the **eCommerce sample data** (`kibana_sample_data_ecommerce`).
   - Explore available fields and records.

2. Go to **Visualize Library** → **Create Visualization**:
   - Use **Lens** editor to create visualizations.
   - Choose types like **Bar Chart**, **Pie Chart**, **Table**, etc.

3. Create Visualizations:
   - Example: Bar Chart of `order_date` vs `total_quantity`.
   - Example: Pie Chart of `category.keyword`.
   - Example: Table showing `customer_gender` and `sum of total_quantity`.

4. Save each visualization with a meaningful name.

5. Go to **Dashboard** → **Create Dashboard**:
   - Click **Add from Library** and select saved visualizations.
   - Arrange and resize them as needed.

6. Save the dashboard with a descriptive name.

**Expected Output:**
- A dashboard with multiple visualizations based on the eCommerce dataset.

---

### Exercise 7: Running Basic Elasticsearch Queries

**Steps:**
1. In Kibana, go to **Dev Tools** → **Console**.
2. Run basic queries, for example:

**Query 1: Fetch first 10 documents**
```json
GET kibana_sample_data_logs/_search
{
  "query": {
    "match_all": {}
  },
  "size": 10
}
