mkdir cDestino
chmod 777 "cDestino"
cp -r "cFuente/*" "cDestino"
cd "cDestino"
fecha = (date +'%Y_%m_%d')
nombreCDestino="${cDestino##*/}"
tar -cf "$nombreCDEstino.tar" cFuente
