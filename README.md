# Stock Market Prediction (Directional Agreement)

- This project aims to predict directional agreement of Nifty-50 stock on per minute basis.

## Flow of the project:
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure1.png)

## Web-Scrapping:

**Algorithm of web scrapping and more:**
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure13.png)

![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure2.png)
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure3.png)
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure4.png)
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure5.png)

## Nifty-50 Share price (1 min freq.):
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure8.png)

## Processed DataSet:
### Feature Engineering -
After dropping unnecessary features we were left with following features:

1. Time
1. Close
1. High
1. Low
1. Volume

Out of which we used High and Low to calculate another feature which determines the overall fluctuation within that 1 minute timespan.

**Final dataset looked like below:**

![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure7.png)

### Normalization
We performed percentage change operation over all features except time, to normalize the data.

### Scaling
We performed scaling on the normalized data. Here we used StandarScaler which by default scales the data using Normal distribution.

### Sliding Window
As LSTM requires sequential data, we created a sliding window of size 60. By using the sliding window we generated all possible sequences of 60 from the dataset.

### Categorization
We shifted the Close feature by 3 unites and then did compare it with the original column. If the data in future is higher than the current data then we labeled it as "1". If the data in future is lower than the current data then we labeled it as "0".

### Category Balancing
We made sure that there are equal amounts of data points for both categories. Therefore, avoiding the biasing in the model.

## LSTM Architecture
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure18.png)

## Ensemble approach with sentiment analysis:
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure15.png)
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure16.png)

## Results:
![](https://github.com/cmdev007/Stock_Market_Prediction/raw/main/images/figure19.png)