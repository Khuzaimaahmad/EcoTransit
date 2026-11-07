from app.database.db import db
from datetime import datetime


class PassengerDemand(db.Model):
    __tablename__ = "passenger_demand"

    demand_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    stop_id = db.Column(
        db.Integer,
        db.ForeignKey("bus_stops.stop_id"),
        nullable=False
    )

    route_id = db.Column(
        db.Integer,
        db.ForeignKey("routes.route_id"),
        nullable=True
    )

    passenger_count = db.Column(
        db.Integer,
        nullable=False
    )

    demand_level = db.Column(
        db.String(30),
        nullable=False
    )

    recorded_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<PassengerDemand {self.demand_id}>"
