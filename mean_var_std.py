import numpy as np

def calculate(list):
        
        # make a condition if the list number is less than nine (9)
        # raise "ValueError" if list number less than nine (9)
        if len(list) < 9:
            raise ValueError("List must contain nine numbers.")
        
        else:
            # convert list into numpy array
            array_1d = np.array(list)

            # convert array in 1 dimension into 3 dimension
            array_2d = array_1d.reshape(3,3)
            
            # take mean value of col, row, and all element of the list
            col_mean = np.mean(array_2d, axis=0)
            row_mean = np.mean(array_2d, axis=1)
            all_mean = np.mean(array_2d)

            # convert mean values to dictionary
            mean_dict = {
                 'mean': [
                      col_mean.tolist(),
                      row_mean.tolist(),
                      all_mean.item(0)
                 ]
            }

            # take var value of col, row, and all element of the list
            col_var = np.var(array_2d, axis=0)
            row_var = np.var(array_2d, axis=1)
            all_var = np.var(array_2d)

            # convert var values to dictionary
            var_dict = {
                 'variance': [
                      col_var.tolist(),
                      row_var.tolist(),
                      all_var.item(0)
                 ]
            }

            # take std value of col, row, and all element of the list
            col_std = np.std(array_2d, axis=0)
            row_std = np.std(array_2d, axis=1)
            all_std = np.std(array_2d)

            # convert std values to dictionary
            std_dict = {
                 'standard deviation': [
                      col_std.tolist(),
                      row_std.tolist(),
                      all_std.item(0)
                 ]
            }

            # take max value of col, row, and all element of the list
            col_max = np.max(array_2d, axis=0)
            row_max = np.max(array_2d, axis=1)
            all_max = np.max(array_2d)

            # convert max values to dictionary
            max_dict = {
                 'max': [
                      col_max.tolist(),
                      row_max.tolist(),
                      all_max.item(0)
                 ]
            }

            # take min value of col, row, and all element of the list
            col_min = np.min(array_2d, axis=0)
            row_min = np.min(array_2d, axis=1)
            all_min = np.min(array_2d)

            # convert min values to dictionary
            min_dict = {
                 'min': [
                      col_min.tolist(),
                      row_min.tolist(),
                      all_min.item(0)
                 ]
            }

            # take sum value of col, row, and all element of the list
            col_sum = np.sum(array_2d, axis=0)
            row_sum = np.sum(array_2d, axis=1)
            all_sum = np.sum(array_2d)

            # convert sum values to dictionary
            sum_dict = {
                 'sum': [
                      col_sum.tolist(),
                      row_sum.tolist(),
                      all_sum.item(0)
                 ]
            }

            # unpacking each dictionary into one combination of dictionary
            # in Python, the double asterisk (**) is used for dictionary unpacking.
            calculations = {
                **mean_dict,
                **var_dict,
                **std_dict,
                **max_dict,
                **min_dict,
                **sum_dict
            }

            return calculations