import numpy as np


def species_richness(features: np) -> int:
    """
    Conta o número de espécies com base nas características fornecidas.

    Parameters:
        features: A entrada que representa as características da imagem.

    Returns:
        O número de espécies presentes nas características.

    Raises:
        ValueError: Se o tipo de características não for suportado (não é uma matriz NumPy).

    Examples:
        >>> import numpy as np
        >>> features = np.array([1, 2, 3, 1, 2, 3, 4])
        >>> species_richness(features)
        4
    """
    if isinstance(features, np.ndarray):

        unique_species = np.unique(features)
        num_species = len(unique_species)

        return num_species
    else:
        raise ValueError('Unsupported data type')


def taxonomic_distinction(hist: np) -> int:
    """
    Calcula o índice de distinção taxonômica.

    Args:
      hist: Um histograma de abundância de espécies.

    Returns:
      O índice de distinção taxonômica.

    Examples:
        >>> import numpy as np
        >>> hist = np.array([10, 20, 30])
        >>> taxonomic_distinction(hist)
        0.7909604519774012
    """

    # num_species = len(hist)
    num_species = species_richness(hist)

    mean_dist = 0
    for i in range(num_species):
        for j in range(i + 1, num_species):
            dist = abs(i - j)
            mean_dist += dist * hist[i] * hist[j]

    total_abundance = np.sum(hist)

    taxonomic_distinction = (
        2 * mean_dist / (total_abundance * (total_abundance - 1))
    )

    return taxonomic_distinction