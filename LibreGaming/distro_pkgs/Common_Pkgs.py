import os, subprocess

class Common_Pkgs:
    """
    Here are all the pkgs that are distro agnostic
    """

    # TO check if LibreGaming is executed with root or not 
    def whoami(self, authorize):
        whoami = str(subprocess.getoutput("whoami"))
        if whoami == "root" and authorize == False:
           print("\n\tPlease run LibreGaming without sudo or doas command for this flag\t")
           exit(0)
        elif whoami != "root" and authorize == True:
           print("\n\tPlease run LibreGaming with sudo or doas command for this flag\n")
           exit(0)

    # installation for Itch.io store
    def itch(self):
        self.whoami(False)
        print('Downloading itch.io')
        os.system("wget 'https://itch.io/app/download?platform=linux' -O itch-setup")
        os.system("chmod +x itch-setup && ./itch-setup")

    # installation for Athenaeum store For FOSS games
    def Athenaeum(self):
        self.whoami(False)
        os.system("flatpak install flathub com.gitlab.librebob.Athenaeum -y")
