#!/usr/bin/env python3
import os,sys

soft=" \
sudo sed -i 's/cn.archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list;\
sudo apt-get clean ;\
sudo apt-get update;\
sudo apt-get dist-upgrade;\
sudo apt-get autoremove;\
sudo apt-get autoclean; \
"

gits=[
"git lfs install         ;",
"git config --global init.defaultBranch main         ;",
"git config --global color.ui true                   ;",
"git config --global core.quotepath false            ;",
"git config --global gui.encoding utf-8              ;",
"git config --global i18n.commit.encoding utf-8      ;",
"git config --global i18n.logoutputencoding utf-8    ;",
"git config --global core.filemode false             ;",
"git config --global diff.tool vimdiff               ;",
"git config --global difftool.prompt false           ;",
"git config --global user.email \"lipengbo@msn.com\" ;", 
"git config --global user.name  \"lipengbo\"         ;",
"git config --global core.editor vim                 ;"]

flpk= "\
        flatpak remote-add --if-not-exists flathub https://mirrors.sjtu.edu.cn/flathub;\
        flatpak install org.mozilla.firefox org.zotero.Zotero com.zettlr.Zettlr"

#https://codeload.github.com/BannedPatriot/ttf-wps-fonts/zip/refs/heads/master

guis="\
sudo apt-get install i3-wm i3lock-fancy redshift-gtk pcmanfm \
    flatpak lxappearance lxterminal gnome-disk-utility flameshot \
    simplescreenrecorder smplayer bleachbit gparted i3status \
    i3blocks blueman rofi  lxappearance nitrogen pcmanfm"

clis="\
sudo apt-get install vim git git-lfs gcc build-essential gfortran gdb python3 \
    bash-completion python3-pip pandoc pandoc-citeproc tmux wget axel \
     tig graphviz rsync doxygen libgsl-dev libblas-dev liblapack-dev xcompmgr \
    htop libgeos++-dev proj-bin  libproj-dev libgeos.dev global cscope dos2unix trash-cli\
    upower pciutils sshfs tig  universal-ctags unzip transmission-daemon transmission-cli\
    lftp"


pips="\
#pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/ ;\n\
pip3 config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/ ;\n\
pip3 install -U pip ;\n\
pip3 install -U numpy matplotlib pandas ipython scipy tk cartopy pygments;\n\
pip3 install -U keras tensorflow-gpu pydot sklearn scikit-learn pyforest geopandas memory_profiler;\n\
"

def setConfig():
    exSet="\
    rm -rf ~/.cache; \n\
    ln -sf /dev/shm/ ~/.cache; \n\
    rm -rf ~/.adobe; \n\
    ln -sf /dev/shm/ ~/.adobe; \n\
    "
    os.system(exSet)

    pwd=os.getcwd()
    lnlist=["bashrc","i3/config", "ctags.conf", "gtags.conf", "i3blocks.conf", "tmux.conf", 
        "vimrc", "Xresources", "snippets","gitconfig"]


    for ln in lnlist:
        cmd='rm -rf ~/.%s; ln -sf %s/%s ~/.%s '%(ln,pwd,ln,ln)
        print(cmd)
        os.system(cmd)

    cmd = "git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle"
    os.system(cmd)

    cmd = "git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm"
    os.system(cmd)

def printhelp():
    print("setMySys help \n",
    "-soft : set software mirros \n",  
    "-gits : git settings  \n",
    "-guis : install GUI softwares \n", 
    "-clis : install CLI softwares  \n",
    "-pips : set pip and install Python packages \n",
    "-link : link dot file into configs \n",
    )


npars=len(sys.argv)

if npars <=1:
    printhelp()
    sys.exit()

for idx in range(1, len(sys.argv)): 
    if   sys.argv[idx] == "-soft": 
        print("soft")
        os.system(soft)
    elif sys.argv[idx] == "-gits": 
        print("gits")
        for ts in gits:
            print(ts)
            os.system(ts)
    elif sys.argv[idx] == "-guis": 
        print("guis")
        os.system(guis)
    elif sys.argv[idx] == "-clis": 
        print("clis")
        os.system(clis)
    elif sys.argv[idx] == "-pips": 
        print("pips")
        os.system(pips)
    elif sys.argv[idx] == "-link": 
        setConfig()
        print("link")

