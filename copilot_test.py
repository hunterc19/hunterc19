import pandas as pd
import numpy as np

def test_dataframe_operations():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    }
    df = pd.DataFrame(data)

    # Test basic operations
    assert df.shape == (4, 3), "Shape mismatch"
    assert df['A'].sum() == 10, "Sum of column A should be 10"
    assert df['B'].mean() == 6.5, "Mean of column B should be 6.5"

    # Test adding a new column
    df['D'] = df['A'] + df['B']
    assert 'D' in df.columns, "Column D should be added"
    assert df['D'].iloc[0] == 6, "First value of column D should be 6"

    # Test filtering
    filtered_df = df[df['A'] > 2]
    assert len(filtered_df) == 2, "Filtered DataFrame should have length 2"
    assert filtered_df['A'].iloc[0] == 3, "First value of filtered column A should be 3"
    assert filtered_df['B'].iloc[0] == 7, "First value of filtered column B should be 7"
    assert filtered_df['C'].iloc[0] == 11, "First value of filtered column C should be 11"

    # Test applying a function
    df['E'] = df['A'].apply(lambda x: x ** 2)
    assert df['E'].iloc[0] == 1, "First value of column E should be 1"
    assert df['E'].iloc[1] == 4, "Second value of column E should be 4"
    assert df['E'].iloc[2] == 9, "Third value of column E should be 9"
    assert df['E'].iloc[3] == 16, "Fourth value of column E should be 16"   
    # Test handling missing values
    df.loc[2, 'A'] = np.nan
    assert df['A'].isnull().sum() == 1, "There should be one missing value in column A"
    df['A'].fillna(0, inplace=True)
    assert df['A'].isnull().sum() == 0, "There should be no missing values in column A after filling"
    # Test groupby operation
    grouped = df.groupby('A').sum()
    assert grouped.shape == (4, 4), "Grouped DataFrame should have shape (4, 4)"
    assert grouped['B'].iloc[0] == 5, "First value of grouped column B should be 5"
    assert grouped['C'].iloc[0] == 9, "First value of grouped column C should be 9"
    assert grouped['D'].iloc[0] == 6, "First value of grouped column D should be 6"
    assert grouped['E'].iloc[0] == 1, "First value of grouped column E should be 1"
    # Test merging DataFrames
    df2 = pd.DataFrame({'A': [1, 2], 'F': [13, 14]})
    merged_df = pd.merge(df, df2, on='A', how='left')
    assert merged_df.shape == (4, 5), "Merged DataFrame should have shape (4, 5)"
    assert merged_df['F'].iloc[0] == 13, "First value of merged column F should be 13"
    assert merged_df['F'].iloc[1] == 14, "Second value of merged column F should be 14"
    assert merged_df['F'].iloc[2] is np.nan, "Third value of merged column F should be NaN"
    assert merged_df['F'].iloc[3] is np.nan, "Fourth value of merged column F should be NaN"
    # Test pivot table
    pivot_df = df.pivot_table(index='A', values=['B', 'C'], aggfunc='sum')
    assert pivot_df.shape == (4, 2), "Pivot table should have shape (4, 2)"
    assert pivot_df['B'].iloc[0] == 5, "First value of pivot column B should be 5"
    assert pivot_df['C'].iloc[0] == 9, "First value of pivot column C should be 9"
    # Test sorting
    sorted_df = df.sort_values(by='B', ascending=False)
    assert sorted_df.iloc[0]['B'] == 8, "First value of sorted column B should be 8"
    assert sorted_df.iloc[1]['B'] == 7, "Second value of sorted column B should be 7"
    assert sorted_df.iloc[2]['B'] == 6, "Third value of sorted column B should be 6"
    assert sorted_df.iloc[3]['B'] == 5, "Fourth value of sorted column B should be 5"
    # Test dropping a column
    df.drop(columns=['D'], inplace=True)
    assert 'D' not in df.columns, "Column D should be dropped"
    # Test resetting index
    df.reset_index(drop=True, inplace=True)
    assert df.index.name is None, "Index name should be None after reset"
    assert df.shape == (4, 4), "DataFrame should have shape (4, 4) after reset"
    # Test saving to CSV
    df.to_csv('test.csv', index=False)
    loaded_df = pd.read_csv('test.csv')
    assert loaded_df.shape == df.shape, "Loaded DataFrame should have the same shape as original"
    assert loaded_df.equals(df), "Loaded DataFrame should be equal to original DataFrame"
    # Test saving to Excel
    df.to_excel('test.xlsx', index=False)
    loaded_df = pd.read_excel('test.xlsx')
    assert loaded_df.shape == df.shape, "Loaded DataFrame should have the same shape as original"
    assert loaded_df.equals(df), "Loaded DataFrame should be equal to original DataFrame"
