# ARES PRO — Passive Bug Bounty Framework

ARES es un framework **pasivo y legal** para reconocimiento, mapeo y OSINT en Bug Bounty, diseñado para ser liviano, modular y seguro.

## Filosofía
ARES NO explota, NO ataca y NO daña objetivos. Su objetivo es automatizar el flujo de trabajo seguro y legal:
**Reconocimiento → Mapeo de superficie → Controles pasivos → Evidencia → Informe**

## Estructura del Proyecto
```text
ARES/
├── cli/            # Interfaz de línea de comandos
├── core/           # Motor central y orquestación
├── agents/         # Agentes especializados (Reportes, etc.)
├── modules/        # Módulos de escaneo (Recon, Web, OSINT)
├── utils/          # Utilidades y validadores
├── config/         # Configuración del sistema
├── data/           # Almacenamiento de resultados crudos
└── reports/        # Informes generados (JSON, Markdown)
```

## Instalación
```bash
git clone https://github.com/juanibarrasec-tech/ARES.git
cd ARES
pip install -r requirements.txt
```

## Uso
Para realizar un escaneo básico:
```bash
python cli/ares.py -t example.com
```

Para activar el modo automático (incluye OSINT extendido):
```bash
python cli/ares.py -t example.com --auto
```

## Módulos Incluidos
- **Recon**: Descubrimiento de subdominios y consulta WHOIS.
- **Web**: Análisis de encabezados de seguridad.
- **OSINT**: Sugerencias de Google Dorks, Shodan y Wayback Machine.
- **Reporting**: Generación automática de informes en formato JSON y Markdown.

## Aviso Legal
Usar SÓLO en:
1. Programas de recompensas por errores (Bug Bounty) autorizados.
2. Tus propios laboratorios.
3. Objetivos con permiso escrito explícito.

Usted es responsable del modo en que utiliza ARES. El framework cumple con las reglas de plataformas como HackerOne y Bugcrowd al ser 100% pasivo.

---
**ARES PRO — Creado para verdaderos cazadores.**
