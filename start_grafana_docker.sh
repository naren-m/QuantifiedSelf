docker run -d -i --net=influxdb \
                 -p 3000:3000 \
                 -v $PWD/grafana:/var/lib/grafana \
                 --name grafana grafana/grafana
