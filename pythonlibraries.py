def data_frame():
    import numpy as np
    import pandas as pd
    array_list=np.array([1,2,3,4,5,6])
    print(array_list**2)
    print(f"mean value o array is:{np.mean(array_list)}")
    #abhay_data={'name':["Abhay"], "age":[35],"job":["developer"]}
    abhay_data={'name':["Abhay","Khushboo","Yuvaan","Kiaan"], "age":[35,34,9,2],"job":["developer","HR","student","student"]}
    abhay_df=pd.DataFrame(abhay_data)
    print(abhay_df)
data_frame()