import os
import re

number_finder = re.compile('\d+')

past_cpu_stats = {
    "prevTotal": 0,
    "prevIdle": 0
}

# sumar todos los stats del cpu encontrados en procfile


def get_cpu_stats_total(cpu_stats):
    try:
        return cpu_stats["user"] + cpu_stats["nice"] + cpu_stats["system"] + cpu_stats["idle"] + cpu_stats["iowait"] + cpu_stats["irq"] + cpu_stats["softirq"]
    except Exception as e:
        print(" ERROR SUMANDO TODOS LOS STATS ")
        print(cpu_stats)
        print(e)
        if hasattr(e, 'message'):
            print(e.message)
        return 1

# obtener el porcentaje utilizado del CPU


def get_cpu_percentage():
    try:
        proc_file = open("/proc/stat", mode="r", encoding="utf-8")
        first_line = proc_file.readline()
        print("PROC FILE: " + first_line)

        numbers = number_finder.findall(first_line)
        print("NUMEROS ENCONTRADOS: ")
        print(numbers)

        stats = {
            "user": int(numbers[0]),
            "nice": int(numbers[1]),
            "system": int(numbers[2]),
            "idle": int(numbers[3]),
            "iowait": int(numbers[4]),
            "irq": int(numbers[5]),
            "softirq": int(numbers[6])
        }

        cpu_total = get_cpu_stats_total(stats)

        diff_idle = stats["idle"] - past_cpu_stats["prevIdle"]
        diff_total = cpu_total - past_cpu_stats["prevTotal"]
        
        diff_usage = ( 1000 * ( diff_total - diff_idle) / diff_total + 5 ) / 10
        print("USO DE CPU: " + str(diff_usage) + "%")

        past_cpu_stats["prevIdle"] = stats["idle"]
        past_cpu_stats["pastTotal"] = cpu_total

        return diff_usage

    except Exception as e:
        print(" ERROR CALCULANDO CPU UTILIZADO ")
        print(e)

        if hasattr(e, 'message'):
            print(e.message)
        return 0
