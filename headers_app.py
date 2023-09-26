from streamlit.web.server.websocket_headers import _get_websocket_headers

headers = _get_websocket_headers()
st.write(headers)
