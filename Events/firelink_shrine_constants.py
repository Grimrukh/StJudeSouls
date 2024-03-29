import soulstruct.emevd.ds_types as dt


class CHR(dt.Character):
    Solaire = 6001
    Logan = 6031
    Quelana = 6171
    Siegmeyer = 6281
    Patches = 6321
    Havel = 6581
    Ornstein = 1020527
    Sif = 1020452

    Anastacia = 6060
    Frampt = 6330
    FemaleUndeadMerchant = 6240  # For Burg level (sells Remote Detonator).

    GoToDepths = 1020403  # NPC interaction.


class FLAG(dt.Flag):
    SolaireRecruited = 1900
    SiegmeyerRecruited = 1901
    PatchesRecruited = 1902
    OrnsteinRecruited = 1903
    LoganRecruited = 1904
    HavelRecruited = 1905
    QuelanaRecruited = 1906
    SifRecruited = 1907

    AlliesKilled = 1910
    PatchesKilled = 1911

    FramptHelpReceived = 71800026
    FramptOfferedWarp = 71800033

    SerpentSoulDestroyed = 11022006
    FramptHasEatenYou = 11022009

    BattleStarted = 11212001


class ITEMLOT(dt.ItemLot):
    FramptGift = 4640


class REGION(dt.Region):
    GoToUndeadBurg = 1022400
    GoToSensFortress = 1022401
    GoToCatacombs = 1022402
    ReturnFromUndeadBurg = 1022404  # Technically in Firelink Shrine map.


class SPEFFECT(dt.IntEnum):
    HalfSpeed = 4701
    RingOfTheSerpent = 4708


class TEXT(dt.Text):
    ReturnToFirelink = 10010140
    TravelToCity = 10010141
    TravelToFortress = 10010142
    TravelToCatacombs = 10010143
    TravelToDepths = 10010146
    LetFramptEatYou = 10010147
    BurnSerpentSoul = 10010381
    RestToReviveFriends = 10010382
    RestAndEnd = 10010383


class GOOD(dt.Good):
    SerpentSoul = 420
