# Quote Generator Application using Flask

A simple demo Flask web application that displays random motivational quotes. The app fetches quotes from an external API and provides fallbacks when the API is unavailable.

## Features

- Random motivational quotes display
- New quote on button click without page refresh
- Fallback quotes when API is unavailable
- Simple and clean UI

## Project Structure

```
/quote_generator
  /static
    /css
      style.css
  /templates
    index.html
  app.py
  requirements.txt
```

## Setup Instructions

### 1. Clone the repository or create the project structure as shown above

### 2. Install Python 3.12
Download and install Python from [python.org](https://www.python.org/downloads/) or use your package manager.

### 3. Set up a virtual environment using Conda

```bash
# Create a new conda environment
conda create -p venv python==3.12 -y

# Activate the environment
conda activate venv
```

### 4. Create requirements.txt file with the following content

```
flask==2.3.3
requests==2.31.0
urllib3==2.0.7
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Access the application
Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How It Works

1. The app initializes a Flask web server
2. When a user accesses the homepage, the app attempts to fetch a random quote from the Quotable API
3. If the API call is successful, the quote is displayed
4. If the API is unavailable, a fallback quote is randomly selected from the predefined list
5. Users can get a new quote by clicking the "New Quote" button, which uses AJAX to fetch a new quote without reloading the page

## API Reference

The application attempts to fetch quotes from the [Quotable API](https://api.quotable.io/random).

## Flask Documentation

For more information about Flask:
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask Quick Start Guide](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- [Flask Tutorial](https://flask.palletsprojects.com/en/2.3.x/tutorial/)

 