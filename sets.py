new_set = set(("poland", "netherlands", "wroclaw", "warsaw", "monaco", "monaco"))
new_set.add("luxoft")
new_set.update(["Google", "Microsoft", "amazon"])
print(new_set)
new_set.remove("monaco")
print(new_set)

non_tuple = set(("tuple", "amazon"))
tuple = set(("tuple", "netflix"))
print(f"{non_tuple  - tuple}")