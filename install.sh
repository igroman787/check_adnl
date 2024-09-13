# доустановить пакеты
apt update && apt dist-upgrade -y
apt install python3-pip ncdu nload git iptables iptables-persistent -y

# Настроить консоль
echo "PS1='\[\033[01;32m\]\u\[\033[01;34m\]-\[\033[01;31m\]\h\[\033[00;34m\]{\[\033[01;34m\]\w\[\033[00;34m\]}\[\033[01;32m\]:\[\033[00m\]'" > ~/.bashrc

# Клонировать репозиторий
useradd -d /dev/null -s /dev/null front
mkdir -p /home/front/www && cd /home/front/www
git clone --recursive https://github.com/igroman787/check_adnl
pip3 install -r /home/front/www/check_adnl/requirements.txt --break-system-packages

# Добавить службу
cp /home/front/www/check_adnl/front.service /etc/systemd/system/front.service
systemctl daemon-reload
systemctl enable front
systemctl start front

# Прокинуть порт
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables-save -c > /etc/iptables/rules.v4
