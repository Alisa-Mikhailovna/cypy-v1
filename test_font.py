import os
from cypy.core.utils import _download_noto_font
from cypy.core.config import ASSETS_DIR

def main():
    font = _download_noto_font('korean')
    print(f'Downloaded: {font}')
    
    jap_font = os.path.join(ASSETS_DIR, 'KosugiMaru.ttf')
    print(f'Japanese font exists: {os.path.exists(jap_font)}')

if __name__ == '__main__':
    main()
