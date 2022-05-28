mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"colemcintosh6@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "[theme]

primaryColor='#000'
backgroundColor='#D8D8F6'
secondaryBackgroundColor='#B18FCF'
textColor='#000'
font='sans serif'"
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml