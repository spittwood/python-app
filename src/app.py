from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/info')

def details():
    return jsonify(
        {
            "message": "Gordon's Alive!!!",
            'hostname': socket.gethostname(),
            "time": datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
            'deployed_on': "Kubernetes with ArgoCD"
        }
    )

@app.route('/api/v1/healthz')

def health():
    return jsonify({"status": "up"}),200
    

if __name__ == '__main__':
    
    app.run(host="0.0.0.0")
