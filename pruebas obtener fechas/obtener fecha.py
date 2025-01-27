from datetime import date
from datetime import datetime
def obtener_fecha():
    now=datetime.now()
    fecha_hoy=now.strftime('%d/%m/'+'20'+'%y(%H:%M)')
    return fecha_hoy

print(obtener_fecha())
