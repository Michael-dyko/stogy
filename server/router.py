from flask import Flask, jsonify

def use_router(app):
    # sanity check route
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')