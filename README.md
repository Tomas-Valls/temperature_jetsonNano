# Pasos instalación

## Instalación OS


## Configurar dependencias

- Crear carpeta temporal y clonar repositorio o descargar zip.

```bash
cd ~
mkdir tmp
sudo apt install git
cd tmp && git clone https://github.com/Tomas-Valls/temperature_jetsonNano.git
```

## Instalación docker y docker-compose

- Ejecutar scripts `install_docker.sh` y `install_compose.sh`:

```bash
cd ~/tmp/temperature_jetsonNano/docker
chmod +x install_docker.sh
chmod +x install_compose.sh

./install_docker.sh
./install_compose.sh
```


## Creación de directorios

Crear directorios, ejecutando:

```bash
cp ~/tmp/temperature_jetsonNano/make_dirs.sh ~/
cd
chmod +x make_dirs.sh
./make_dirs.sh
```




- En caso de no utilizar `docker-compose` :

```bash
cp ~/tmp/temperature_jetsonNano/run_docker_hc.sh ~/Sinanticam/sinanticam_cam/

cd ~/Sinanticam/sinanticam_cam/
chmod +x run_docker_hc.sh
```

