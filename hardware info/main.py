from click import command
import psutil
import os
from time import sleep
def cpu_monit():
    #monitoring CPU usage
    cpu_usg = psutil.cpu_percent()
    #monitoring CPU temperature
    try:
        temp = psutil.sensors_temperatures()['coretemp'][0].current
        print("CPU Temperature: %.2f" % temp)
    except:
        pass
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
    #monitoring RAM usage
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
    #monitoring disks usage on windows
    print("\n    Disks usage in %")
    cdrive_usg = psutil.disk_usage('C:\\').percent
    try:
        ddrive_usg = psutil.disk_usage('D:\\').percent
    except:
        ddrive_usg = 0
    try:
        edrive_usg = psutil.disk_usage('E:\\').percent
    except:
        edrive_usg = 0
    try:
        fdrive_usg = psutil.disk_usage('F:\\').percent
    except:
        fdrive_usg = 0
    try:
        gdrive_usg = psutil.disk_usage('G:\\').percent
    except:
        gdrive_usg = 0
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
    #drive G usage graph
    print("G:\\", gdrive_usg, end="")
    print(" |", end="")
    round_gdrive = int(round(gdrive_usg, 0) / 5)
    for i in range(round_gdrive):
        print("#", end="")
    for i in range(20 - round_gdrive):
        print(" ", end="")
    print("|")
    
def drives_monit_linux():
    #monitoring disks usage on linux
    print("\n    Disks usage in %")
    try:
        sdadrive_usg = psutil.disk_usage('/dev/sda').percent
    except:
        sdadrive_usg = 0
    try:
        sdbdrive_usg = psutil.disk_usage('/dev/sdb').percent
    except:
        sdbdrive_usg = 0
    try:
        sdcdrive_usg = psutil.disk_usage('/dev/sdc').percent
    except:
        sdcdrive_usg = 0
    try:
        sdddrive_usg = psutil.disk_usage('/dev/sdd').percent
    except:
        sdddrive_usg = 0
    try:
        sdedrive_usg = psutil.disk_usage('/dev/sde').percent
    except:
        sdedrive_usg = 0
    #drive sda usage graph
    print("/dev/sda", sdadrive_usg, end="")
    print(" |", end="")
    round_sdadrive = int(round(sdadrive_usg, 0) / 5)
    for i in range(round_sdadrive):
        print("#", end="")
    for i in range(20 - round_sdadrive):
        print(" ", end="")
    print("|")
    #drive sdb usage graph
    print("/dev/sdb", sdbdrive_usg, end="")
    print(" |", end="")
    round_sdbdrive = int(round(sdbdrive_usg, 0) / 5)
    for i in range(round_sdbdrive):
        print("#", end="")
    for i in range(20 - round_sdbdrive):
        print(" ", end="")
    print("|")
    #drive sdc usage graph
    print("/dev/sdc", sdcdrive_usg, end="")
    print(" |", end="")
    round_sdcdrive = int(round(sdcdrive_usg, 0) / 5)
    for i in range(round_sdcdrive):
        print("#", end="")
    for i in range(20 - round_sdcdrive):
        print(" ", end="")
    print("|")
    #drive sdd usage graph
    print("/dev/sdd", sdddrive_usg, end="")
    print(" |", end="")
    round_sdddrive = int(round(sdddrive_usg, 0) / 5)
    for i in range(round_sdddrive):
        print("#", end="")
    for i in range(20 - round_sdddrive):
        print(" ", end="")
    print("|")
    #drive sde usage graph
    print("/dev/sde", sdedrive_usg, end="")
    print(" |", end="")
    round_sdedrive = int(round(sdedrive_usg, 0) / 5)
    for i in range(round_sdedrive):
        print("#", end="")
    for i in range(20 - round_sdedrive):
        print(" ", end="")
    print("|")
    

def network_usage():
    #monitoring network usage
    net_usg = psutil.net_io_counters()
    net_rec = round(net_usg.bytes_recv / 1024 / 1024, 4)
    net_sen = round(net_usg.bytes_sent / 1024 / 1024, 4)
    print("\n    Network usage in MB", "\n", "Received:", net_rec, " MB \n", "Sent:", net_sen, " MB") 

def nvd_gpumemusg():
    #monitoring GPU memory usage
    command = "nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits"
    gpmem_usg = int(os.popen(command).read())
    command = "nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits"
    gpmem_max = int(os.popen(command).read())
    print("     GPU used mem:", gpmem_usg, "MB\n     GPU max mem:", gpmem_max, "MB")  
    #gpu usage graph
    gpumem_graph = int(round(gpmem_usg/gpmem_max * 100) / 5)
    print("|", end="")
    for i in range(gpumem_graph):
        print("#", end="")
    for i in range(20 - gpumem_graph):
        print(" ", end="")
    print("| \n") 

def nvd_gpuusg():
    #monitoring GPU usage
    command = "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits"
    gpu_usg = int(os.popen(command).read())
    print("     GPU usage in % :", gpu_usg)
    #monitoring GPU temperature
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
    try:
        try:
            print("CPU model:", psutil.cpu_info().model)
        except:
            pass
        cpu_monit()
    except:
        print("\n    CPU usage not available")
    try:
        print("\n GPU model:", os.popen("nvidia-smi --query-gpu=name --format=csv,noheader,nounits").read(), end="")
        nvd_gpumemusg()
        nvd_gpuusg()
    except:
        print("\n    GPU usage and memory usage not available")
    try:
        ram_monit()
    except:
        print("\n    RAM usage not available")
    try:
        drives_monit_win()
    except:
        try:
            drives_monit_linux()
        except:
            print("\n    Disks usage not available")
    #try:
    #    network_usage()
    #except:
    #    print("\n    Network usage not available")
    
def main():
    while(True):
        monit()
        sleep(1.33)

if __name__ == '__main__':
    main()
