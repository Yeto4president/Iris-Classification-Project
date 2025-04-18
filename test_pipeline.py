import pytest
from src.data_loading import load_data
from src.preprocessing import preprocess_data
from src.modeling import train_model

def test_data_loading():
    X, y = load_data()
    assert X.shape == (150, 4)
    assert len(y) == 150

def test_preprocessing():
    X, y = load_data()
    X_scaled = preprocess_data(X)
    assert X_scaled.mean() == pytest.approx(0, abs=1e-2)
    assert X_scaled.std() == pytest.approx(1, abs=1e-2)

@pytest.mark.parametrize("model_name", ["KNN", "Decision Tree"])
def test_model_training(model_name):
    X, y = load_data()
    X_scaled = preprocess_data(X)
    model = train_model(X_scaled, y, model_name)
    assert hasattr(model, "predict")
