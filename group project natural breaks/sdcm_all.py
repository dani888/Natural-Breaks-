def sdcm_all(numbers):
	sdcms = [sdam(numbers[:i]) + sdam(numbers[i:]) for i, e in enumerate(numbers)]
	index = sdcms.index(min(sdcms))
	return [numbers[:index],numbers[index:]]