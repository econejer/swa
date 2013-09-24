este-swon
=========

Requerimientos:

bottle - webserver
beaker - sessions
tornado - para que corrar el webserver de test

pip install bottle beaker tornado fono

Puerto por defecto 8080

Se modifica en development_server.py

rutas creadas:

/test <- responde de 3 maneras distintas
/media/ <- carga lo que hay en static, prueba dh.jpg
