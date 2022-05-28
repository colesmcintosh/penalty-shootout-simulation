mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"colemcintosh6@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "[theme]
primaryColor = ‘#84a3a7’
backgroundColor = ‘#EFEDE8’
secondaryBackgroundColor = ‘#fafafa’
textColor= ‘#424242’
font = ‘sans serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml