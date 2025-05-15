# 🎓 Student Activity Management with Retool and Google Sheets

A lightweight CRUD-based student activity management system built using **Retool** and connected to **Google Sheets** for backend data storage.

---

## 📂 Project Overview

This app allows users to:

- 🔍 **View** all student records in a table
- ➕ **Insert** new student entries via a form
- ✏️ **Update** selected student information
- ❌ **Delete** student records

---

## 🔗 Data Source Configuration

- **Backend**: Google Sheets
- **Spreadsheet Name**: `student activity`
- **Sheet Name**: `Sheet1`

### Sheet Columns:
- `Student Name`
- `Gender`
- `Class Level`
- `Home State`
- `Major`
- `Extracurricular Activity`

---

## 🧩 Retool Components Setup

### 📝 Form Inputs

| Label                    | Component Type | ID                        |
|--------------------------|----------------|---------------------------|
| Student Name             | Text Input     | `student_name`            |
| Gender                   | Dropdown/Text  | `gender`                  |
| Class Level              | Dropdown/Text  | `class_level`             |
| Home State               | Text Input     | `home_state`              |
| Major                    | Dropdown/Text  | `major`                   |
| Extracurricular Activity | Dropdown/Text  | `extracurricular_activity`|

### 🔘 Submit Button

- **Label**: Submit
- **Component ID**: `submitBtn`
- **Event Handler**:
  - Action: Run query → `insertStudent`
  - (Optional: Refresh table using `readData` after insert)

---

## 🧠 Queries Used

### 1. 📥 `insertData` (Insert New Row)
- **Resource**: Google Sheets
- **Action Type**: Append data to a spreadsheet
- **Sheet**: `Sheet1`
- **Values to Append**:

```js
{
  "Student Name": {{ form1.data.Student_name }},
  "Gender": {{ form1.data.Gender }},
  "Class Level": {{ form1.data.Class_level }},
  "Home State": {{ form1.data.Home_state }},
  "Major": {{ form1.data.Major }},
  "Extracurricular Activity": {{ form1.data.Extracurricular_activity }}
}
```

### 📄 2. `readData` – Read Records

- **Action Type**: `Read data from a spreadsheet`
- **Sheet Name**: `Sheet1`

### ✅ Use Case:
Fetches all records and displays them in a table component.

> No filters needed for full sheet read.

### 3. `updateRow` – Update a Record

- **Action Type**: `Update a row`
- **Sheet Name**: `Sheet1`

🔎 Filter to Match Row:
Use a unique identifier to match the correct row to update. Example using Student Name (if unique):
```js
{
  "Student Name": {{ form1.data["Student Name"] }}
}
```

### ❌ 4. `deleteRow` – Delete a Record

- **Action Type**: `Delete a single row`
- **Sheet Name**: `Sheet1`

🔎 Filter to Match Row:
```js
{
  "Student Name": {{ form1.data["Student Name"] }}
}
```