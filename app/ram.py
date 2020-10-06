
import subprocess
import re

matcher = re.compile('\d+')

# Memory usage
total_ram = subprocess.run(['sysctl', 'hw.memsize'], stdout=subprocess.PIPE).stdout.decode('utf-8')
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
vmLines = vm.split('\n')

wired_memory = (int(matcher.search(vmLines[6]).group()) * 4096) / 1024 ** 3
free_memory = (int(matcher.search(vmLines[1]).group()) * 4096) / 1024 ** 3
active_memory = (int(matcher.search(vmLines[2]).group()) * 4096) / 1024 ** 3
inactive_memory = (int(matcher.search(vmLines[3]).group()) * 4096) / 1024 ** 3

# Used memory = wired_memory + inactive + active
def get_ram_percentage():
    tu = int(matcher.search(total_ram).group())/ 1024 ** 3
    print("MEMORIA TOTAL: " + str(tu))
    ur = round(wired_memory + active_memory + inactive_memory, 2)
    print("MEMORIA USADA: " + str(ur))
    print("PORCENTAJE: " + str((ur / tu) * 100))

    return (ur / tu) * 100