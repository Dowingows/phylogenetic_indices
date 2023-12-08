import numpy as np


def species_richness(hist: np) -> int:
    """
    Conta o número de espécies de uma imagem com base em um histograma fornecido.

    Parameters:
        hist: A entrada que representa o histograma da imagem.

    Returns:
        O número de espécies únicas presentes no histograma.

    Raises:
        ValueError: Se o tipo de características não for suportado (não é uma array NumPy).

    Examples:
        >>> import numpy as np
        >>> hist = np.array([1, 2, 3, 1, 2, 3, 4])
        >>> species_richness(hist)
        4
    """
    if isinstance(hist, np.ndarray):

        unique_species = np.unique(hist)
        num_species = len(unique_species)

        return num_species
    else:
        raise ValueError('Unsupported data type')


def taxonomic_distinction(hist: np) -> int:
    """
    Calcula o índice de distinção taxonômica.

    Esta função recebe um histograma de abundância de espécies como entrada e retorna o índice de distinção taxonômica. A função calcula a distância taxonômica média entre todos os pares de espécies, ponderada por suas abundâncias, e então divide esse valor pela abundância total ao quadrado.

    Args:
      hist: Um histograma de abundância de espécies.

    Returns:
      O índice de distinção taxonômica.

    Raises:
        ValueError: Se o tipo de características não for suportado (não é uma array NumPy).

    Examples:
        >>> import numpy as np
        >>> hist = np.array([10, 20, 30])
        >>> taxonomic_distinction(hist)
        0.7909604519774012
    """

    if not isinstance(hist, np.ndarray):
        raise ValueError('Unsupported data type')

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
