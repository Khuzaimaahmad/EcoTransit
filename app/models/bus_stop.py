from app.database.db import db


class BusStop(db.Model):
    __tablename__ = "bus_stops"

    stop_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stop_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(255), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    stop_type = db.Column(db.String(50), nullable=False)

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    def __repr__(self):
        return f"<BusStop {self.stop_name}>"
