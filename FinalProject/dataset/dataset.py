import objaverse
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

uids = objaverse.load_uids() # each object has a unique ID (uid), then load it
print("all of objects length :", len(uids))

random.seed(42)
lvis_annotations = objaverse.load_lvis_annotations()

num_of_objects = 50
filtered_lvis_annotations = {key: value for key, value in lvis_annotations.items() if len(value) >= num_of_objects}
print(f"the number of classes having items more than {num_of_objects} : {len(filtered_lvis_annotations)}")

count = 1
for key, value in filtered_lvis_annotations.items():
    sampled_uids = random.sample(value, num_of_objects)
    print(f"Downloading {key}... ({count} / {len(filtered_lvis_annotations)})")
    objaverse.load_objects(sampled_uids, 1)
    print(f"Downloading {key} done.\n")
    count += 1

print("All downloading are done.")