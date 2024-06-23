from data_models.exceptions import ConclusionError
from data_models.match import Match, MatchResult
from data_models.model_store import db
from . import players as p_logic


def conclude(match: Match):
    if match.result not in [
        MatchResult.CORP_WIN.value,
        MatchResult.RUNNER_WIN.value,
        MatchResult.DRAW.value,
        MatchResult.INTENTIONAL_DRAW.value,
        MatchResult.CORP_CORP_CORP_WIN.value,
        MatchResult.CORP_CORP_RUNNER_WIN.value,
        MatchResult.CORP_CORP_DRAW_WIN.value,
        MatchResult.CORP_DRAW_DRAW_WIN.value,
        MatchResult.CORP_DRAW_RUNNER_WIN.value,
        MatchResult.RUNNER_RUNNER_RUNNER_WIN.value,
        MatchResult.RUNNER_RUNNER_CORP_WIN.value,
        MatchResult.RUNNER_RUNNER_DRAW_WIN.value,
        MatchResult.RUNNER_DRAW_DRAW_WIN.value,
        MatchResult.DRAW_DRAW_DRAW.value,
    ]:
        raise ConclusionError("No result recorded")
    match.concluded = True
    db.session.add(match)
    db.session.commit()


def corp_win(match: Match):
    match.result = MatchResult.CORP_WIN.value
    db.session.add(match)
    db.session.commit()

def corp_corp_corp_win(match: Match):
    match.result = MatchResult.CORP_CORP_CORP_WIN.value
    db.session.add(match)
    db.session.commit()

def corp_corp_runner_win(match: Match):
    match.result = MatchResult.CORP_CORP_RUNNER_WIN.value
    db.session.add(match)
    db.session.commit()

def corp_corp_draw_win(match: Match):
    match.result = MatchResult.CORP_CORP_DRAW_WIN.value
    db.session.add(match)
    db.session.commit()

def corp_draw_draw_win(match: Match):
    match.result = MatchResult.CORP_DRAW_DRAW_WIN.value
    db.session.add(match)
    db.session.commit()

def corp_draw_runner_win(match: Match):
    match.result = MatchResult.CORP_DRAW_RUNNER_WIN.value
    db.session.add(match)
    db.session.commit()

def draw_draw_draw(match: Match):
    match.result = MatchResult.DRAW_DRAW_DRAW.value
    db.session.add(match)
    db.session.commit()

def runner_runner_runner_win(match: Match):
    match.result = MatchResult.RUNNER_RUNNER_RUNNER_WIN.value
    db.session.add(match)
    db.session.commit()

def runner_runner_corp_win(match: Match):
    match.result = MatchResult.RUNNER_RUNNER_CORP_WIN.value
    db.session.add(match)
    db.session.commit()

def runner_runner_draw_win(match: Match):
    match.result = MatchResult.RUNNER_RUNNER_DRAW_WIN.value
    db.session.add(match)
    db.session.commit()

def runner_draw_draw_win(match: Match):
    match.result = MatchResult.RUNNER_DRAW_DRAW_WIN.value
    db.session.add(match)
    db.session.commit()


def runner_win(match: Match):
    match.result = MatchResult.RUNNER_WIN.value
    db.session.add(match)
    db.session.commit()


def tie(match: Match):
    match.result = MatchResult.DRAW.value
    db.session.add(match)
    db.session.commit()


def intentional_draw(match: Match):
    match.result = MatchResult.INTENTIONAL_DRAW.value
    db.session.add(match)
    db.session.commit()


def reset(match: Match):
    match.result = None
    match.concluded = False
    db.session.add(match)
    db.session.commit()


def delete(match: Match):
    if match.is_bye:
        match.corp_player.recieved_bye = False
        # p_logic.reset(match.corp_player)
    # else:
    #     p_logic.reset(match.corp_player)
    #     p_logic.reset(match.runner_player)
    db.session.delete(match)
    db.session.commit()
