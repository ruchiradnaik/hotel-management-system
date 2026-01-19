from flask import Flask, request, jsonify
from models import db, Room, Booking

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db.init_app(app)

@app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    return jsonify([room.to_dict() for room in rooms])

@app.route('/book', methods=['POST'])
def book_room():
    data = request.json
    new_booking = Booking(customer_name=data['customer_name'], room_id=data['room_id'])
    db.session.add(new_booking)
    db.session.commit()
    return jsonify(new_booking.to_dict()), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)