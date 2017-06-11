# Acerca
Información Venezuela es un bot de Telegram (@infovebot) con el cual puedes consultar información pública de servicios de Venezuela, tales como el estado de cuenta en CANTV y las cotizaciones en el IVSS. Puedes usarlo en chat privado o en grupo. También puedes usarlo en modo inline. 


# Desplegar @infovebot en tu propio servidor

Información Venezuela ya se encuentra funcionando en Telegram con la cuenta @infovebot, sin embargo, puedes ejecutar este bot de este modo:

* Registra un bot con el [BotFather](https://telegram.me/botfather)
* Después de instalar `Python2.7` y `pip` en el servidor, ejecuta lo siguiente:

```
sudo pip install pycurl
sudo pip install python-telegram-bot==6.0.3
```

* Descarga el código desde mi [repositorio en Github](https://github.com/eniolw/infovebot)
* Reemplaza la cadena `TU_TOKEN` dentro de la llamada a `Updater` en la función `main` (archivo `infovebot.py`) con tu propio token de bot que obtuviste con el botfather.
* Ejecuta el script `infovebot.py`con `python infovebot.py &` para que se ejecute permanentemente en segundo plano.


# Reconocimientos
@infovebot es un proyecto iniciado por Oniel Revilla Morón (correo: eniolw@gmail.com; Telegram: @eniolw) y dedicado a la [`ComunidadNaciente de software libre de Venezuela`](https://t.me/ComunidadNaciente) y todos los usuarios de Telegram.

En este proyecto se han portado y modificado scripts de William Cabrera (<cabrerawilliam@gmail.com> https://github.com/willicab/infove-api) y se han utilizado las bibliotecas [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot)
y `pycurl`.

Agradecimientos a Riztan Gutiérrez (Telegram: @riztan) por hospedar a @infovebot.
