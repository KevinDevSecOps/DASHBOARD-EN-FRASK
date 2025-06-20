# 🔥 **CyberDash: Dashboard Flask para Pentesters & SOC Analysts** 🔥  

**¿Cansado de dashboards genéricos?** Aquí tienes uno **hecho con ❤️ por KevinDevSecOps
para la comunidad cibernética**, con código tan afilado como una navaja suiza IoT.  

--- 
¿Cansado de dashboards genéricos que parecen hechos en WordPress en 2008?** Bienvenido a **CyberDash**, una herramienta de visualización y análisis de datos de ciberseguridad construida con Flask, diseñada para **pentesters, SOC analysts, red teams y cualquiera que valore la eficiencia sobre el humo**.  

---

## **🔥 ¿Por qué CyberDash?**  

Porque no todos los dashboards son iguales. Este está diseñado para:  

✅ **Analizar logs masivos** (Suricata, Zeek, Nginx) sin colgar el navegador.  
✅ **Visualizar IOCs** (Indicadores de Compromiso) en gráficos interactivos que no dan vergüenza.  
✅ **Integrar APIs clave** (Shodan, VirusTotal, MITRE ATT&CK) sin perder tiempo en documentación mal escrita.  
✅ **Desplegar en segundos** (Docker-ready) porque tu tiempo vale más que pelearte con dependencias.  

**Si tu dashboard actual no te hace más rápido, más inteligente o más peligroso… ¿para qué lo usas?**  

---

## **🛠️ Tecnologías Usadas (Sin Relleno)**  

| **Categoría**       | **Stack Real** (No "Hello World") |  
|---------------------|-----------------------------------|  
| **Backend**         | Flask + Gunicorn + Redis (Para APIs rápidas, no tutoriales) |  
| **Frontend**        | Bootstrap 5 + Plotly.js + Vanilla JS (Porque no todo necesita React) |  
| **Autenticación**   | JWT + OAuth2 (Opcional, para los que no confían en nadie) |  
| **Base de Datos**   | PostgreSQL (O SQLite si vas rápido, no juzgamos) |  
| **Deployment**      | Docker + Nginx (Porque si no usas contenedores en 2024, ¿qué haces con tu vida?) |  

---

## **🚀 ¿Cómo se Usa? (Modo Guerra)**  

### **Opción 1: Docker (Recomendado para Humanos)**  
```bash
git clone https://github.com/tu-usuario/cyberdash.git && cd cyberdash  
docker-compose up --build -d  # Listo. Accede en https://localhost:8443  
```  

### **Opción 2: Manual (Para los que Les Gusta Sufrir)**  
```bash
python -m venv .venv && source .venv/bin/activate  # Linux/Mac  
pip install -r requirements-pro.txt  # Dependencias de verdad, no juguetes  
gunicorn --bind 0.0.0.0:5000 --reload app:app  # Boom, servido.  
```  

---

## **💡 Características que Importan (No "Features" de Relleno)**  

### **1. Visualización de Datos que No Apesta**  
- Gráficos interactivos de **tráfico de red** (con filtros por IP, puerto, protocolo).  
- Mapa geolocalizado de **amenazas** (usando MaxMind DB).  
- **Timeline de eventos** para investigar breaches sin perder la cordura.  

### **2. Parsers de Logs que No Te Harán Llorar**  
- Soporte para **Suricata, Zeek, Apache, Nginx** (sin configs absurdas).  
- Búsqueda de **IOCs** (hashes, IPs, dominios) en segundos.  

### **3. Integraciones con Herramientas Reales**  
- **Shodan**: Encuentra dispositivos IoT vulnerables antes que el atacante.  
- **VirusTotal**: Verifica hashes maliciosos sin abrir 50 pestañas.  
- **MITRE ATT&CK**: Mapea tácticas y técnicas usadas en ataques.  

---

## **📌 ¿Para Quién Es Esto?**  

✔ **Pentesters** que quieren visualizar datos de escaneos masivos.  
✔ **SOC Teams** que necesitan dashboards personalizados (no los de SIEM comerciales).  
✔ **Red Teams** que odian perder tiempo en herramientas lentas.  
✔ **Cualquiera que prefiera código sobre PowerPoint**.  

---

## **📜 Licencia MIT (Sin Dogmatismos)**  

Usa, modifica, distribuye… **haz lo que quieras**, pero:  
- **Incluye el copyright original** (es lo mínimo).  
- **No nos culpes** si algo explota (probaste el código antes, ¿no?).  

> *"El código abierto es como un cuchillo: útil en manos expertas, peligroso en las equivocadas."*  

---

## **🤝 ¿Quieres Contribuir?**  

1. **Haz fork y clona el repo**.  
2. **Codea como si tu reputación dependiera de ello**.  
3. **Envía un PR con pruebas reales** (no "funciona en mi máquina").  

**Recompensa**: Tu nombre en el README y el respeto de la comunidad.  

---

### **🎯 ¿Por qué Este Proyecto?**  
Porque después de **8 años en ciberseguridad**, ya estaba harto de herramientas que:  
- Son lentas.  
- Tienen UIs de los 90.  
- No se pueden personalizar.  

**CyberDash es la respuesta.**  

--- 

**¿Listo para dejar de perder tiempo con dashboards que no sirven?** ⚡  

```markdown
🚀 **Descarga ahora**: [github.com/tu-usuario/cyberdash](https://github.com/tu-usuario/cyberdash)  
💬 **¿Preguntas?**: Abre un *issue* o únete a nuestro Discord.  
```  

---  
**"No es un dashboard. Es un multiplicador de fuerza."** 🏴‍☠️

## 🛠️ **Tech Stack Élite**  
- **Backend**: Flask + Gunicorn (porque Werkzeug es para jugar)  
- **Frontend**: Bootstrap 5 + Plotly.js (visualizaciones que intimidarían a Matrix)  
- **Autenticación**: JWT + OAuth2 (opcional, para los paranoicos)  
- **Database**: SQLAlchemy + PostgreSQL (o SQLite si vas rápido)  
- **Deployment**: Docker + Kubernetes (si no usas contenedores, ¿en qué siglo vives?)  

```bash
 ✨ Si no te gusta Python, hay un Dockerfile listo para desplegar sin sufrir. ✨
```

---

## 🚀 **Instalación (Modo Hacker)**  

### **Opción 1: Docker (Recomendado)**  
```bash
git clone https://github.com/tu-usuario/cyberdash.git
cd cyberdash
docker-compose up --build -d
```
**Listo**. Accede en `https://localhost:8443` (con SSL, obvio).  

### **Opción 2: Manual (Para los puristas)**  
```bash
# 1. Entorno virtual (porque contaminar el sistema es de script kiddies)
python -m venv .venv && source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows

# 2. Dependencias (requiere Python 3.9+)
pip install -r requirements-pro.txt  # Incluye extras para análisis de red

# 3. Variables de entorno (configura tus secrets)
cp .env.example .env && nano .env

# 4. Ejecutar (con auto-reload para desarrollo)
gunicorn --bind 0.0.0.0:5000 --reload app:app
```

---

## 📊 **Features (Porque un dashboard debe dar miedo)**  

### **1. Visualización de Datos en Tiempo Real**  
- Gráficos interactivos de **tráfico de red** (Plotly + Packet sniffing opcional).  
- Mapa geolocalizado de **IPs sospechosas** (con MaxMind DB integrada).  

### **2. Análisis de Logs Avanzado**  
- Parseo de logs de **Nginx, Apache y Suricata** con Pandas.  
- Filtros dinámicos para **buscar IOCs** (Indicators of Compromise).  

### **3. Integraciones Élite**  
- **Shodan API**: Escaneo de dispositivos IoT vulnerables.  
- **VirusTotal**: Verificación de hashes maliciosos.  
- **MITRE ATT&CK**: Mapeo de tácticas detectadas.  

---

## 🧩 **Estructura del Proyecto**  

```markdown
cyberdash/
├── app/                      # Código principal
│   ├── auth/                 # Autenticación JWT
│   ├── data_processing/      # Análisis de logs y redes
│   ├── static/               # JS/CSS personalizados (con animaciones CSS3)
│   └── templates/            # HTML con Jinja2 (sí, también para hackers)
├── tests/                    # Tests con Selenium + pytest
├── Dockerfile                # Optimizado para Alpine (5MB)
└── docker-compose.yml        # Con Nginx + Redis para cache
```

---

## 🔐 **Security Hardening**  

- **Headers de Seguridad**: CSP, HSTS, XSS Protection preconfigurados.  
- **Rate Limiting**: Para evitar bruteforce (gracias, Flask-Limiter).  
- **Logging**: Auditoría de todas las acciones (sí, hasta tus clicks).  

```python
# Ejemplo: Endpoint con protección máxima
@app.route("/api/iocs", methods=["GET"])
@limiter.limit("10/minute")
@jwt_required()
def get_iocs():
    return jsonify({"iocs": ["CVE-2023-1234", "Malware:Emotet"]})
```

---

## 🤝 **Contribuir (Para los que no tienen vida)**  

1. Haz fork y clona el repo.  
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`.  
3. **Codea como si tu vida dependiera de ello**.  
4. Haz PR y discute mejoras.  

```markdown
✨ **Recompensas**:  
- Mención en el Hall of Fame del README.  
- Una cerveza virtual (o real si estamos en la misma ciudad).  
```

---

## 📜 **Licencia**  

**GPL-3.0** (Porque el código abierto es religión).  

--- 

> 🔥 **"No es un dashboard, es un arma de análisis masivo."**  
> — *Alguien en DEF CON*  

**¿Listo para hackear el mundo?** 🚀  

---

### 🎨 **Capturas de Pantalla**  

![Dashboard Preview](https://i.imgur.com/cyberdash-preview.png)  
*Interfaz diseñada para oscilar entre modo claro y oscuro (como tu ética).*  

---

✨ **Hecho con ❤️ para la comunidad de ciberseguridad. No para script kiddies.** ✨  

¿Quieres una función específica? ¡Abre un **issue** y lo discutimos!
