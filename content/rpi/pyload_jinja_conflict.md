Title: Pyload Webserver (Jinja2)-Probleme
Date: 2013-07-09 12:56
Category: Raspberry Pi
Tags: raspberry_pi, pyload, python, jinja2
Author: x4343
Summary: Probleme mit dem pyload Webserver

Seitdem ich meinen RPi nutze um damit diese [pelican][pelican] Seiten zu generieren, funktionierte der
[pyload][pyload] Webserver (threaded) nicht mehr.

Ich hab pyload bereits seit einigen Monaten laufen - unabhaengig davon, ob ich es nutze.
Zieht ja kaum Performance...

Der Server und alles andere laeuft auch nach wie vor problemlos. Erst nachdem man via Browser
auf das Webinterface zugreifen moechte, kommt eine Fehler, der jede weitere Arbeit unterbindet!

> Critical Error while processing request

Durch Einschalten der Debug-Ausgabe in der pyload.conf (in $HOME/.pyload)...

``` bash
bool debug_mode : "Debug Mode" = True
```

...wird die Fehlermeldung schon etwas klarer:

```
Critical error while processing request: 
Error: 
UndefinedError("'_' is undefined",) 

Traceback: 

Traceback (most recent call last):
	File "/usr/share/pyload/module/lib/bottle.py", line 820, in wsgi
		out = self._cast(self._handle(environ), request, response)
	File "/usr/share/pyload/module/lib/bottle.py", line 773, in _cast
		out = self.error_handler.get(out.status, repr) (out)
	File "/usr/share/pyload/module/web/pyload_app.py", line 53, in error500
		error.traceback.replace("\n", if error.traceback else "No Traceback"])
	File "/usr/share/pyload/module/web/pyload_app.py", line 72, in base
		return render_to_response('base.html', {'messages': messages}, [pre_processor])
	File "/usr/share/pyload/module/web/utils.py", line 30, in render_to_response
	return t.render(**args)
	File "/usr/local/lib/python2.7/dist-packages/jinja2/environment.py", line 969, in render
		return self.environment.handle_exception(exc_info, True)
	File "/usr/local/lib/python2.7/dist-packages/jinja2/environment.py", line 742, in handle_exception
		reraise(exc_type, exc_value, tb)
	File "/usr/share/pyload/module/web/templates/default/base.html", line 20, in top-level template code 
	
	File "/usr/share/pyload/module/web/templates/default/base.html", line 20, in block "title" 
	
UndefinedError: '_' is undefined 
```

Durch ueberfliegen des Tracebacks wird mir als python-Laie klar, dass irgendwas
mit dem Paket *Jinja2* nicht in Ordnung ist.

Zufaellig wusste ich, dass *Jinja2* auch fuer die [Templates](http://docs.getpelican.com/en/3.2/themes.html)
von Pelican genutzt wird.
Irgendwas muss da durcheinander gekommen sein.

Da ich nichts zu verlieren hatte, wurde pyload runtergeschmissen und komplett neu installiert.
Wie so oft schon geschehen, versprach ich mir auch diesmal eine Art Selbstheilung...

Leider traf dies nicht ganz zu, doch eine hilfreiche Warnung erschien, die mir das 
vermutete Problem mit *Jinja2* bestaetigte:

>"Ihre installierte Version 2.7 von jinja2 scheint veraltet zu sein.
>Sie koennen problemlos fortfahren, sollte jedoch das Webinterface nicht funktionieren,
>sollten Sie es upgraden oder deinstallieren, pyload bringt eine ausreichende jinja2
>Bibliothek mit.
>
>jinja2: fehlt"

Das Webinterface funktionierte immer noch nicht. Also folgte ich den Ratschlaegen des
Installers und wagte mich daran *jinja2* auch neuzuinstallieren. Mir war unwohl dabei,
da ich nicht wusste, ob pelican danach noch funktionieren wuerde...*(haette ich doch damals nicht
die dringenden Hinweise der pelican Entwickler ignoriert, das ganze unbedingt in einem eigenen python
Environment zu installieren um gerade solchen Cross-Kompatibilitaets-Problemen aus dem Weg zu
gehen.)*

Also: *jinja2* deinstallieren... 

``` bash
pip uninstall jinja2
```

...und erneut aufspielen:

``` bash
pip install jinja2
```

und Webinterface testen: *erfolglos!* - Same Error!

Die einzige Loesung, die mir als nicht-Programmierer blieb, aus den ganzen gesammelten
Fehlerfragmenten schlau zu werden, war wieder einmal Foren-Recherche!

Ich erhoffte mir nicht viel davon, weil ich bereits vorher schonmal die pyload Foren vergebens
durchsucht habe und dorkeweiteren hilfreichen Ratschlaege fand.

Doch durch Gottes Weisung fand ich die Loesung in einem [Github Ticket](https://github.com/mitsuhiko/jinja2/issues/225).

Der Ratschlag ist so professionell wie [simpel](/static/pictures/pyload/09-07-2013_jinja2-1.png):

``` bash
sudo nano /usr/local/lib/python2.7/dist-packages/jinja2/loaders.py
# In nano zu Zeile 352 springen: STRG-W, STRG-T, 352
# Den Rueckgabewert um *globals* ergaenzen:
return loader.load(environment, local_name, globals)
# Speichern: STRG-X, y
```

Und wieder einmal wurde bewiesen, wie aufschlussreich eine vernuenftige Webrecherche ist.
Die ganze Vorarbeit haette ich mir auch sparen koennen...




[pelican]: http://blog.getpelican.com/
[pyload]: http://pyload.org/de:start

