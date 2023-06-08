import numpy as np
import scipy.integrate

class System:
    @property
    def matrix(self):
        return(self._matrix)
    
    @property
    def results(self):
        return(self._results)
    
    @property
    def y(self):
        return(self._results.y)
    
    @property
    def t(self):
        return(self._results.t)
    
    @property
    def isomer_names(self):
        return(self._isomer_names)

    def solve_system(self, t_eval):
        def derivatives(t, y):
            derivative = np.matmul(self.matrix, y)

            return(derivative)

        t_span = np.array((t_eval[0], t_eval[-1]))

        self_results = self._results = scipy.integrate.solve_ivp(derivatives, t_span, self._initial_conditions, t_eval=t_eval)



        
        