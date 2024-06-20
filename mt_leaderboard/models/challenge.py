from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class ClassInfo(BaseModel):
    className: str
    classLevel: int
    championIndex: int


class StartingConditions(BaseModel):
    enabledDlcs: List[int]
    seed: int
    isBattleMode: bool
    battleModeStartTime: datetime
    version: str
    mainClassInfo: ClassInfo
    subclassInfo: ClassInfo
    ascensionLevel: int
    blessings: List[str]
    covenants: List[str]
    mutators: List[str]


class Challenge(BaseModel):
    serverTimeInSeconds: int
    id: str
    startTime: datetime
    endTime: datetime
    pubnubChannel: str
    pubnubPresenceTimeout: int
    pubnubPresenceInterval: int
    startingConditions: StartingConditions
