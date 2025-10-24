def main():
    import pandas as pd
    import numpy as np
    dataset = pd.read_csv('mushrooms.csv')
    edible_count=int((dataset['class']=='e').sum())
    total_count=dataset.shape[0]
    edible_percentage=(edible_count/total_count)*100

    # 2. Extract unique cap colors
    cap_colors=np.unique(dataset['cap-color'].values)

    # Write your code here. Do not change any other parts of the code
    print("edible_count:",edible_count)
    print("edible_percentage:",edible_percentage)
    print("cap_colors:",cap_colors)


    return edible_count, edible_percentage, cap_colors
if __name__=="__main__":
    main()

