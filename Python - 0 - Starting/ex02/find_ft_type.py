def all_thing_is_obj(object: any) -> int:
		if type(object) == list:
			print(f"List : {type(object)}")
		elif type(object) is tuple:
			print(f"Tuple : {type(object)}")
		elif type(object) is set:
			print(f"Set : {type(object)}")
		elif type(object) is dict:
			print(f"Dict : {type(object)}")
		elif type(object) is str:
			print(f"{object} is in the kitchen : {type(object)}")
		else:
			print(f"Type not found")
		return 42
		