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

### 1. 📥 `insertStudent` (Insert New Row)
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

