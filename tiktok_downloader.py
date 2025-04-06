#!/usr/bin/env python
import os
import sys
import argparse
from datetime import datetime
import yt_dlp

def descargar_videos_tiktok(username, directorio_salida=None, limite=None):
    """
    Descarga videos de TikTok de un usuario específico usando yt-dlp
    
    Args:
        username: Nombre de usuario de TikTok (sin @)
        directorio_salida: Directorio donde guardar los videos (por defecto: ./downloaded/username)
        limite: Número máximo de videos a descargar (por defecto: todos)
    """
    # Configurar el directorio de salida
    if directorio_salida is None:
        directorio_salida = os.path.join(os.getcwd(), "downloaded", username)
    
    # Asegurar que el directorio exista
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)
    
    # URL del perfil de TikTok
    tiktok_url = f"https://www.tiktok.com/@{username}"
    
    print(f"> Descargando videos de: @{username}")
    print(f"> Directorio de salida: {directorio_salida}")
    if limite:
        print(f"> Límite: {limite} videos")
    
    # Opciones para yt-dlp
    opciones = {
        'format': 'best',  # Mejor calidad disponible
        'outtmpl': os.path.join(directorio_salida, '%(id)s.%(ext)s'),  # Formato de nombre de archivo
        'restrictfilenames': True,  # Evitar caracteres especiales en nombres de archivo
        'nooverwrites': False,  # No sobrescribir archivos existentes
        'no_warnings': False,
        'ignoreerrors': True,  # Ignorar errores y continuar
        'quiet': False,
        'verbose': False,
        'force_generic_extractor': False,
        'progress': True,  # Mostrar progreso de descarga
        'prefer_ffmpeg': True,  # Usar ffmpeg si está disponible
        'extract_flat': False,
        'cookiefile': None,
        'nocheckcertificate': True,  # No verificar certificados SSL
    }
    
    # Si hay un límite, añadirlo a las opciones
    if limite:
        opciones['playlist_items'] = f'1-{limite}'
    
    # Iniciar descarga
    try:
        print("> Iniciando descarga con yt-dlp (esto puede tardar unos momentos)...")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            # Descargar información y videos
            info = ydl.extract_info(tiktok_url, download=True)
            
            # Verificar si es una lista de reproducción o un solo video
            if '_type' in info and info['_type'] == 'playlist':
                print(f"> Descarga completada: {len(info['entries'])} videos")
            else:
                print("> Descarga completada: 1 video")
                
    except Exception as e:
        print(f"! Error durante la descarga: {str(e)}")
        sys.exit(1)
    
    print(f"> Todos los videos han sido descargados en: {directorio_salida}")

def main():
    parser = argparse.ArgumentParser(description='Descarga videos de TikTok usando yt-dlp')
    parser.add_argument('username', help='Nombre de usuario de TikTok (sin @)')
    parser.add_argument('-o', '--output', help='Directorio de salida (opcional)')
    parser.add_argument('-l', '--limit', type=int, help='Número máximo de videos a descargar')
    
    # Si no hay argumentos, mostrar ayuda
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()
    
    # Ejecutar función principal
    descargar_videos_tiktok(args.username, args.output, args.limit)

if __name__ == "__main__":
    main()