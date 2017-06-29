## Notebooks + support code for Alexandria workshop

### to install:
`python3 setup.py install`

### to create docker image:
`docker build -t huygensing/alexandria-workshop-notebooks .`

### to run the docker image:
`docker run -d -p${local_port}:8888 -v ${local_workdir}:/data/work huygensing/alexandria-workshop-notebooks`

### build the alexandria-markup-notebook image:
`docker build --tag huygensing/alexandria-markup-notebook --file MarkupDockerfile`

### run the alexandria-markup-notebook + dependencies using docker-compose
1. download the docker-compose.yml file
2. replace `192.168.99.100` in lines 9 & 19 by your docker-machine IP address.
3. replace `/c/Users/bramb` in line 29 with a local directory
4. save your docker-compose.yml
5. run `docker-compose pull && docker-compose up`
6. open a browser and go to http://192.168.99.100, with `192.168.99.100` replaced by your docker-machine IP address.
7. click on `examples` and run the `markup-init` notebook
8. on the `markup-init` notebook, change the `server_url` and `lates_server_url` to the `BASE_URI`s defined in the `docker-compose.yml` for the `alexandria` and `latex` services, respectively.
9. now you can run the notebook.  