from app.database.db import db


class Route(db.Model):
    __tablename__ = "routes"

    route_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    route_name = db.Column(db.String(100), nullable=False)

    route_type = db.Column(db.String(50), nullable=False)

    start_point = db.Column(db.String(100), nullable=False)

    end_point = db.Column(db.String(100), nullable=False)

    distance_km = db.Column(db.Float, nullable=True)

    estimated_time = db.Column(db.Integer, nullable=True)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="active"
    )

    def __repr__(self):
        return f"<Route {self.route_name}>"
