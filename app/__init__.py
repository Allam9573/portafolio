from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message


def create_app():
    app = Flask(__name__)

    app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '73990b21480f51'
    app.config['MAIL_PASSWORD'] = 'f7d9bf230ff5f6'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    mail = Mail(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/mail', methods=['POST', 'GET'])
    def send_email():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            msg = Message(
                "Hola Allam, tienes un nuevo correo",
                body=f'Nombre: {name}\nCorreo: {email}\n\nEscribio: {message}',
                sender=email,
                recipients=['allam9573@mailtrap.io']
            )
            mail.send(msg)
            return render_template('send_email.html')
        return redirect(url_for('index'))

    @app.errorhandler(404)
    def error404(error):
        return render_template('error404.html')
    return app
