# Pasos de uso



## Configurar dependencias

- Crear carpeta temporal y clonar repositorio o descargar zip.

```bash
cd ~
mkdir tmp
sudo apt install git
cd tmp && git clone https://github.com/Tomas-Valls/temperature_jetsonNano.git
```

## Instalación docker y docker-compose

- Ejecutar script `install_docker.sh`:

```bash
cd ~/tmp/temperature_jetsonNano/docker
chmod +x install_docker.sh
./install_docker.sh
```







- En caso de no utilizar `docker-compose` :

```bash
cd ~/tmp/temperature_jetsonNano

sudo docker build -t temperature_jetsonnano:0.1 . 
sudo docker run  "temperature_jetsonnano:0.1" 
python3 -u temperature_test.py 

```
