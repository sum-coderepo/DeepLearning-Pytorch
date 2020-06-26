#!/bin/bash
# The ping job will help keep awesome-streamlit.org alive.
# See https://lnx.azurewebsites.net/python-app-on-azure-web-apps-frequently-restarts/
# python "ping_test.py" &
# top -d 60 -b &
echo "Invoked Streamlit shell" 
cat app.py
streamlit run app.py
