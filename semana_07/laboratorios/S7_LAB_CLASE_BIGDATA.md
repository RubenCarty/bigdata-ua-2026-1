# S7 — LABORATORIO DE CLASE: Limpieza de Datos en 35 Minutos
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 7: Diagnosticar y Limpiar un Dataset Real Sucio

---

> **Este laboratorio se realiza DURANTE la clase bajo supervisión del docente**
> **Tiempo: 35 minutos | Individual**
> **Herramienta: Google Colab — no requiere instalación**

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código** | ______________________________________________ |
| **Fecha** | ______________________________________________ |

---

## ACCESO AL ENTORNO (2 minutos)

1. Abre el navegador → **colab.research.google.com**
2. Inicia sesión con tu cuenta Google
3. Clic en **"+ Nuevo notebook"** → Renombrar: `S7_Lab_Clase_TuNombre`
4. Ejecuta en la primera celda:

```python
import pandas as pd
import numpy as np
import re
print(f"✅ pandas {pd.__version__} | numpy {np.__version__} | re ready")
```

**¿Ves ✅ con versiones? → Listo.**

---

## CONTEXTO

Eres Analista de Datos en **InkaLogística** — empresa de delivery B2B en Lima. El equipo comercial te envió un Excel con los datos de 15 clientes empresariales para cargar en el CRM. El archivo tiene errores típicos de ingreso manual. Tienes 30 minutos para limpiarlo y entregarlo listo.

---

## PASO 1 — Cargar el dataset sucio (5 min)

```python
# ============================================================
# CELDA 1: Dataset InkaLogística — ejecutar sin modificar
# ============================================================
import pandas as pd
import numpy as np
import re

# Dataset con errores típicos de ingreso manual
data_sucio = {
    "id_cliente": ["CL001","CL002","CL003","CL001","CL004","CL005",
                   "CL006","CL007","CL008","CL009","CL010",
                   "CL011","CL012","CL013","CL014"],
    "razon_social": [
        "BEMBOS SAC", "bembos sac", "Ripley Corp SA",
        "BEMBOS SAC", "METRO S.A.", "Oechsle SA",
        "FALABELLA PERU SA", "falabella peru sa", "InRetail S.A.",
        None, "La Victoria Burger SRL",
        "LAPODEROSA CORP", "PROMART HOMECENTER", "WONG SA", "TOTTUS SA"
    ],
    "ruc": [
        "20100128218", "20100128218", "20337564373",
        "20100128218", "2010012821X", "20522876543",
        "20349837528", "20349837528", "20511128716",
        "20123456789", "2011122345",   # RUC con solo 10 dígitos
        "20987654321", "20765432198", "20876543219", "20654321987"
    ],
    "distrito": [
        "Miraflores", "MIRAFLORES", "San Isidro",
        "Miraflores", "SAN ISIDRO", "surco",
        "San Borja", "san borja", "Los Olivos",
        "SJL", "La Victoria",
        "ATE", "San Juan de Lurigancho", "SURCO", "Los Olivos"
    ],
    "telefono": [
        "+51 1 447-8800", "014478800", "01-441-9000",
        "+51 1 447-8800", "999", "+51(1)477-2400",
        "01 618 8000", "01-618-8000", "N/A",
        "987654321",   # celular (válido para empresa?)
        "01234567",    # solo 8 dígitos con código
        "01 345 6789", "01-9876543", "014567890", "+511234567891"
    ],
    "monto_contrato": [
        "S/. 12,500.00", "S/. 12,500.00", "S/ 45000",
        "S/. 12,500.00", "S/.8,200", "S/ 15,750.50",
        "47500", "47500", "S/. 28,900.00",
        "S/ 5,000.00", "tres mil quinientos",
        "S/. 9,800.00", "62000", "S/ 31,450.00", "S/. 18,200.00"
    ],
    "fecha_contrato": [
        "2024-03-01", "01/03/2024", "2024-03-05",
        "2024-03-01", "03/10/2024", "10 de marzo 2024",
        "2024-03-15", "15/03/2024", "2024-03-20",
        "2024-03-25", "2024-03-28",
        "2024-04-01", "2024-04-05", "5 abril 2024", "2024-04-10"
    ],
}

df_sucio = pd.DataFrame(data_sucio)
print(f"✅ Dataset cargado: {df_sucio.shape[0]} registros × {df_sucio.shape[1]} columnas")
print(f"\nPrimeras 5 filas:")
df_sucio.head()
```

**PUNTO DE VERIFICACIÓN 1:** ¿Ves 15 filas y 7 columnas? → Continúa.

---

## PASO 2 — Diagnóstico (5 min)

```python
# ============================================================
# CELDA 2: Diagnóstico — ¿cuánto hay que limpiar?
# ============================================================
print("=== DIAGNÓSTICO DE CALIDAD ===\n")

# Nulos
print("1. VALORES NULOS:")
print(df_sucio.isnull().sum())

# Duplicados
print(f"\n2. DUPLICADOS:")
print(f"   Filas exactas duplicadas: {df_sucio.duplicated().sum()}")
print(f"   IDs duplicados: {df_sucio.duplicated(subset=['id_cliente']).sum()}")
print(f"   RUCs duplicados: {df_sucio.duplicated(subset=['ruc']).sum()}")

# Muestras de cada columna problemática
print(f"\n3. MUESTRA DE DATOS PROBLEMÁTICOS:")
print("   monto_contrato:", df_sucio["monto_contrato"].unique().tolist()[:6])
print("   telefono:", df_sucio["telefono"].unique().tolist()[:6])
print("   distrito:", df_sucio["distrito"].unique().tolist()[:6])
```

---

## PASO 3 — Limpieza y normalización (20 min)

```python
# ============================================================
# CELDA 3: ▶ TU TURNO — Limpieza completa
# COMPLETA los ___ para que el pipeline funcione
# ============================================================

df_limpio = df_sucio.copy()  # NUNCA modificar el original

# ─── LIMPIEZA 1: Eliminar duplicados ───
antes = len(df_limpio)
df_limpio = df_limpio.drop_duplicates(subset=["___"], keep="first")
# ↑ COMPLETA: columna que identifica a un cliente único → "id_cliente"
print(f"1. Duplicados eliminados: {antes - len(df_limpio)}")
print(f"   Registros restantes: {len(df_limpio)}")

# ─── LIMPIEZA 2: Normalizar razón social ───
df_limpio["razon_social_limpia"] = (
    df_limpio["razon_social"]
    .str.strip()          # quitar espacios
    .str.___()            # ← COMPLETA: método para poner en mayúsculas → upper()
    .fillna("SIN RAZÓN SOCIAL")
)
print(f"\n2. Razones sociales únicas (antes): {df_sucio['razon_social'].nunique()}")
print(f"   Razones sociales únicas (después): {df_limpio['razon_social_limpia'].nunique()}")

# ─── LIMPIEZA 3: Validar RUC ───
def validar_ruc(ruc):
    if pd.isna(ruc):
        return None
    ruc_str = str(ruc).strip()
    # RUC peruano: exactamente 11 dígitos numéricos
    if re.match(r"^\d{11}$", ruc_str):
        return ruc_str
    return ___    # ← COMPLETA: valor para RUC inválido → None

df_limpio["ruc_valido"] = df_limpio["ruc"].apply(validar_ruc)
invalidos = df_limpio["ruc_valido"].isna().sum()
print(f"\n3. RUCs inválidos encontrados: {invalidos}")
print("   RUCs problemáticos:", 
      df_limpio[df_limpio["ruc_valido"].isna()][["razon_social", "ruc"]].values.tolist())

# ─── LIMPIEZA 4: Normalizar distrito ───
mapeo_distritos = {
    "sjl": "San Juan de Lurigancho",
    "san juan de lurigancho": "San Juan de Lurigancho",
    "miraflores": "Miraflores",
    "san isidro": "San Isidro",
    "san borja": "San Borja",
    "surco": "Santiago de Surco",
    "los olivos": "Los Olivos",
    "ate": "Ate",
    "la victoria": "La Victoria",
}

def normalizar_distrito(d):
    if pd.isna(d):
        return None
    clave = " ".join(d.lower().split())   # minúsculas + sin espacios dobles
    return mapeo_distritos.get(clave, d.___())   # ← COMPLETA: capitalizar si no está en el mapeo → title()

df_limpio["distrito_limpio"] = df_limpio["distrito"].apply(normalizar_distrito)
print(f"\n4. Distritos únicos (antes): {df_sucio['distrito'].nunique()}")
print(f"   Distritos únicos (después): {df_limpio['distrito_limpio'].nunique()}")
print("   Valores:", sorted(df_limpio["distrito_limpio"].dropna().unique()))

# ─── LIMPIEZA 5: Normalizar monto del contrato ───
def normalizar_monto(monto_str):
    if pd.isna(monto_str):
        return None
    monto_str = str(monto_str).strip()
    # Remover prefijos de moneda
    for prefijo in ["S/. ", "S/ ", "S/."]:
        monto_str = monto_str.replace(prefijo, "")
    # Remover comas de miles y espacios
    monto_str = monto_str.replace(",", "").strip()
    try:
        return float(monto_str)   # convertir a float
    except ValueError:
        return ___    # ← COMPLETA: valor para montos no numéricos ("tres mil quinientos") → None

df_limpio["monto_soles"] = df_limpio["monto_contrato"].apply(normalizar_monto)
nulos_monto = df_limpio["monto_soles"].isna().sum()
print(f"\n5. Montos no convertibles: {nulos_monto}")
print(f"   Rango de contratos: S/ {df_limpio['monto_soles'].min():,.2f} a S/ {df_limpio['monto_soles'].max():,.2f}")

print("\n✅ Limpieza completada")
```

*Pistas para los `___`:*
- `drop_duplicates(subset=["___"])` → `"id_cliente"`
- `.str.___()` → `.str.upper()`
- `return ___` (RUC inválido) → `None`
- `d.___()` → `title()`
- `return ___` (monto no numérico) → `None`

**PUNTO DE VERIFICACIÓN 2:** ¿Eliminaste 3 duplicados? ¿Todas las razones sociales están en MAYÚSCULAS? ¿Hay 2 RUCs inválidos? ¿Los distritos están capitalizados consistentemente? → Continúa.

---

## PASO 4 — Pregunta de análisis final (5 min)

```python
# ============================================================
# CELDA 4: Resumen de calidad y análisis final
# ============================================================

# Resumen de calidad
print("=== RESUMEN DEL PROCESO DE LIMPIEZA ===")
print(f"Registros originales: {len(df_sucio)}")
print(f"Registros finales (sin duplicados): {len(df_limpio)}")
print(f"Duplicados eliminados: {len(df_sucio) - len(df_limpio)}")
print(f"RUCs inválidos: {df_limpio['ruc_valido'].isna().sum()}")
print(f"Montos no convertibles: {df_limpio['monto_soles'].isna().sum()}")
print(f"Nulos en razón social: {(df_limpio['razon_social_limpia'] == 'SIN RAZÓN SOCIAL').sum()}")

# Calcular el valor total de contratos válidos
total_contratos = df_limpio["monto_soles"].sum()
print(f"\nValor total cartera InkaLogística: S/ {total_contratos:,.2f}")

# Mostrar dataset limpio final
cols_limpias = ["id_cliente", "razon_social_limpia", "ruc_valido",
                "distrito_limpio", "monto_soles", "fecha_contrato"]
print("\nDataset limpio:")
print(df_limpio[cols_limpias].to_string(index=False))
```

```python
# ============================================================
# CELDA 5: Escribe tus respuestas como comentarios
# ============================================================

pregunta_1 = """
Identifica un problema de calidad en el dataset original
que el pipeline de limpieza NO resolvió automáticamente
y que requeriría revisión manual. Explica por qué no se
puede resolver solo con código.

# Tu respuesta:
"""

pregunta_2 = """
El campo 'telefono' no fue limpiado en este laboratorio.
Si tuvieras que normalizarlo, ¿cuál es el mayor desafío
específico de los teléfonos en este dataset?
(Pista: mira los valores: "+51 1 447-8800", "999", "N/A")

# Tu respuesta:
"""

pregunta_3 = """
¿Por qué aplicamos los cambios a 'df_limpio = df_sucio.copy()'
en lugar de modificar 'df_sucio' directamente?
¿Qué principio de integridad de datos sigue esa práctica?

# Tu respuesta:
"""

print(pregunta_1)
print(pregunta_2)
print(pregunta_3)
```

---

## ROL DEL DOCENTE DURANTE EL LABORATORIO

### Qué observar al circular

| Señal positiva | Señal de alerta | Acción |
|----------------|-----------------|--------|
| 15 registros en Celda 1 sin error | `ModuleNotFoundError` | "pandas viene preinstalado en Colab — ¿iniciaste un nuevo notebook o un notebook existente?" |
| 3 duplicados eliminados en Celda 3 | `KeyError: 'id_cliente'` | "¿Escribiste `'id_cliente'` con comillas simples? Es case-sensitive" |
| `.str.upper()` produce MAYÚSCULAS consistentes | Pone `.str.Title()` o `.str.upper` sin `()` | "Los métodos de pandas necesitan los paréntesis. `str.upper` sin `()` devuelve el método, no lo ejecuta" |
| RUC `"2010012821X"` y `"2011122345"` detectados como inválidos | La función valida todos como válidos | "¿Tu regex permite el caracter 'X'? Un RUC válido tiene SOLO dígitos (0-9). `\d` en regex significa solo dígitos, no letras" |
| Monto `"tres mil quinientos"` → `None` | ValueError deteniendo el loop | "¿Pusiste el `try/except` en la función? Sin él, `float('tres mil...')` lanza ValueError y detiene toda la Celda" |
| Respuestas de análisis con argumento técnico | Copias texto del compañero | Pedir que explique con otro ejemplo de su propia experiencia |

### Preguntas de andamiaje

- *"Tu función `validar_ruc` devuelve `None` para RUC inválido. ¿Qué pasa en el DataFrame donde hay `None`? ¿Cómo lo verías si haces `df_limpio['ruc_valido'].isna().sum()`?"*
- *"¿Por qué en el mapeo de distritos usamos `.lower()` como clave? ¿Qué pasaría si `"MIRAFLORES"` y `"miraflores"` son claves distintas en el diccionario?"*
- *"¿`df_limpio = df_sucio.copy()` hace una copia real o solo otro apuntador al mismo objeto? (Pista: ¿qué pasaría con `df_limpio = df_sucio` sin el `.copy()`?)"*

### Señales de comprensión vs. no comprensión

**Entendió:**
- Puede explicar por qué `.str.upper()` reduce los duplicados de "razón social"
- Identifica que `"2010012821X"` falla el regex porque X no es dígito
- Dice que la copia evita modificar el dataset original

**No entendió:**
- Cree que `drop_duplicates()` sin `subset` es lo mismo que con `subset=["id_cliente"]`
- No entiende por qué hay que hacer `str.lower()` antes de buscar en el diccionario
- No sabe qué hace `re.match(r"^\d{11}$", ruc_str)`

### Cierre (5 min)

```
1. "¿Cuántos encontraron exactamente 3 duplicados eliminados?"
   → Si alguien dice 0 o 6: revisar que el subset sea ["id_cliente"]
   
2. "¿Qué valor tuvo 'tres mil quinientos' después de la limpieza?"
   → Respuesta esperada: None (NaN en el DataFrame)
   → Si alguien dice "3500": "¿El código convirtió el texto a número
     automáticamente? ¿Qué método convierte texto a número? 
     ¿`float('tres mil quinientos')` funciona?"
     
3. "Pregunta de reflexión: si el jefe les pide el TOTAL de contratos
   (valor de cartera), ¿deben incluir el cliente con monto 'None'?
   ¿O reportar la suma de solo los montos válidos y aclarar cuántos
   quedaron pendientes de corrección?"
   → Conecta con integridad: la transparencia sobre datos faltantes
     es tan importante como el dato mismo.
```

---

## ENTREGABLE EN CLASE

Al finalizar los 35 minutos, el estudiante muestra al docente:

1. **Pantalla:** Celda 3 ejecutada sin errores con output visible
2. **La tabla de dataset limpio** de la Celda 4 con columnas normalizadas
3. **Verbalmente:** responde — *"¿Por qué la razón social 'bembos sac' y 'BEMBOS SAC' son un duplicado?"* + *"¿Qué pasa en pandas con un valor `None` en una columna numérica?"*

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 7 | 2026-1*
*Laboratorio de Clase — Ejecutar durante la sesión presencial*
