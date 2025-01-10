def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
    else:
        attributes.append(attr)

    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    return info


number_info = introspection_info(42)
print(number_info)

number_info2 = introspection_info('World')
print(number_info2)
