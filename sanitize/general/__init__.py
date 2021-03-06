from sanitize.general.general import SanitizeGeneralDaySchoolCandidates, SanitizeGeneralAllCandidates
from sanitize.general.best_5 import SanitizeBest5DaySchoolCandidates, SanitizeBest5AllCandidates
from sanitize.general.best_6 import SanitizeBest6DaySchoolCandidates, SanitizeBest6AllCandidates
from sanitize.general.sen import SanitizeSEN
from sanitize.general.level_distribution import SanitizeLevelDistribution
from sanitize.general.top_levels import SanitizeTopLevels


def sanitize_general() -> None:
    SanitizeGeneralDaySchoolCandidates()
    SanitizeGeneralAllCandidates()
    SanitizeBest5DaySchoolCandidates()
    SanitizeBest5AllCandidates()
    SanitizeBest6DaySchoolCandidates()
    SanitizeBest6AllCandidates()
    SanitizeSEN()
    SanitizeLevelDistribution()
    SanitizeTopLevels()
