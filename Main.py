from flask import Flask, render_template, request, redirect, url_for

        # Opretter en Flask app
app = Flask(__name__)

        # Opretter et dictionary med tjenester og deres status
services = {
        # Tjenester og deres status
    "Internet": "OK",
    "Docker": "OK",
    "Kubernetes": "OK",
    "Proxmox": "OK"
}

        # En dictionary til at holde meddelelser per service
messages = {}
        # Opretter en route for hjemmesiden
@app.route('/')
        # Funktion der håndterer visningen af hjemmesiden
def home():
        # render template og send både services og messages
    return render_template('home.html', services=services, messages=messages)

        # Admin-side hvor man kan tilføje meddelelser og ændre status
        # Bruger både GET og POST for at håndtere formularen
@app.route('/admin', methods=['GET', 'POST'])
def admin():
        # Hvis formularen er sendt
    if request.method == 'POST':
        service = request.form.get('service')
        note = request.form.get('note')
        new_status = request.form.get('status')
        # opdater status hvis der er en ny
        if service and new_status:
            services[service] = new_status
        # håndter note, hvis den er tom skal den fjernes
        if service:
            if note and note.strip():
                messages[service] = note
            else:
                messages.pop(service, None)
        # efter post redirect til admin for at undgå at genindlæse data ved refresh
        return redirect(url_for('admin'))

        # ved GET vis admin-form
        # send også nuværende services dictionary for at kunne vise status og eksisterende meddelelser
    return render_template('admin.html', services=services.keys(), current_status=services)

        # Kører appen
        # Flask appen kører på alle interfaces på port 5000, og debug mode er aktiveret for nem fejlfinding
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)