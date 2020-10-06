
import subprocess
import re

number_finder = re.compile('\d+')

# Obtener el porcentaje de ram utilizado actualmente
def get_ram_percentage():
    try:
        total_ram = subprocess.run(
            ['free'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        tr = number_finder.findall(total_ram)

        print("VALORES DE MEMORIA ENCONTRADO: ")
        print(tr)

        mtotal = int(tr[0])
        mused = int(tr[1])

        print("MEMORIA TOTAL (bytes): " + str(mtotal))
        print("MEMORIA USADA (bytes): " + str(mused))

        return round((mused / mtotal) * 100, 2)

    except Exception as e:
        print("ERROR CALCULANDO MEMORIA LIBRE")
        print(e)
        
        if hasattr(e, 'message'):
            print(e.message)
        return 0
