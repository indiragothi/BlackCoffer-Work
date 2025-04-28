# Project: Building a Kibana Dashboard with Elasticsearch Queries on a Sample Dataset (Using ELK Stack)

## Introduction
In this project, I learn how to install and configure the ELK Stack (Elasticsearch, Logstash, Kibana) on a Windows machine, ingest sample datasets provided by Kibana, run basic Elasticsearch queries, and create interactive dashboards for data visualization. By the end of this project, I have a working ELK setup on Windows and a custom Kibana dashboard based on real-world data.

## Pre-requisites
- Basic understanding of web applications and data visualization.
- Familiarity with Windows OS and Command Prompt.
- Java JDK installed on the machine.

## Lab Setup and Tools
- Windows 10/11
- [Java JDK (LTS version)](https://www.oracle.com/java/technologies/javase-downloads.html) installed
- [Elasticsearch for Windows](https://www.elastic.co/downloads/elasticsearch)
- [Kibana for Windows](https://www.elastic.co/downloads/kibana)
- (Optional) [Logstash for Windows](https://www.elastic.co/downloads/logstash)

---

## Exercises

### Exercise 1: Installing Java

**Steps:**
1. Download and install the latest LTS Java JDK from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html) or use OpenJDK.
2. Set the `JAVA_HOME` environment variable:
    - Right-click on **This PC** → **Properties** → **Advanced system settings** → **Environment Variables**.
    - Under **System variables**, click **New**:
        - Variable name: `JAVA_HOME`
        - Variable value: `C:\Program Files\Java\jdk-XX` (replace with your installed path).
    - Edit the **Path** variable and add:
      ```
      %JAVA_HOME%\bin
      ```
3. Verify Java installation:
    ```bash
    java -version
    ```

**Expected Output:**
- Java version displayed successfully.

---

### Exercise 2: Installing Elasticsearch

**Steps:**
1. Download Elasticsearch for Windows from [Elastic Downloads](https://www.elastic.co/downloads/elasticsearch).
2. Extract the ZIP file to `C:\elasticsearch-9.0.0-windows-x86_64\`.
3. Open Command Prompt and navigate:
    ```bash
    cd C:\Users\indira gothi\Downloads\elasticsearch-9.0.0-windows-x86_64\elasticsearch-9.0.0\bin
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
2. Extract the ZIP file to `C:\kibana-9.0.0-windows-x86_64`.
3. Configure Kibana:
    - Open `C:\Users\indira gothi\Downloads\kibana-9.0.0-windows-x86_64\kibana-9.0.0\config\kibana.yml` in a text editor.
    - Uncomment and ensure the following settings:
    ```yaml
    server.port: 5601
    server.host: "localhost"
    elasticsearch.hosts: ["http://localhost:9200"]
    ```
4. Open Command Prompt and navigate:
    ```bash
    cd C:\Users\indira gothi\Downloads\kibana-9.0.0-windows-x86_64\kibana-9.0.0\bin
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
1. In Kibana, go to **Dashboard** → **Create dashboard**.
2. Click **Create visualization**.
3. Select Visualization Type:
    - **Bar Chart**, **Line Graph**, **Pie Chart**, etc.
4. Choose the Sample Dataset’s Index Pattern:
    - e.g., `kibana_sample_data_logs`
5. Configure Visualization:
    - Add a **Metric** (e.g., Count, Average, Sum).
    - Add **Buckets** (e.g., Date Histogram for time series).
6. Save each visualization.
7. Add saved visualizations to your dashboard.
8. Arrange and resize visualizations as needed.
9. Save the dashboard with a descriptive name.

**Expected Output:**
- A custom dashboard with multiple interactive visualizations.

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
