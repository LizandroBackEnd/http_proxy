
# Proxy HTTP con Logging en Python usando Flask

Este proyecto consiste en un proxy HTTP básico implementado en Python utilizando Flask. El proxy registra las solicitudes entrantes y las respuestas del servidor destino usando logging, lo cual es útil para propósitos de depuración y análisis.

## Requisitos

- Python 3.x instalado (se recomienda la versión más reciente).
- `pip` instalado para la gestión de paquetes de Python.

## Instalación

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/LizandroBackEnd/http_proxy.git
   cd proxy
   ```

2. **Configurar un Entorno Virtual (Opcional pero recomendado):**

   ```bash
   python -m venv myenv
   # En Windows: .\myenv\Scripts\activate
   # En Linux/macOS: source myenv/bin/activate
   ```

3. **Instalar Dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Ejecutar el Proxy:**

   ```bash
   python proxy.py
   ```

   - El proxy comenzará a ejecutarse en `http://127.0.0.1:8080`.
   - Asegúrate de dejar esta ventana de la terminal abierta mientras usas el proxy.

2. **Enviar Solicitudes al Proxy:**

   - Puedes enviar solicitudes al proxy usando tu navegador web o herramientas como `curl` o Postman.
   - Ejemplo usando `curl` en la terminal:

     ```bash
     curl -X GET http://127.0.0.1:8080/path
     ```

## Ejemplo de Logs

- Cuando envíes solicitudes al proxy, los logs de las solicitudes y las respuestas se mostrarán en la consola donde ejecutaste `proxy.py`.
- Verás mensajes informativos que detallan cada solicitud entrante, los headers y el cuerpo de las respuestas.

Ejemplo de salida de logs:

```
INFO:root:Solicitud entrante: GET http://127.0.0.1:8080/path
INFO:root:Header de solicitud: Host: 127.0.0.1:8080
INFO:root:Header de solicitud: User-Agent: curl/7.68.0
INFO:root:Respuesta del servidor: 200 OK
INFO:root:Header de respuesta: Content-Type: text/html; charset=UTF-8
INFO:root:Cuerpo de la respuesta: <html>...</html>
```

## Detalles Técnicos

- El proxy está implementado con Flask, un framework web ligero para Python.
- Se utiliza `requests` para hacer las solicitudes al servidor destino y para manejar las respuestas.
- El logging se configura para registrar información detallada sobre cada solicitud y respuesta, facilitando la depuración y el análisis del tráfico.

