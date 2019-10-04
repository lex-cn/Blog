pwd=`cd $(dirname $0);pwd -P`

ln -fs $(pwd)/_vimrc ~/.vimrc
ln -sf $(pwd)/bashrc ~/.bashrc
ln -sf $(pwd)/Xresources ~/.Xresources

rm -rf ~/.desk.png
rm -rf ~/.lock.png
ln -sf $(pwd)/desk.png ~/.desk.png
ln -sf $(pwd)/lock.png ~/.lock.png

rm -rf ~/.i3*
mkdir ~/.i3/
ln -sf $(pwd)/config ~/.i3/config
ln -sf $(pwd)/ctags.conf ~/.ctags

rm -rf ~/.cache
ln -sf /dev/shm/ ~/.cache
rm -rf ~/.adobe
ln -sf /dev/shm/ ~/.adobe
