
Author: Valentina D'Orazio
E_mail: valentina_dorazio@virgilio.it

###############################################################
################	Introduzione		###############
###############################################################
Il progetto sviluppato si basa su uno studio di fattibilità 
dell’applicazione del Filtro di Kalman al problema del 
positioning indoor. Lo scenario applicativo consiste in 
un’infrastruttura wireless composta da ancore posizionate in 
maniera fissa e nota, le quali fungono da emettitori di segnale,
e da un’antenna ricevente che ha lo scopo di effettuare le misure
di potenza (RSSI) dei segnali emessi dalle ancore. Essendo noto 
il legame tra potenza e distanza tra le antenne è possibile 
risalire alla posizione spaziale in tempo reale dell’oggetto in 
movimento, come ad esempio un drone, sul quale è montato il nodo 
ricevente.

###############################################################
################	localTrackingPYTHON	###############
###############################################################

WINDOWS:

1) Dopo aver importato il progetto (è consigliabile usare PyCharm come IDE)
assicurarsi di utilizzare il file remotAapi.dll corretto (32/64 bit). Nel progetto
è presente quello a 64 bit. Il file a 32 bit è reperibile nella cartella:
V-REP3\V-REP_PRO_EDU\programming\remoteApiBindings\lib\lib\Windows\32Bit

2) Eseguire il file vrep_LSI e successivamente eseguire il progetto in 
Python.

###############################################################
################	localTrackingMATLAB	###############
###############################################################

Eseguire lo script main.m

###############################################################

Per ulteriori informazioni consultare il pdf all'interno della 
cartella doc.
