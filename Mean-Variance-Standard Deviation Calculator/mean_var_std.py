import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  calculations = {}
  A_flattened = np.array(list)
  A = A_flattened.reshape((3,3))

  mean_cols = [np.mean(A[:, i:i+1]) for i in range(3)]
  mean_rows = [np.mean(A[i:i+1, :]) for i in range(3)]
  mean_flattened = np.mean(A_flattened)
  calculations['mean'] = [mean_cols, mean_rows, mean_flattened]

  var_cols = [np.var(A[:, i:i+1]) for i in range(3)]
  var_rows = [np.var(A[i:i+1, :]) for i in range(3)]
  var_flattened = np.var(A_flattened)
  calculations['variance'] = [var_cols, var_rows, var_flattened]
  
  std_cols = [np.std(A[:, i:i+1]) for i in range(3)]
  std_rows = [np.std(A[i:i+1, :]) for i in range(3)]
  std_flattened = np.std(A_flattened)
  calculations['standard deviation'] = [std_cols, std_rows, std_flattened]

  max_cols = [np.max(A[:, i:i+1]) for i in range(3)]
  max_rows = [np.max(A[i:i+1, :]) for i in range(3)]
  max_flattened = np.max(A_flattened)
  calculations['max'] = [max_cols, max_rows, max_flattened]

  min_cols = [np.min(A[:, i:i+1]) for i in range(3)]
  min_rows = [np.min(A[i:i+1, :]) for i in range(3)]
  min_flattened = np.min(A_flattened)
  calculations['min'] = [min_cols, min_rows, min_flattened]

  sum_cols = [np.sum(A[:, i:i+1]) for i in range(3)]
  sum_rows = [np.sum(A[i:i+1, :]) for i in range(3)]
  sum_flattened = np.sum(A_flattened)
  calculations['sum'] = [sum_cols, sum_rows, sum_flattened]    
  
  return calculations