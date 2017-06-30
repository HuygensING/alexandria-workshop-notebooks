# Notebooks + support code for Alexandria workshop

## run the alexandria-markup-notebook + dependencies using docker-compose
1. download the [docker-compose.yml](https://raw.githubusercontent.com/HuygensING/alexandria-workshop-notebooks/master/docker-compose.yml) file
1. move to the directory containing `docker-compose.yml` 
2. replace `192.168.99.100` in lines 10 and 21 by your docker-machine IP address.
3. replace `/c/Users/bramb/work` in line 33 with a local directory
4. save your docker-compose.yml
5. run `docker-compose pull && docker-compose up`
6. open a browser and go to http://192.168.99.100, with `192.168.99.100` replaced by your docker-machine IP address.
7. click on `examples` and run the `markup-init` notebook
8. on the `markup-init` notebook, change the `server_url` and `lates_server_url` to the `BASE_URI`s defined in the `docker-compose.yml` for the `alexandria` and `latex` services, respectively.
9. now you can run the notebook.  

### to install:
`python3 setup.py install`

### to create alexandria-workshop-notebooks docker image:
`docker build -t huygensing/alexandria-workshop-notebooks .`

### to run the alexandria-workshop-notebooks docker image:
`docker run -d -p${local_port}:8888 -v ${local_workdir}:/data/work huygensing/alexandria-workshop-notebooks`

### create the alexandria-markup-notebook docker image:
`docker build --tag huygensing/alexandria-markup-notebook --file MarkupDockerfile`
