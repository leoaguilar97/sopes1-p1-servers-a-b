import os

# CPUS del OS
cpus = os.cpu_count()

def get_cpu_percentage():
    
    print("CANTIDAD DE CPUS: " + str(cpus))
    
    last_minute_load, l5, l15 = os.getloadavg()
    cpu_prctg = (last_minute_load / cpus) * 100
    print("CPU PERCENT: " + str(cpu_prctg))

    return  cpu_prctg