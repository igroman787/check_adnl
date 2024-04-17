# доустановить пакеты
apt install -y iptables

# скачать либу

# 

# 

# 

# 

# Добавить службу

# Прокинуть порты и заблокировать неиспользуемый
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
