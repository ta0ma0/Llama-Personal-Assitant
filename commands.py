import subprocess
import os


def open_keepass():
    cmd = "keepassx"
    subprocess.Popen(cmd, shell=True)


def open_thunderbird():
    cmd = "thunderbird"
    subprocess.Popen(cmd, shell=True)


def open_flyweel():
    cmd = "gnome-terminal -- '/home/ruslan/opt/flywheel/Code/flywheel.py'"
    subprocess.Popen(cmd, shell=True)


def start_working():
    open_thunderbird()
    cmd = "dbeaver"
    cmd2 = ["konsole"]
    subprocess.Popen(cmd, shell=True)
    subprocess.Popen(cmd2, shell=True)


def stop_working():
    pid_cmd = ["ps", "-a", "-u", "-x"]
    pid = subprocess.run(pid_cmd, stdout=subprocess.PIPE)
    pid_result = pid.stdout.decode("utf-8").split('\n')
    for line in pid_result:
        if "dbeaver" in line:
            pid_beav = line.split()[1]
    try:
        os.kill(int(pid_beav), 15)
    except UnboundLocalError:
        pass
    cmd2 = "pkill konsole"
    subprocess.Popen(cmd2, shell=True)
    cmd3 = "pkill thunderbird"
    subprocess.Popen(cmd3, shell=True)


def start_joplin():
    cmd = "~/opt/Joplin-2.9.17.AppImage"
    subprocess.Popen(cmd, shell=True)