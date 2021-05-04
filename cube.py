def cube_volume(a):
    try:
        val = int(a)
        val = float(a)
        if(val < 0):
            val = -val
        return (val*val*val)      
    except ValueError:
        try:
            val = float(a)
            if(val < 0):
                val = -val
            return (val*val*val)
        except ValueError:
            return 0