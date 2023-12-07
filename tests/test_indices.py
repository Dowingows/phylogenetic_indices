import numpy as np
import pytest

from phylogenetic_indices.indices import species_richness


def test_species_richness_success():
    hist = np.array([0, 1, 2, 3, 1, 2, 3, 4, 1])
    result = species_richness(hist)

    assert 5 == result


def test_species_richness_error():
    hist_list = [0, 5, 8, 0, 3]

    with pytest.raises(ValueError, match='Unsupported data type'):
        species_richness(hist_list)