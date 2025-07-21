# Data Extraction and Text Analysis for Blackcoffer

## Company Details
**Blackcoffer**
- **Consulting Website:** [Blackcoffer](https://blackcoffer.com) | [LSA Lead](https://lsalead.com)
- **Web App Products:** [Netclan](https://netclan.com/) | [Blackcoffer Insights](https://insights.blackcoffer.com/) | [Hire Kingdom](https://hirekingdom.com/) | [Workcroft](https://workcroft.com/)
- **Mobile App Products:** Netclan | Bwstory

## Objective
The goal of this assignment is to extract article text from the URLs provided in the **Input.xlsx** file and perform text analysis to compute specific variables. The final output should be structured as per the **Output Data Structure.xlsx** file.

## Data Extraction
For each article URL in **Input.xlsx**, the program should:
- Extract the **title** and **article text**.
- **Exclude** website headers, footers, and any irrelevant content.
- Save the extracted text in a **text file** named after the URL_ID.

### Tools for Data Extraction
You must use **Python** for data extraction. Recommended libraries:
- **BeautifulSoup**
- **Selenium**
- **Scrapy**
- Any other Python web scraping library of your choice

## Text Analysis
For each extracted article, perform textual analysis and compute the following variables:

### Computed Variables
1. **Positive Score**
2. **Negative Score**
3. **Polarity Score**
4. **Subjectivity Score**
5. **Average Sentence Length**
6. **Percentage of Complex Words**
7. **Fog Index**
8. **Average Number of Words per Sentence**
9. **Complex Word Count**
10. **Word Count**
11. **Syllables per Word**
12. **Personal Pronouns**
13. **Average Word Length**

Refer to **Text Analysis.docx** for detailed definitions of these variables.

## Output Format
- The computed values must be saved in a **CSV or Excel file** following the exact format of **Output Data Structure.xlsx**.
- Ensure that all input variables from **Input.xlsx** are included in the output file.

## Submission Guidelines
To submit your solution:
1. Fill out this **Google Sheet**: [Submission Form](https://forms.gle/nvWAgrCBdq1JkKou8)
2. Upload your files to Google Drive and share the link in the form.

### Submission Requirements
Ensure your submission includes:
✅ **Python Script (.py file)**
✅ **Output File (CSV/Excel as per Output Data Structure.xlsx)**
✅ **Instructions for Running the Script**

 
