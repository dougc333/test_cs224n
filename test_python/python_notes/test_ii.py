from code import InteractiveInterpreter
#we can use this to replace code in jupyter notebook

import pdb; pdb.set_trace()
code='import numpy as np; a=np.array([1,2,3,4]); print(a)'
i = InteractiveInterpreter()
i.runsource(code)


