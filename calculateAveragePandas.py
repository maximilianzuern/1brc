import pandas as pd


# Read data file
df = pd.read_csv(
    "measurements.txt",
    sep=";",
    header=None,
    names=["station_name", "measurement"],
    dtype={"station_name": "category", "measurement": "float16"},
    memory_map=True,
    engine="c",
)

# Group data
grouped = df.groupby("station_name", observed=False, sort=True)["measurement"].agg(
    ["min", "mean", "max"]
)

# Print final results
print("{", end="")
for data in grouped.iterrows():
    print(
        "{data[0]}={data[1][0]:.1f}/{data[1][1]:.1f}/{data[1][2]:.1f}",
        end=", ",
    )
print("\b\b} ")
