import subprocess



def open_keepass():
    cmd = "keepassx"
    subprocess.Popen(cmd, shell=True)


def open_thunderbird():
    cmd = "thunderbird"
    subprocess.Popen(cmd, shell=True)

def open_flyweel():
    cmd = "gnome-terminal -- '/home/ruslan/opt/flywheel/Code/flywheel.py'"
    subprocess.Popen(cmd, shell=True)

