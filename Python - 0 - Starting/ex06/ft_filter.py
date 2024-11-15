def ft_filter(function, iterable):
    if function is None:
        function = bool
    for item in iterable:
        if function(item):
            yield item
