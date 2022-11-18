# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    # create 3d axes
    fig = plt.figure(figsize=(15, 15))
    #ax = plt.axes(projection='3d')

    popt3_calc = [(0.003276728) * 1.8684 / 100, (-0.008181688) * 1.8684 / 100, 0.004813692 * 3.4909 / 100,
                  (-3.33334E-05) * 3.4909 / 100]
    # popt3_calc = [110*0.25/1391684.0, 112*0.25/854199.0, 112*0.25/973357.0, 112*0.25/586476.0]

    K_ES_APP = 100.0 * 60.0 * 60.0 / (100000.0 / 1.75)
    K_ES_2_APP = 100.0 * 60.0 * 60.0 / (10000000.0 * 2.56)
    K_ES_APP_2 = 100.0 * 60.0 * 60.0 / (10000000.0)
    K_ES_2_APP_2 = 100.0 * 60.0 * 60.0 / (100000000.0 * 45.5)
    k_mic = [K_ES_APP, K_ES_2_APP, K_ES_APP_2, K_ES_2_APP_2]

    # function for Z values
    def fun_consum(n, app):
        return popt3_calc[0] * k_mic[0] * n * app + popt3_calc[1] * k_mic[1] * n * n * app + popt3_calc[2] * k_mic[
            2] * n * app * app + popt3_calc[3] * k_mic[3] * n * n * app * app

    # x and y values
    n = np.linspace(110, 400, 50)
    app = np.linspace(20, 200, 50)

    X, Y = np.meshgrid(n, app)
    Z = fun_consum(X, Y)

    #ax = plt.axes(projection='3d')
    ax = fig.add_subplot(projection='3d')

    # ax.plot_wireframe(X, Y, Z, color ='red')
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
    #                 cmap='viridis')
    ax.plot_surface(X, Y, Z, cmap='viridis',
                    linewidth=0, antialiased=False)

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
