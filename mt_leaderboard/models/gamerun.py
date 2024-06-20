from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class ClassInfo(BaseModel):
    className: str
    classLevel: int
    championIndex: int


class CardUpgrade(BaseModel):
    cardUpgradeDataId: str
    attackDamage: int
    additionalHP: int
    costReduction: int
    additionalHeal: int
    additionalSize: int
    statusEffectUpgrades: List[dict]
    traitDataUpgrades: List[dict]
    triggerUpgrades: List[dict]


class CardModifiers(BaseModel):
    additionalDamage: int
    additionalMaxHP: int
    additionalCost: int
    additionalHeal: int
    additionalSize: int
    cardTraitReplacements: List[dict]
    cardUpgrades: List[CardUpgrade]
    mergedCardStateIDs: List[int]


class Card(BaseModel):
    cardDataID: str
    cardModifiers: CardModifiers


class Blessing(BaseModel):
    relicDataID: str


class CompletedBattle(BaseModel):
    battleIndex: int
    scenarioIndex: int
    scoreEvent: str
    turnsLasted: int
    totalTurns: int
    healthLost: int
    trialID: str
    bossHPRemaining: str


class BuildVersion(BaseModel):
    number: str


class StartingConditions(BaseModel):
    seed: str
    isBattleMode: bool
    version: str
    mainClassInfo: ClassInfo
    subclassInfo: ClassInfo
    ascensionLevel: int
    spChallengeId: Optional[str]
    covenants: List[str]
    mutators: List[str]
    enabledDlcs: List[str]


class InitiatorData(BaseModel):
    shareCode: Optional[str]


class Gamerun(BaseModel):
    buildVersion: BuildVersion
    startingConditions: StartingConditions
    initiatorData: InitiatorData
    id: str
    analyticsPlayerId: str
    analyticsPlayerFriendlyName: str
    runType: str
    isBattleMode: bool
    battleModeRank: int
    runTime: int
    numBattlesWon: int
    score: int
    hpOverTime: List[int]
    gold: int
    goldOverTime: List[int]
    crystals: int
    saveDate: datetime
    cards: List[Card]
    blessings: List[Blessing]
    completedBattles: List[CompletedBattle]
    victory: bool
    mergedCards: List[Card]
