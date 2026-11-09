from src.data_cleaning import data_cleaning
from src.univariate_analysis import univariate_analysis
from utils.visualize_helper import separator

if __name__ == "__main__":
    separator('Data Cleaning')
    df = data_cleaning()
    separator('Univariate Analysis')
    univariate_analysis()