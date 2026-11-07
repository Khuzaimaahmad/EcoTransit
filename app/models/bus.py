from app.database.db import db


class Bus(db.Model):
    __tablename__ = "buses"

    bus_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bus_number = db.Column(db.String(30), unique=True, nullable=False)
    bus_type = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    fuel_type = db.Column(db.String(30), nullable=False)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="active"
    )

    def __repr__(self):
        return f"<Bus {self.bus_number}>"
