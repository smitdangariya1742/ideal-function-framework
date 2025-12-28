import pandas as pd
from analyzer import LeastSquaresSelector
from mapper import Mapper

def test_least_squares_selection():
    train_df = pd.DataFrame({'X':[0,1,2],'Y1':[0,1,2]})
    ideal_df = pd.DataFrame({'X':[0,1,2],'Y1':[0,1,2],'Y2':[0,0,0]})
    selector = LeastSquaresSelector()
    selected, _ = selector.select_ideal_functions(train_df, ideal_df)
    assert selected == [1]

def test_mapper():
    ideal_df = pd.DataFrame({'X':[0,1,2],'Y1':[0,1,2]})
    mapper = Mapper([1], ideal_df, {1:1})
    test_df = pd.DataFrame({'X':[1.5],'Y':[1.5]})
    mapped = mapper.map_dataset(test_df)
    assert mapped['IdealFunc'].iloc[0] == 1
