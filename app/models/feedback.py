from app.database.db import db
from datetime import datetime


class Feedback(db.Model):
    __tablename__ = "feedback"

    feedback_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    journey_id = db.Column(
        db.Integer,
        db.ForeignKey("journeys.journey_id"),
        nullable=True
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )

    comment = db.Column(
        db.Text,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Feedback {self.feedback_id}>"
