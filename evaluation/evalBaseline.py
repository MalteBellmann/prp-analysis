from evaluation.helpers import load_value
import pandas as pd
import matplotlib.pyplot as plt

# %%
x = []

ns_options = [100, 400, 900]

for ns in ns_options:
    ns_name = "simpleNetwork_5min_%dNodes_100MB" % ns

    d = {
        "Number of Nodes": ns,

        "Availability": load_value(ns_name, "Alg001", "Availability"),
        "Lost@Start": load_value(ns_name, "Alg001", "Lost@Start"),
        "Lost@Move": load_value(ns_name, "Alg001", "Lost@Move"),
    }
    x.append(d)

x_df = pd.DataFrame(x).set_index("Number of Nodes")

# %%

print(x_df.to_latex())
