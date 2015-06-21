class weight_rand():
    """Provides logic for determining a weighted random choice. Not subclassed
    from random.Random or random.SystemRandom because I don't want its behavior
    unduly influenced in ways I can't yet predict by those built-ins."""

    def __init__(self, weighted_dict):
        """By passing in a dictionary of the form dict_name[item] = weight, a
        weighted dictionary object may be created with the relevane weighting
        information."""
        self.wd = weighted_dict

    def __getitem__(self, i):
        return self.wd[i]
