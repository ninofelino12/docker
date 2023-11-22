<h1>Docker</h1>
<h3>
1. Install Portainer
</h3>
<img src="flask/static/portainer.png"/>
<p>
<code>
docker pull portainer/portainer<br>
docker volume create portainer_data<br>
</code>
</p>
<p>
docker run -d -p 9000:9000 -v ~/portainer_data:/data -v /var/run/docker.sock:/var/run/docker.sock --name portainer portainer/portainer
</p>
<h3>
Install Odoo:17

</h3>

docker compose odoo17.yaml