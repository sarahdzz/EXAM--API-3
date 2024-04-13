from flask import Flask, request, jsonify
import platform
import subprocess
import os, platform, re


app = Flask(__name__)


# Ejercicio Examen es el get-hostnameAPI
@app.route('/get-hostnameApi')
def renderCategoryContent():
    if request.method == 'GET':      

        sistema = platform.system()
        if sistema == 'Windows':
            local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
        else:
            local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")


        diccionario = {'ip': local, 'hostname': os.getenv('COMPUTERNAME', 'defaultValue')}
        
        return jsonify(diccionario)  
 
        
if __name__ == "_main_":
   app.run(debug=True)