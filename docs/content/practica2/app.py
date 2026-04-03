from flask import Flask, render_template, request, redirect, url_for, flash
from models.parking import ParkingLot, ParkingSpot, VehicleType, Car, Motorcycle, HourlyRatePolicy

app = Flask(__name__)
app.secret_key = "clave_secreta_uabc"

# Instancia global para persistencia en memoria durante la ejecución
spots = [ParkingSpot(f"C{i}", VehicleType.CAR) for i in range(1, 6)] + \
        [ParkingSpot(f"M{i}", VehicleType.MOTORCYCLE) for i in range(1, 4)]
parking_system = ParkingLot(spots, HourlyRatePolicy())

@app.route('/')
def index():
    status = parking_system.get_status()
    return render_template('dashboard.html', 
                           occupied=status['occupied'], 
                           total=status['total'],
                           tickets=status['tickets'],
                           revenue=parking_system.total_revenue)

@app.route('/entry', methods=['GET', 'POST'])
def entry():
    if request.method == 'POST':
        plate = request.form['plate']
        v_type = request.form['type']
        
        v = Car(plate) if v_type == 'CAR' else Motorcycle(plate)
        ticket = parking_system.enter_vehicle(v)
        
        if ticket:
            flash(f"Entrada registrada: Ticket #{ticket['id']}", "success")
            return redirect(url_for('index'))
        flash("No hay lugares disponibles", "danger")
        
    return render_template('entry.html')

@app.route('/exit', methods=['POST'])
def exit_vehicle():
    ticket_id = int(request.form['ticket_id'])
    costo = parking_system.exit_vehicle(ticket_id)
    if costo is not None:
        flash(f"Salida procesada. Cobro: ${costo}", "info")
    else:
        flash("Ticket inválido", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)