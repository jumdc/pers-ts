import numpy as np
from matplotlib import pyplot as plt

class ACF():
    """
    Class to compute autocorrelation function (ACF).
    
    Parameters
    ----------
    self.ts : time series to compute ACF on. 
    """
    def __init__(self, ts):
        self.ts = ts
        self.mean = np.mean(ts)
        self.T = len(ts)
    
    
    def acf_lag(self, k):
        """
        Compute ACF for one particular laf.
        
        Parameters 
        ----------
        k : lag.
        """
        numerator = np.sum([
            (self.ts[t] - self.mean) * (self.ts[t-k] - self.mean)
            for t in range(k,self.T)
        ])
        denumerator = np.sum([
            (self.ts[t] - self.mean) ** 2
            for t in range(self.T)
        ])
        
        return numerator/denumerator
    
    def acf_lags(self, lags):
        """
        Compute acf for several lags.
        
        Parameters
        ----------
        self : ACF object.
        lags : list.
            list of lags to compute ACF on. 
        """
        results = []
        for lag in lags : 
            results.append(
                self.acf_lag(lag)
            )
        return results
    
    
    def plot_acf(self, lags, lag_values):
        plt.figure()
        plt.title('Autocorrelation plot')
        for idx, lag in enumerate(lags):
            if lag_values[idx] > 0: 
                plt.vlines(lag, 0, lag_values[idx])
            else:
                plt.vlines(lag, lag_values[idx], 0) 
        #plt.scatter(lags, lag_values)
        plt.show()
        

    @staticmethod
    def get_lag_0(r_lags):
        """
        Get the index of the lag with the corelation closest to 0. 
        
        r_lags : list.
            correlation values for the relevant lags.
        """
        r_lags = np.array(r_lags)
        index = np.where(r_lags < 0)[0][0]
        return index