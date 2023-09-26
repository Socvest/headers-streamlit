import streamlit as st
from streamlit_javascript import st_javascript
from streamlit.web.server.websocket_headers import _get_websocket_headers

headers = _get_websocket_headers()
st.write(headers)

script = """await (async function () {
        var pairs = document.cookie.split(";");
        var cookies = {};
        for (var i = 0; i < pairs.length; i++) {
            var pair = pairs[i].split("=");
            cookies[(pair[0]+'').trim()] = unescape(pair.slice(1).join('='));
        }
        return cookies;
    })()
    """

st.write(st_javascript(script))
