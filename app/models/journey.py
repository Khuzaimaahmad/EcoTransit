from app.database.db import db
from datetime import datetime


class Journey(db.Model):
    __tablename__ = "journeys"

    journey_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=True
    )

    start_stop_id = db.Column(
        db.Integer,
        db.ForeignKey("bus_stops.stop_id"),
        nullable=False
    )

    end_stop_id = db.Column(
        db.Integer,
        db.ForeignKey("bus_stops.stop_id"),
        nullable=False
    )

    total_distance = db.Column(db.Float, nullable=True)

    estimated_time = db.Column(db.Integer, nullable=True)

    transport_mode = db.Column(db.String(50), nullable=True)

    co2_saved = db.Column(db.Float, nullable=True)

    journey_status = db.Column(
        db.String(30),
        nullable=False,
        default="planned"
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Journey {self.journey_id}>"
