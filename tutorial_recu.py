import requests

# Define la URL a la que se realizará la solicitud GET
url = "http://vps-3701198-x.dattaweb.com:4000/snacks"

# Define el token de autorización que se incluirá en los encabezados de la solicitud
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"

# Define los encabezados de la solicitud, incluyendo el token de autorización
headers = {"Authorization": f"Bearer {token}"}

# Realiza la solicitud GET a la URL especificada, incluyendo los encabezados
response = requests.get(url, headers=headers)

# Imprime el código de estado de la respuesta HTTP (por ejemplo, 200 para éxito)
print(response)

# Imprime el contenido de la respuesta en formato binario
print(response.content)

# Imprime la URL a la que se hizo la solicitud (útil para verificar redirecciones)
print(response.url)

# Intenta interpretar el contenido de la respuesta como JSON y lo imprime
print(response.json())
