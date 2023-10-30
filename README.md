# Sales_prediction
Making use of 5 models to compare their base performance and using a gui to input new data and use new data as input to predict sales

we will be exploring through the intricate nature of sales prediction and model comparison, scrutinizing the meaningfulness of these forecasts. We will inspect different prediction methodologies and models, examining the subtle nuances that differentiate them. 
There are 6 models which we will be using in the testing and to draw conclusions from. The models that will be used are:
•	RandomForestRegression
•	GrasdientBoosterRegressor
•	HistGradientBoosterRegression
•	XGBoost
•	LGBMRegressor
We have made an GUI using tkinter to input data and use it for taking inputs of the parameters. They will be then logged into an excel file and will serve as input for the data.

The selected algorithm will them give predictions for the input data and the results will be logged into a sperate excel file as prediction results.
Dataset: 
The Dataset that we will be using is found on Kaggle and can be downloaded here:
https://www.kaggle.com/datasets/shivan118/big-mart-sales-prediction-datasets/data?select=train.csv

The variables we work with are:
Item ID: The unique identifier for each item in the dataset.
Item Weight: The weight of the item in grams, potentially influencing logistics and transportation costs.
Item Visibility: A measure of how prominently the item is displayed in the store.
Item Fat Content: Classifies items as "Low Fat" or "Regular Fat," affecting consumer choices.
Item Type: Categorizes items into various product types.
Item MRP: The maximum price at which an item can be sold.
Outlet Identifier: Identifies the specific store where the item is sold.
Outlet Establishment Year: The year the store was established, influencing its reputation and customer base.
Outlet Size: Categorizes stores as "Small," "Medium," or "High" in terms of size.
Outlet Location Type: Classifies the store location as "Tier 1," "Tier 2," or "Tier 3."
Outlet Type: Distinguishes between various store types, such as supermarkets or grocery stores.
The dataset has 8523 entries. The dataset was split into 70-30, with training data being the larger 70% and the rest 30% going to the testing. 

Testing Data:
The split leaves us with 5966 data entries to work with. Some of these are null values as well. We will be working on the removal of them later.
The test data has 2 main types of values. Numeric (int64 and float64) and non numeric i.e. object type of values. We will separate them into their respective categories. 
The numeric data contains the following variables.
•	Item_Weight	    
•	Item_Visibility	  
•	Item_MRP  	  
•	Outlet_Establishment_Year  

The non numeric data contains the following variables:
•	Item_Identifier	  
•	Item_Fat_Content	  
•	Item_Type	  
•	Outlet_Identifier	  
•	Outlet_Size	  
•	Outlet_Location_Type	  
•	Outlet_Type  
