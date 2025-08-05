import os
from pathlib import Path

def organizar_descargas():
    # 1. Definir categorías de extensiones
    categorias = {
        'Imágenes': ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.svg'],
        'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.rtf', '.odt', '.xlsx', '.xls', '.csv', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'Audio': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a'],
        'Programas': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
        'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.sh', '.bat', '.ps1'],
    }
    
    # Carpeta objetivo (descargas del usuario)
    carpeta_objetivo = Path(r"D:\Platzi\Santander Academy\Cursor\organizador_archivos\Descargas")
    
    # Verificar si la carpeta existe
    if not carpeta_objetivo.exists():
        print(f"La carpeta {carpeta_objetivo} no existe.")
        return
    
    # 2. Listar todos los archivos de la carpeta objetivo
    archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]
    
    # Crear diccionario para mapear extensiones a categorías
    extension_a_categoria = {}
    for categoria, extensiones in categorias.items():
        for extension in extensiones:
            extension_a_categoria[extension.lower()] = categoria
    
    # Procesar cada archivo
    for archivo in archivos:
        # 3. Determinar extensión y categoría
        extension = archivo.suffix.lower()
        categoria = extension_a_categoria.get(extension, "Otros")
        
        # 4. Crear carpeta si no existe
        carpeta_destino = carpeta_objetivo / categoria
        carpeta_destino.mkdir(exist_ok=True)
        
        try:
            # 5. Mover el archivo
            nuevo_nombre = archivo.name
            # Manejar archivos con el mismo nombre
            contador = 1
            while (carpeta_destino / nuevo_nombre).exists():
                nombre_base = archivo.stem
                nuevo_nombre = f"{nombre_base}_{contador}{archivo.suffix}"
                contador += 1
            
            archivo.rename(carpeta_destino / nuevo_nombre)
            print(f"✓ {archivo.name} → {categoria}")
        except Exception as e:
            print(f"✗ Error al mover {archivo.name}: {str(e)}")
    
    print("\nOrganización completada!")

if __name__ == "__main__":
    organizar_descargas()