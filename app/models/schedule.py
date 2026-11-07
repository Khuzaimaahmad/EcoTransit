from app.database.db import db


class Schedule(db.Model):
    __tablename__ = "schedules"

    schedule_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    bus_id = db.Column(
        db.Integer,
        db.ForeignKey("buses.bus_id"),
        nullable=False
    )

    route_id = db.Column(
        db.Integer,
        db.ForeignKey("routes.route_id"),
        nullable=False
    )

    departure_time = db.Column(db.Time, nullable=False)

    arrival_time = db.Column(db.Time, nullable=False)

    operating_days = db.Column(db.String(100), nullable=False)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="active"
    )

    def __repr__(self):
        return f"<Schedule {self.schedule_id}>"
