# Student Activity Management with Retool and Google Sheets

This project is a simple student management interface built using **Retool** and connected to **Google Sheets** as a backend. It allows users to **view**, **add**, **update**, and **delete** student records, including fields such as name, gender, class level, home state, major, and extracurricular activity.

---

## 🔗 Data Source

- **Backend**: Google Sheets (`student activity`)
- **Sheet Name**: `Sheet1`
- **Columns**:
  - `Student Name`
  - `Gender`
  - `Class Level`
  - `Home State`
  - `Major`
  - `Extracurricular Activity`

---

## 🧩 Features

- ✅ View student data in a table (auto-synced with Google Sheets)
- ➕ Add new student records using a form
- 🔄 Update existing student details
- ❌ Delete student records from the table

---

## 🛠 Retool Setup

### 1. Create Form Inputs

Inside Retool, add the following form inputs:

| Label                    | Component Type | ID                        |
|--------------------------|----------------|---------------------------|
| Student Name             | Text Input     | `student_name`            |
| Gender                   | Dropdown/Text  | `gender`                  |
| Class Level              | Dropdown/Text  | `class_level`             |
| Home State               | Text Input     | `home_state`              |
| Major                    | Dropdown/Text  | `major`                   |
| Extracurricular Activity | Dropdown/Text  | `extracurricular_activity`|

Also add a **Submit** button with ID: `submitBtn`

---

### 2. Create Insert Query

- **Query Name**: `insertStudent`
- **Resource**: Google Sheets
- **Action Type**: `Append data to a spreadsheet`
- **Spreadsheet**: `student activity`
- **Sheet Name**: `Sheet1`
- **Values to Append**:
```js
[
  [
    student_name.value,
    gender.value,
    class_level.value,
    home_state.value,
    major.value,
    extracurricular_activity.value
  ]
]

 