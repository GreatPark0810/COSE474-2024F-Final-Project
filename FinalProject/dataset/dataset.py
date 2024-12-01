import objaverse
import random


uids = objaverse.load_uids() # each object has a unique ID (uid), then load it
print("objects length :", len(uids))

random.seed(42)
lvis_annotations = objaverse.load_lvis_annotations()

count = 1
for key, value in lvis_annotations.items():
    print(f"Downloading {key}... ({count} / {len(lvis_annotations.keys())})")
    if len(value) < 10:
        sampled_uids = random.sample(uids, len(value))
    else:
        sampled_uids = random.sample(uids, 10)

    objaverse.load_objects(sampled_uids, 1)
    print(f"Downloading {key} done.\n")
    count += 1

print("All downloading are done.")