from app.database.db import db


class Connection(db.Model):
    __tablename__ = "connections"

    connection_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    from_stop_id = db.Column(
        db.Integer,
        db.ForeignKey("bus_stops.stop_id"),
        nullable=False
    )

    to_stop_id = db.Column(
        db.Integer,
        db.ForeignKey("bus_stops.stop_id"),
        nullable=False
    )

    route_id = db.Column(
        db.Integer,
        db.ForeignKey("routes.route_id"),
        nullable=False
    )

    distance_km = db.Column(db.Float, nullable=False)

    travel_time = db.Column(db.Integer, nullable=False)

    transport_type = db.Column(
        db.String(50),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    def __repr__(self):
        return f"<Connection {self.from_stop_id} to {self.to_stop_id}>"
