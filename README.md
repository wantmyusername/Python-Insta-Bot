# Python Insta Bot — Generador de imágenes

Script en **Python** que genera una **imagen con formato Instagram** a partir de un texto: lee la primera línea de `contenido.txt`, la **envuelve** para ajustarla al lienzo y la **dibuja** sobre una imagen de fondo, guardando `hola.png`. Además, **elimina la primera línea de `dias.txt`** para ir consumiendo una lista (p. ej. de días/frases) sin repetir.

## Cómo funciona

1. Lee la **primera línea** de `contenido.txt`.
2. Ajusta el texto con `textwrap.wrap(texto, width=25)`.
3. Abre la imagen base (p. ej. `assets/1.png`) y dibuja el texto con **Arial 35**.
4. Guarda el resultado como **`hola.png`**.
5. Borra la **primera línea** de `dias.txt`.

## Requisitos

- **Python 3** + **Pillow**:
  ```bash
  pip install pillow
  ```
- **Windows** (las rutas del script están hardcodeadas a Windows, ver *Notas*).
- Estos archivos en la carpeta del script:
  - `contenido.txt` — texto a dibujar.
  - `dias.txt` — lista de líneas (se van consumiendo).
  - la **imagen base** (por defecto en `…/assets/1.png`).

## Uso

```bash
pip install pillow
python Generar.py
```

**Salida:** `hola.png` (la imagen generada).

## Notas / a mejorar

- ⚠️ **Rutas hardcodeadas de Windows**: `E:\Bots\Instagram Python Generador\assets\1.png` y `C:\Windows\Fonts\Arial.ttf`. No es portable → usa **rutas relativas** y `os.path.join(...)`, y una fuente incluida en `assets/`.
- `draw.textsize()` está **deprecado** en Pillow ≥ 10; usar `draw.textbbox()` o `font.getlength()`.
- Solo procesa la **primera línea** de `contenido.txt` (si quieres varias imágenes, itera).
- `MAX_W, MAX_H = 300, 300` no limitan realmente el dibujo (se usan solo en el cálculo de la posición X).
- El script **no publica** nada: solo **genera la imagen** (el posteo/automatización de Instagram iría aparte).

## Licencia

Sin licencia definida. Script de ejemplo; úsalo bajo tu responsabilidad.
