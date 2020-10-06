import os

# CPUS del OS
cpus = os.cpu_count()

def get_cpu_percentage():
    try:

        print("CANTIDAD DE CPUS: " + str(cpus))
        last_minute_load, l5, l15 = os.getloadavg()
        
        print("CPU LM: ")
        print(last_minute_load, l5, l15)

        print("OS GETLOADAVG: ")
        print(os.getloadavg())

        cpu_prctg = (last_minute_load / cpus) * 100
        print("CPU PERCENT: " + str(cpu_prctg))

        return  cpu_prctg
    
    except Exception as e:
        print(" ERROR CALCULANDO CPU UTILIZADO ")
        print(e)
        
        if hasattr(e, 'message'):
            print(e.message)
        return 0