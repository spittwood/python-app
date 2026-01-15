from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify(
        {
            "message": "Lorem Ipsum",
            'hostname': socket.gethostname(),
            "time": datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        }
    )

@app.route('/api/v1/healthz')

def health():
    return jsonify({"status": "up"}),200
    

if __name__ == '__main__':
    
    app.run(host="0.0.0.0")
