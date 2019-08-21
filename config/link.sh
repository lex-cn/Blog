pwd=`cd $(dirname $0);pwd -P`

ln -fs $(pwd)/_vimrc ~/.vimrc
ln -sf $(pwd)/bashrc ~/.bashrc
ln -sf $(pwd)/Xresources ~/.Xresources
rm -rf ~/.i3*
mkdir ~/.i3/
ln -sf $(pwd)/config ~/.i3/config
rm -rf ~/.cache
ln -sf /dev/shm/ ~/.cache
rm -rf ~/.adobe
ln -sf /dev/shm/ ~/.adobe
