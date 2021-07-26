from evaluation.helpers import load_value
import pandas as pd

# %%

ns_options = list([10 ** 2, 15 ** 2, 20 ** 2, 25 ** 2, 30 ** 2])

x = []

for ns in ns_options:
    ns_name = "simpleNetwork_1ns_%dNodes_100MB" % ns
    x.append({
        "nodes": ns,
        "AccNextNode": load_value(ns_name, "Alg004_2_true_(0.9_PT24H_true)", "NextNode")
    })

x_df = pd.DataFrame(x).set_index("nodes", drop=True)

# %%

# use as table
print(x_df.to_latex())