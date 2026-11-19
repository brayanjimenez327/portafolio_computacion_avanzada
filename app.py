"""
Portafolio de aplicaciones — Computación Avanzada (ET0197)
Brayan Jiménez Ospina · Institución Universitaria Pascual Bravo

Reúne en una sola página las apps de Streamlit desarrolladas en las sesiones
del curso. Cada tarjeta tiene una ilustración propia (SVG dibujado en código,
sin archivos de imagen), el título, la sesión, la categoría y el enlace a la
app desplegada en Streamlit Community Cloud.
"""

import streamlit as st

st.set_page_config(
    page_title="Portafolio de Aplicaciones · Computación Avanzada",
    page_icon="🧠",
    layout="wide",
)

URL_CURSO = "https://sites.google.com/view/computacinavanzada/inicio"

# ---------------------------------------------------------------------------
# Ilustraciones (SVG en línea). Paleta común para que todas se vean del mismo
# sistema: fondo claro, trazos oscuros y un color de acento por tarjeta.
# ---------------------------------------------------------------------------
SVG = {
    "frutas": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <circle cx="38" cy="58" r="20" fill="#e4572e"/><rect x="36" y="33" width="4" height="9" fill="#5b3a29"/>
  <circle cx="122" cy="40" r="15" fill="#f2a541"/><circle cx="118" cy="82" r="14" fill="#9bc53d"/>
  <line x1="58" y1="58" x2="107" y2="42" stroke="#334" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="58" y1="58" x2="104" y2="80" stroke="#334" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="70" y="44" font-size="10" fill="#334" font-family="sans-serif">d₁</text>
  <text x="76" y="80" font-size="10" fill="#334" font-family="sans-serif">d₂</text>
</svg>""",
    "gradiente": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <g fill="none" stroke="#5c7cfa" stroke-width="1.6">
    <ellipse cx="105" cy="62" rx="48" ry="34"/><ellipse cx="105" cy="62" rx="32" ry="22"/>
    <ellipse cx="105" cy="62" rx="16" ry="11"/>
  </g>
  <polyline points="28,18 52,30 70,42 84,51 94,57 100,60 105,62" fill="none" stroke="#e4572e" stroke-width="2.4"/>
  <circle cx="28" cy="18" r="4" fill="#f2a541"/><circle cx="105" cy="62" r="4" fill="#2b8a3e"/>
</svg>""",
    "anomalias": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <g fill="#4dabf7">
    <circle cx="40" cy="70" r="4"/><circle cx="52" cy="62" r="4"/><circle cx="48" cy="78" r="4"/>
    <circle cx="62" cy="70" r="4"/><circle cx="58" cy="56" r="4"/><circle cx="70" cy="62" r="4"/>
    <circle cx="66" cy="80" r="4"/><circle cx="76" cy="72" r="4"/>
  </g>
  <circle cx="128" cy="28" r="6" fill="#e4572e"/><circle cx="128" cy="28" r="12" fill="none" stroke="#e4572e" stroke-width="2"/>
  <text x="96" y="96" font-size="14" font-weight="bold" fill="#334" font-family="monospace">O(n)</text>
</svg>""",
    "datos": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <g stroke="#334" stroke-width="1.4" fill="#fff">
    <rect x="18" y="22" width="56" height="66"/>
    <line x1="18" y1="38" x2="74" y2="38"/><line x1="18" y1="54" x2="74" y2="54"/><line x1="18" y1="70" x2="74" y2="70"/>
    <line x1="46" y1="22" x2="46" y2="88"/>
  </g>
  <rect x="47" y="55" width="26" height="14" fill="#ffd8a8"/>
  <text x="54" y="66" font-size="10" fill="#e4572e" font-family="sans-serif">NaN</text>
  <path d="M84 55 h22" stroke="#334" stroke-width="2" marker-end="url(#f)"/>
  <defs><marker id="f" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#334"/></marker></defs>
  <g fill="#69db7c"><rect x="114" y="62" width="9" height="22"/><rect x="126" y="46" width="9" height="38"/><rect x="138" y="54" width="9" height="30"/></g>
</svg>""",
    "rios": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <path d="M0 70 Q20 60 40 70 T80 70 T120 70 T160 70 V110 H0 Z" fill="#74c0fc"/>
  <path d="M0 84 Q20 76 40 84 T80 84 T120 84 T160 84 V110 H0 Z" fill="#339af0"/>
  <rect x="118" y="18" width="8" height="64" fill="#495057"/>
  <g stroke="#fff" stroke-width="2"><line x1="118" y1="30" x2="126" y2="30"/><line x1="118" y1="44" x2="126" y2="44"/><line x1="118" y1="58" x2="126" y2="58"/></g>
  <circle cx="40" cy="30" r="10" fill="#e4572e"/><path d="M40 40 L34 52 L46 52 Z" fill="#e4572e"/>
</svg>""",
    "regresion": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <line x1="20" y1="92" x2="148" y2="92" stroke="#334" stroke-width="1.5"/><line x1="20" y1="92" x2="20" y2="14" stroke="#334" stroke-width="1.5"/>
  <g fill="#4dabf7"><circle cx="34" cy="80" r="3.5"/><circle cx="48" cy="72" r="3.5"/><circle cx="58" cy="76" r="3.5"/><circle cx="70" cy="60" r="3.5"/>
  <circle cx="84" cy="58" r="3.5"/><circle cx="96" cy="46" r="3.5"/><circle cx="110" cy="44" r="3.5"/><circle cx="124" cy="32" r="3.5"/><circle cx="136" cy="28" r="3.5"/></g>
  <line x1="26" y1="86" x2="144" y2="24" stroke="#e4572e" stroke-width="2.4"/>
  <text x="30" y="26" font-size="11" fill="#334" font-family="serif" font-style="italic">ŷ = wx + b</text>
</svg>""",
    "series": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <polyline points="10,70 22,52 34,68 46,48 58,62 70,42 82,58 94,38" fill="none" stroke="#334" stroke-width="2"/>
  <polyline points="94,38 106,52 118,32 130,46 142,26 152,40" fill="none" stroke="#e4572e" stroke-width="2.4" stroke-dasharray="5 3"/>
  <path d="M94 30 L106 42 L118 22 L130 34 L142 14 L152 28 L152 52 L142 38 L130 58 L118 42 L106 62 L94 46 Z" fill="#e4572e" opacity=".15"/>
  <line x1="94" y1="12" x2="94" y2="96" stroke="#868e96" stroke-dasharray="2 3"/>
  <circle cx="22" cy="90" r="5" fill="#69db7c"/><text x="31" y="94" font-size="9" fill="#334" font-family="sans-serif">IoT</text>
</svg>""",
    "aire": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <path d="M40 60 a18 18 0 0 1 10 -32 a24 24 0 0 1 44 6 a16 16 0 0 1 4 32 Z" fill="#ced4da"/>
  <g fill="#868e96"><circle cx="54" cy="78" r="3"/><circle cx="70" cy="86" r="2"/><circle cx="84" cy="76" r="3.5"/><circle cx="98" cy="88" r="2.5"/><circle cx="62" cy="96" r="2"/></g>
  <text x="108" y="44" font-size="12" font-weight="bold" fill="#e4572e" font-family="sans-serif">PM2.5</text>
  <text x="110" y="62" font-size="12" font-weight="bold" fill="#f2a541" font-family="sans-serif">PM10</text>
</svg>""",
    "termica": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <rect x="34" y="14" width="16" height="62" rx="8" fill="#fff" stroke="#334" stroke-width="2"/>
  <circle cx="42" cy="84" r="14" fill="#e4572e" stroke="#334" stroke-width="2"/>
  <rect x="38" y="40" width="8" height="40" fill="#e4572e"/>
  <path d="M104 26 q-16 24 0 34 q16 -10 0 -34 z" fill="#4dabf7"/>
  <text x="76" y="92" font-size="12" fill="#334" font-family="sans-serif">T + HR → ST</text>
</svg>""",
    "lluvia": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <path d="M22 44 a12 12 0 0 1 8 -22 a18 18 0 0 1 32 4 a11 11 0 0 1 2 18 Z" fill="#adb5bd"/>
  <g stroke="#339af0" stroke-width="2.4" stroke-linecap="round"><line x1="30" y1="54" x2="26" y2="64"/><line x1="44" y1="54" x2="40" y2="64"/><line x1="58" y1="54" x2="54" y2="64"/></g>
  <line x1="80" y1="92" x2="152" y2="92" stroke="#334"/><line x1="80" y1="92" x2="80" y2="16" stroke="#334"/>
  <path d="M80 88 C104 88 108 86 116 54 C124 22 128 20 152 20" fill="none" stroke="#e4572e" stroke-width="2.4"/>
  <line x1="80" y1="54" x2="152" y2="54" stroke="#868e96" stroke-dasharray="3 3"/>
  <text x="124" y="66" font-size="9" fill="#334" font-family="sans-serif">0.5</text>
</svg>""",
    "suelo": """
<svg viewBox="0 0 160 110" xmlns="http://www.w3.org/2000/svg">
  <rect width="160" height="110" rx="10" fill="#f3f6fa"/>
  <path d="M10 80 Q40 66 80 74 T150 76 V100 H10 Z" fill="#8d6e63"/>
  <path d="M46 74 V44" stroke="#2b8a3e" stroke-width="3"/>
  <path d="M46 56 q-16 -4 -18 -18 q14 2 18 18 z" fill="#69db7c"/><path d="M46 50 q14 -6 18 -20 q-16 2 -18 20 z" fill="#40c057"/>
  <g font-family="sans-serif" font-size="9" fill="#334">
    <rect x="96" y="20" width="10" height="10" fill="#d95f02"/><text x="110" y="28">Baja</text>
    <rect x="96" y="36" width="10" height="10" fill="#e6ab02"/><text x="110" y="44">Media</text>
    <rect x="96" y="52" width="10" height="10" fill="#1b9e77"/><text x="110" y="60">Alta</text>
  </g>
</svg>""",
}

# ---------------------------------------------------------------------------
# Catálogo de apps: una entrada por sesión del curso
# ---------------------------------------------------------------------------
APPS = [
    {"titulo": "¿Qué fruta es más parecida?", "sesion": "Sesión 2 · Vectores y matrices",
     "categoria": "Clasificación", "img": "frutas",
     "desc": "Distancia euclidiana entre vectores [peso, diámetro, dulzor]; incluye la pera agregada en clase.",
     "url": "https://frutasapppy-lttprfq8gtr2lgfxolwpwh.streamlit.app/"},
    {"titulo": "Descenso de gradiente interactivo", "sesion": "Sesión 3 · Cálculo aplicado",
     "categoria": "Optimización", "img": "gradiente",
     "desc": "Trayectoria del descenso sobre f(x, y) = (x−3)² + (y+2)² variando η y el punto inicial.",
     "url": "https://appgradientpy-p2ihfrelxkd3v7uimpcfuq.streamlit.app/"},
    {"titulo": "Detector de anomalías", "sesion": "Sesión 4 · Lógica, Big-O y vectorización",
     "categoria": "Big-O", "img": "anomalias",
     "desc": "Reglas de negocio, costo computacional y versión vectorizada con NumPy.",
     "url": "https://pruebaclase3-nrrrhgttdbvnbtfsv2yfn4.streamlit.app/"},
    {"titulo": "Preparación de datos de sensores", "sesion": "Sesión 5 · Preparación de datos",
     "categoria": "Datos", "img": "datos",
     "desc": "Tipos de datos, faltantes, outliers (IQR), normalización y particiones train/val/test.",
     "url": "https://sesion4-cwhqdp8iklwde3vcjrhtmg.streamlit.app/"},
    {"titulo": "Nivel de ríos y quebradas", "sesion": "Sesión 6 · Datos reales (Cornare)",
     "categoria": "Datos reales", "img": "rios",
     "desc": "Estación 43 · Río Santo Domingo (San Francisco, Antioquia) con datos de la API MARCO.",
     "url": "https://estacion-geolocalizada-2wktgsfugoxpzhhwnwrbsm.streamlit.app/"},
    {"titulo": "Regresión — conceptos clave", "sesion": "Sesión 7 · Regresión lineal",
     "categoria": "Regresión", "img": "regresion",
     "desc": "Regresión simple y múltiple, función de costo, gradiente y métricas R², MAE y RMSE.",
     "url": "https://sesion6-lzunxayznqmiawtp4pnuvt.streamlit.app/"},
    {"titulo": "Series de tiempo — sensor IoT", "sesion": "Sesión 8 · Series de tiempo",
     "categoria": "Forecasting", "img": "series",
     "desc": "ARIMA, SARIMA y Holt-Winters sobre la lectura simulada de un sensor.",
     "url": "https://sesion8-hdevunf4mmiwt9hangjy83.streamlit.app/"},
    {"titulo": "Predictor de calidad del aire", "sesion": "Aplicación · Calidad del aire",
     "categoria": "Forecasting", "img": "aire",
     "desc": "Pronóstico de PM2.5 y PM10 cargando los modelos .pkl entrenados en Colab.",
     "url": "https://apppronosticocornarepy-b4emvpxadbvxcdbp88ydu9.streamlit.app/"},
    {"titulo": "Predictor de sensación térmica", "sesion": "Sesión 10 · IoT (ESP32 + InfluxDB)",
     "categoria": "Regresión", "img": "termica",
     "desc": "Temperatura y humedad desde InfluxDB para predecir la sensación térmica.",
     "url": "https://sesion10-xlfwvrkw6dtjkylnurjqwy.streamlit.app/"},
    {"titulo": "¿Lloverá mañana?", "sesion": "Sesión 11 · Regresión logística",
     "categoria": "Clasificación", "img": "lluvia",
     "desc": "Probabilidad de lluvia con la sigmoide, umbral, matriz de confusión y métricas.",
     "url": "https://appregresionlogisticapy-yi3hvuv9ycwyryvbtnhftn.streamlit.app/"},
    {"titulo": "Diagnóstico de fertilidad del suelo", "sesion": "Aplicación KNN · AGROSAVIA",
     "categoria": "Clasificación", "img": "suelo",
     "desc": "KNN para clasificar suelos en fertilidad baja, media o alta con datos abiertos.",
     "url": "https://gepzvtag3tszlvoch85pwv.streamlit.app/"},
]

COLOR_CATEGORIA = {
    "Clasificación": "#1971c2", "Optimización": "#7048e8", "Big-O": "#c2255c",
    "Datos": "#2b8a3e", "Datos reales": "#2b8a3e", "Regresión": "#e8590c",
    "Forecasting": "#0c8599",
}

# ---------------------------------------------------------------------------
# Estilos de las tarjetas
# ---------------------------------------------------------------------------
st.markdown(
    """
<style>
.card {border: 1px solid rgba(128,128,128,.25); border-radius: 14px; padding: 14px;
       margin-bottom: 18px; background: rgba(255,255,255,.02); height: 100%;}
.card svg {width: 100%; height: auto; border-radius: 10px;}
.card h3 {font-size: 1.12rem; margin: .6rem 0 .1rem 0; line-height: 1.3;}
.card h3 a {text-decoration: none;}
.card .ses {font-size: .82rem; opacity: .75; margin-bottom: .35rem;}
.card .desc {font-size: .9rem; margin: .35rem 0 .6rem 0;}
.card .tag {display: inline-block; font-size: .7rem; font-weight: 700; letter-spacing: .04em;
            text-transform: uppercase; color: #fff; padding: 2px 8px; border-radius: 6px;}
.card .dom {font-size: .75rem; opacity: .6; word-break: break-all; margin-top: .4rem;}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Encabezado y barra lateral
# ---------------------------------------------------------------------------
st.title("Portafolio de aplicaciones — Computación Avanzada")
st.caption("Brayan Jiménez Ospina · Ingeniería de Software · Institución Universitaria Pascual Bravo")

with st.sidebar:
    st.subheader("Computación Avanzada (ET0197)")
    st.write(
        "Aplicaciones desarrolladas en las sesiones del curso: álgebra lineal, cálculo, "
        "complejidad algorítmica, preparación de datos, regresión, series de tiempo, IoT "
        "y clasificación, desplegadas en Streamlit Community Cloud."
    )
    st.write(f"Página del curso: [Compu Avanzada]({URL_CURSO})")
    categorias = sorted({a["categoria"] for a in APPS})
    filtro = st.multiselect("Filtrar por categoría", categorias, default=categorias)

st.divider()

# ---------------------------------------------------------------------------
# Rejilla de tarjetas (3 por fila)
# ---------------------------------------------------------------------------
apps_visibles = [a for a in APPS if a["categoria"] in filtro]
for inicio in range(0, len(apps_visibles), 3):
    columnas = st.columns(3)
    for col, app in zip(columnas, apps_visibles[inicio:inicio + 3]):
        dominio = app["url"].replace("https://", "").rstrip("/")
        color = COLOR_CATEGORIA.get(app["categoria"], "#495057")
        # El SVG se pasa en una sola línea: una línea en blanco dentro del HTML
        # haría que Markdown cerrara el bloque y mostrara el código como texto.
        svg = " ".join(SVG[app["img"]].split())
        html = (
            f'<div class="card">{svg}'
            f'<h3><a href="{app["url"]}" target="_blank">{app["titulo"]}</a></h3>'
            f'<div class="ses">{app["sesion"]}</div>'
            f'<span class="tag" style="background:{color}">{app["categoria"]}</span>'
            f'<div class="desc">{app["desc"]}</div>'
            f'<div class="dom">{dominio}</div></div>'
        )
        with col:
            st.markdown(html, unsafe_allow_html=True)

if not apps_visibles:
    st.info("Selecciona al menos una categoría en la barra lateral.")
