"""Streamlit dashboard for automation status."""
import streamlit as st
from pathlib import Path
from datetime import datetime

LOG_PATH = Path('logs/update_log.txt')
TRENDING = Path('TRENDING.md')

st.title('TrendSpire Automation Dashboard')

if LOG_PATH.exists():
    lines = LOG_PATH.read_text().splitlines()
    last = lines[-1] if lines else ''
    st.write('Last action:', last)
else:
    st.error('No log file found')

if TRENDING.exists():
    ts = TRENDING.stat().st_mtime
    st.write('TRENDING updated:', datetime.fromtimestamp(ts))
else:
    st.error('TRENDING.md missing')

st.markdown('### Recent Logs')
if LOG_PATH.exists():
    st.text(LOG_PATH.read_text()[-2000:])
