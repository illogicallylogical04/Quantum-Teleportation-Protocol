from flask import Flask, request, jsonify
from static.QT import qt

app = Flask(__name__)

@app.route('/teleport', methods=['POST'])
def teleport():
    data = request.json
    prob_0 = float(data['probability0'])
    prob_1 = float(data['probability1'])
    
    # Call the quantum teleportation function
    circuit_image, qsphere_image = qt(prob_0, prob_1)

    return jsonify({
        'circuitImage': circuit_image,
        'qsphereImage': qsphere_image
    })

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
