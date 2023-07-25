class Agreement:
    def __init__(self, gng_name: str, from_sector: str, to_sector: str, gng_notes: str, sortorder: int, fix_before: str, dep_rwy: str, copx_fix: str, fix_after: str , arr_rwy: str, climb: int, descend: int, from_vacc: str, to_vacc: str, at_level: bool = True, cop_display: str = None, from_sector_display: str = None, to_sector_display: str = None, footnote: str = None, special_conditions: str = None, is_altitude: bool = False):
        # Values for GNG
        self.from_vacc = from_vacc
        self.to_vacc = to_vacc
        self.gng_name = gng_name
        self.from_sector = from_sector
        self.to_sector = to_sector
        self.gng_notes = gng_notes
        self.sortorder = sortorder
        self.fix_before = fix_before
        self.dep_rwy = dep_rwy
        self.copx_fix = copx_fix
        self.fix_after = fix_after
        self.arr_rwy = arr_rwy
        self.climb = climb
        self.descend = descend

        # Values for LoAs
        self.at_level = at_level
        self.cop_display = cop_display
        self.from_sector_display = from_sector_display
        self.to_sector_display = to_sector_display
        self.footnote = footnote
        self.special_conditions = special_conditions
        self.is_altitude = is_altitude

    def make_ese_entry(self):
        if self.from_vacc == self.to_vacc:
            type = 'COPX'
        else:
            type = 'FIR_COPX'
        return f'{type}:{self.fix_before}:{self.dep_rwy}:{self.copx_fix}:{self.fix_after}:{self.arr_rwy}:{self.from_vacc}·{self.from_sector}:{self.to_vacc}·{self.to_sector}:{self.climb}:{self.descend}:{self.gng_name}'

