# TikTok Downloader

Herramienta simple para descargar videos de perfiles de TikTok sin marcas de agua utilizando Python.

## Requisitos

- Python 3.6 o superior
- Biblioteca `yt-dlp` (se puede instalar con `pip install yt-dlp`)

## Instalación

1. Clona o descarga este repositorio
2. Instala las dependencias:
   ```
   pip install yt-dlp
   ```

## Uso

### Descargar todos los videos de un perfil

```
python tiktok_downloader.py nombreusuario
```

Por ejemplo:
```
python tiktok_downloader.py movistarplusdeportes
```

### Opciones adicionales

- Limitar el número de videos a descargar:
  ```
  python tiktok_downloader.py nombreusuario -l 10
  ```

- Especificar un directorio de salida personalizado:
  ```
  python tiktok_downloader.py nombreusuario -o "C:\MisVideos\TikTok"
  ```

## Características

- Descarga videos sin marca de agua
- Organiza automáticamente los videos en carpetas por usuario
- Mantiene la mejor calidad disponible
- Manejo de errores robusto

## Estructura

Los videos descargados se guardan en la carpeta `downloaded/nombreusuario`.
Cada video se nombra según su ID único en TikTok.

## Licencia

<p align="center">
	Repositorio generado por <a href="https://github.com/virtuanista" target="_blank">virtu 🎣</a>
</p>

<p align="center">
	<img src="https://open.soniditos.com/cat_footer.svg" />
</p>

<p align="center">
	Copyright &copy; 2025
</p>

<p align="center">
	<a href="/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
