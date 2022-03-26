from click import command
import psutil
import os
from time import sleep
def cpu_monit():
    #monitor CPU usage
    cpu_usg = psutil.cpu_percent()
    print("     CPU usage in % \n", cpu_usg)
    #cpu usage graph
    round_cpu = int(round(cpu_usg, 0) / 5)
    print("|", end="")
    for i in range(round_cpu):
        print("#", end="")
    for i in range(20 - round_cpu):
        print(" ", end="")
    print("|")

    

def ram_monit():
    #monitor RAM usage
    ram_usg = psutil.virtual_memory().percent
    print("     RAM usage in % :", ram_usg)
    #ram usage graph
    print("|", end="")
    round_ram = int(round(ram_usg, 0) / 5)
    for i in range(round_ram):
        print("#", end="")
    for i in range(20 - round_ram):
        print(" ", end="")
    print("|")

def drives_monit_win():
    #monitor disks usage on windows
    print("\n    Disks usage in %")
    cdrive_usg = psutil.disk_usage('C:\\').percent
    ddrive_usg = psutil.disk_usage('D:\\').percent
    edrive_usg = psutil.disk_usage('E:\\').percent
    fdrive_usg = psutil.disk_usage('F:\\').percent
    #drive C usage graph
    print("C:\\", cdrive_usg, end="")
    print(" |", end="")
    round_cdrive = int(round(cdrive_usg, 0) / 5)
    for i in range(round_cdrive):
        print("#", end="")
    for i in range(20 - round_cdrive):
        print(" ", end="")
    print("|")
    #drive D usage graph
    print("D:\\", ddrive_usg, end="")
    print(" |", end="")
    round_ddrive = int(round(ddrive_usg, 0) / 5)
    for i in range(round_ddrive):
        print("#", end="")
    for i in range(20 - round_ddrive):
        print(" ", end="")
    print("|")
    #drive E usage graph
    print("E:\\", edrive_usg, end= "")
    print(" |", end="")
    round_edrive = int(round(edrive_usg, 0) / 5)
    for i in range(round_edrive):
        print("#", end="")
    for i in range(20 - round_edrive):
        print(" ", end="")
    print("|")
    #drive F usage graph
    print("F:\\", fdrive_usg, end="")
    print(" |", end="")
    round_fdrive = int(round(fdrive_usg, 0) / 5)
    for i in range(round_fdrive):
        print("#", end="")
    for i in range(20 - round_fdrive):
        print(" ", end="")
    print("|")
    
def drive_monit_linux():
    #monitor disks usage on linux
    print("\n    Disks usage in %")
    sdadrive_usg = psutil.disk_usage('/dev/sda').percent
    print("/dev/sda", sdadrive_usg, end="")
    #drive sda usage graph
    print(" |", end="")
    round_sdadrive = int(round(sdadrive_usg, 0) / 5)
    for i in range(round_sdadrive):
        print("#", end="")
    for i in range(20 - round_sdadrive):
        print(" ", end="")
    print("|")

def network_usage():
    #monitor network usage
    net_usg = psutil.net_io_counters()
    net_rec = round(net_usg.bytes_recv / 1024 / 1024, 2)
    net_sen = round(net_usg.bytes_sent / 1024 / 1024, 2)
    print("\n    Network usage in MB", "\n", "Received:", net_rec, " MB \n", "Sent:", net_sen, " MB") 

def gpumemusg():
    #monitor GPU memory usage
    command = "nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits"
    gpmem_usg = int(os.popen(command).read())
    command = "nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits"
    gpmem_max = int(os.popen(command).read())
    print("\n     GPU used mem:", gpmem_usg, "MB\n     GPU max mem:", gpmem_max, "MB")  
    #gpu usage graph
    gpumem_graph = int(round(gpmem_usg/gpmem_max * 100) / 5)
    print("|", end="")
    for i in range(gpumem_graph):
        print("#", end="")
    for i in range(20 - gpumem_graph):
        print(" ", end="")
    print("| \n")

def gpuusg():
    #monitor GPU usage
    command = "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits"
    gpu_usg = int(os.popen(command).read())
    print("     GPU usage in % :", gpu_usg)
    #monitor GPU temperature
    command = "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits"
    print("     GPU temperature in C :", int(os.popen(command).read()))
    #gpu usage graph
    gpuusg_graph = int(round(gpu_usg) / 5)
    print("|", end="")
    for i in range(gpuusg_graph):
        print("#", end="")
    for i in range(20 - gpuusg_graph):
        print(" ", end="")
    print("| \n")

def teminal_clearing():
    #function to clear the terminal
    try:
        command = 'cls'
        os.system(command)
    except:
        command = 'clear'
        os.system

def monit():
    teminal_clearing()
    cpu_monit()
    gpumemusg()
    gpuusg()
    ram_monit()
    drives_monit_win()
    network_usage()

def main():
    while(True):
        monit()
        sleep(1)

if __name__ == '__main__':
    main()
