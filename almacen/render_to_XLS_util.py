from django.template import Variable, defaultfilters
from django.http import HttpResponse
from django.conf import settings
import xlwt
import datetime
from pytz import timezone

def render_to_xls(queryset, filename):

    ezxf = xlwt.easyxf
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("movimientos")

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    row_num = 0

    columns = [
            'Picking',
            'Producto',
            'Cantidad',
            'Tractor o Compañía',
            'Propietario', 
            'Detalle',
            'Fecha Creacion',
            'Ultima Actualizacion', 
            'Fecha Programada', 
            'De', 
            'Para',
            'estado']

    for col_num in range(len(columns)):
        sheet.write(row_num, col_num, columns[col_num], font_style)

    rows = queryset.values_list('picking', 'producto', 'cantidad', 'compania', \
                'propietario', 'detalle', 'fecha_creacion', 'ultima_actualizacion',\
                'fecha_programada', 'de', 'para', 'estado'
        )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num], datetime.datetime):
                fecha_row = row[col_num].astimezone(timezone(settings.TIME_ZONE)).strftime("%d-%m-%Y %H:%M")
                sheet.write(row_num, col_num, fecha_row)    
            else:                
                sheet.write(row_num, col_num, row[col_num])
        
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    book.save(response)
    return response
