# pokémon viz website

### initializing and running

This app runs on python.

1. create virtual env

   ```
   python -m venv venv
   source v`nv/bin/activate
   # while in venv:
   python -m pip install dash==2.8.1 pandas==1.5.3 
   ```

2. run app

   ```
   python app.py
   ```

## Tech stack

Dataset from kaggle, read from csv file using \***\*\*\*\*\*\*\***pandas\***\*\*\*\*\*\*\***.

**Dash** for python - an open source framework specifically for creating data visualization interfaces.

Three technologies constitute the core of Dash:

1. **Flask** -web server functionality
2. **React.js** user interface of the web page
3. **Plotly.js** generates the charts

I chose Dash as it is something new I haven’t tried before, it is simple to use for this purpose and uses frameworks I am familiar with, like React.
