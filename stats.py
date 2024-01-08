class Stats:
    def __init__(self, base_stats=None) -> None:
        self._stats = {}
        if base_stats:
            self._stats.update(base_stats)

    def __setitem__(self stat_name, value) -> None:
        self.stats[stat_name] = value
    
    def __contains__(self, stat_name) -> bool:
        return stat_name in self._stats
    
    def get_displayable_attributes(self, filter_criteria):
        # TODO logic to filter
        return self._stats.items()