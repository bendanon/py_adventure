def singletone(_class: type) -> type:
    """
    Singletone decorator for a class.
    
    :param _class: class to decorate
    :type _class: type
    :return: singltone version of given class
    :rtype: type
    """

    class ClassWrapper(object):
        instance = None
        def __init__(self, *args, **kwargs):
            super().__init__()
            if ClassWrapper.instance is None:
                ClassWrapper.instance = _class(*args,**kwargs)

        def __getattribute__(self, attribute):
            return ClassWrapper.instance.__getattribute__(attribute)

        def __setattr__(self, attribute, value):
            return ClassWrapper.instance.__setattr__(attribute, value)
    
    return ClassWrapper

