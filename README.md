# pokémon data viz website

<img width="1016" alt="image" src="https://user-images.githubusercontent.com/70148072/228538959-e56dca93-2311-4438-abbc-a92798096755.png">

### initializing and running

This app runs on python. (v3).

1. create virtual env

   ```
   python -m venv venv
   source venv/bin/activate
   # while in venv:
   pip install -r requirements.txt
   ```

2. run app

   ```
   python app.py
   ```

## Tech stack

Dataset from kaggle ([source](https://www.kaggle.com/datasets/rounakbanik/pokemon)), read from csv file using **pandas**

**Dash** for python - an open source framework specifically for creating data visualization interfaces.

Three technologies constitute the core of Dash:

1. **Flask** -web server functionality
2. **React.js** user interface of the web page
3. **Plotly.js** generates the charts

I chose Dash as it is something new I haven’t tried before, it is simple to use for this purpose and uses frameworks I am familiar with, like React.
The idea for the web page was inspired by my DataViz course at UCT (Univeristy of Cape Town) :)
