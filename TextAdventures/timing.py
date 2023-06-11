from time import perf_counter


def timeEvent(event: callable, *params) -> tuple[float, any]:
	startTime = perf_counter()
	output = event(*params)
	time = perf_counter() - startTime
	return time, output
