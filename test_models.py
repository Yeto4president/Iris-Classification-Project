from src.modeling import get_models
from sklearn.datasets import load_iris

def test_models_initialization():
    models = get_models()
    iris = load_iris()
    assert len(models) == 4
    assert all(isinstance(model, type(models['KNN'])) for model in models.values())
