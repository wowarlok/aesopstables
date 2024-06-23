from data_models.model_store import db
from sqlalchemy import Enum

import enum

class MatchResult(enum.Enum):
    CORP_WIN = 1
    CORP_CORP_CORP_WIN = 2
    CORP_CORP_RUNNER_WIN = 3
    CORP_CORP_DRAW_WIN = 4
    CORP_DRAW_DRAW_WIN = 5
    CORP_DRAW_RUNNER_WIN = 10
    RUNNER_WIN = -1
    RUNNER_RUNNER_RUNNER_WIN = -2
    RUNNER_RUNNER_CORP_WIN = -3
    RUNNER_RUNNER_DRAW_WIN = -4
    RUNNER_DRAW_DRAW_WIN = -5
    DRAW_DRAW_DRAW = -10
    DRAW = 0
    INTENTIONAL_DRAW = 9

class MatchReport(enum.Enum):
    CORP_WIN = 1
    CORP_CORP_CORP_WIN = 3
    CORP_CORP_RUNNER_WIN = 5
    CORP_CORP_DRAW_WIN = 7
    CORP_DRAW_DRAW_WIN = 9
    CORP_DRAW_RUNNER_WIN = 11
    RUNNER_WIN = 2
    RUNNER_RUNNER_RUNNER_WIN = 4
    RUNNER_RUNNER_CORP_WIN = 6
    RUNNER_RUNNER_DRAW_WIN = 8
    RUNNER_DRAW_DRAW_WIN = 10
    DRAW_DRAW_DRAW = 12
    DRAW = 0
    INTENTIONAL_DRAW = 9

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer, db.ForeignKey("tournament.id"))
    rnd = db.Column(db.Integer)
    corp_player_id = db.Column(db.Integer, db.ForeignKey("player.id"))
    runner_player_id = db.Column(db.Integer, db.ForeignKey("player.id"))
    result = db.Column(db.Integer)
    concluded = db.Column(db.Boolean, default=False)
    is_bye = db.Column(db.Boolean, default=False)
    table_number = db.Column(db.Integer)

    corp_player = db.relationship(
        "Player",
        foreign_keys=[corp_player_id],
        backref="corp_matches",
    )
    runner_player = db.relationship(
        "Player", foreign_keys=[runner_player_id], backref="runner_matches"
    )
    tournament = db.relationship("Tournament", back_populates="matches")

    def __repr__(self) -> str:
        return f"<Match> TID: {self.tid} - RND: {self.rnd} - Result: {self.result}"
