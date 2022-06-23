import numpy as np

def calculate(list):
    if len(list) != 9 : 
        raise ValueError ("List must contain nine numbers.")
    else:
        a = list
        x = np.reshape((a), (1, 3, 3))
        calculations ={
            'mean': [(np.mean(x[0] , axis=0)).tolist() , (np.mean(x[0] , axis=1)).tolist() , np.mean(x)] ,

            'variance': [(np.var(x[0], axis=0)).tolist(), (np.var(x[0], axis=1)).tolist(), np.var(x)],

            'standard deviation': [(np.std(x[0] , axis=0)).tolist(), (np.std(x[0], axis=1)).tolist(), np.std(x)],

            'max': [(np.max(x[0], axis=0)).tolist(), (np.max(x[0], axis=1)).tolist() , np.max(x)] ,

            'min': [(np.amin(x[0], axis=0)).tolist() , (np.amin(x[0], axis=1)).tolist() , np.min(x)] ,

            'sum': [(np.sum(x[0], axis=0)).tolist(), (np.sum(x[0], axis=1)).tolist(), np.sum(x) ]
            
        }
        aa = {
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
        y = calculations
        if aa ==y:
            print('yes')
        else:
            print('no')

        return calculations

