import pandas.rpy.common as com

def loadSAV(filename):
    w = com.robj.r('foreign::read.spss("%s", to.data.frame=TRUE)' % filename)
    w = com.convert_robj(w)
    print w
    return w


