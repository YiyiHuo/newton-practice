def df(x0, f, step=1e-5):
    return (f(x0) - f(x0 - step)) / step


def ddf(x0, f, step=1e-5):
    return (df(x0, f) - df(x0 - step, f)) / step


def newton_method(x0, f, tol=1e-7, max_iter=10):
    x1 = x0 + 2 * tol
    i = 0
    while abs(x1 - x0) > tol and i < max_iter:
        i += 1
        df_x0 = df(x0, f)
        ddf_x0 = ddf(x0, f)
        if ddf_x0 == 0:
            return x0
        else:
            x1 = x0
            x0 = x0 - df_x0 / ddf_x0
            print(df_x0, ddf_x0)
            print("i = ", i, "; x0 = ", x0)
    return x0
