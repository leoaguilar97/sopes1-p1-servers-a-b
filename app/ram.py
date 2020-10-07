
import re

number_finder = re.compile('\d+')

# Obtener el porcentaje de ram utilizado actualmente
def get_ram_percentage():
    try:        
        file_content = ""
        with open("/proc/ram", mode='r', encoding="utf-8") as mem_file:
            file_content = mem_file.read()
        
        numbers = number_finder.findall(file_content)

        mtotal = int(numbers[1])
        mused = int(numbers[0])
        
        print("** RAM UTILIZANDO MODULO KERNEL **")
        print("MEMORIA TOTAL (bytes): " + str(mtotal))
        print("MEMORIA PARA UTILIZAR (bytes): " + str(mused))

        percentage = round((mused / mtotal) * 100, 2)
        print("Porcentaje de memoria utilizada: " + str(percentage) + "%")

        return percentage

    except Exception as e:
        print("ERROR CALCULANDO MEMORIA LIBRE")
        print(e)
        
        if hasattr(e, 'message'):
            print(e.message)
        return 0
