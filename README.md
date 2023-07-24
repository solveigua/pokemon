# pokémon data viz website

<img width="1016" alt="image" src="https://user-images.githubusercontent.com/70148072/228538959-e56dca93-2311-4438-abbc-a92798096755.png">

## Deployment

Deployed [here](https://pokemon-ee8l.onrender.com/) with render.

## Running Locally

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

   Can also be runned using gunicorn:

      ```
      gunicorn app:server -b :8000
      ```

## Tech stack

Dataset from kaggle ([source](https://www.kaggle.com/datasets/rounakbanik/pokemon)), read from csv file using **pandas**

**Dash** for python - an open source framework specifically for creating data visualization interfaces.

Three technologies constitute the core of Dash:

1. **Flask** -web server functionality
2. **React.js** user interface of the web page
3. **Plotly.js** generates the charts

I chose Dash as it is something new I haven’t tried before, it is great for interactive visualizations, and has a component based architecture I am familiar with.
The idea for the web page was inspired by my DataViz course at UCT (Univeristy of Cape Town) :)

## Performance

The website is hosted by render with a free plan which makes it a little bit slow. The data is stored at a local csv file as using an API was a bit out of scope for this personal project.
