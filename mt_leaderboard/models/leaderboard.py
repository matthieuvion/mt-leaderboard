from typing import List, Optional

from pydantic import BaseModel, Field


class LeaderboardEntry(BaseModel):
    playerId: str
    friendlyName: str
    runId: str
    score: int
    victory: bool
    rank: int
    runTime: int


class TargetPlayer(BaseModel):
    rank: int
    offset: int


class Leaderboard(BaseModel):
    challengeId: str
    targetPlayer: TargetPlayer
    pageCount: int
    currentPage: int
    leaderboard: List[LeaderboardEntry]
