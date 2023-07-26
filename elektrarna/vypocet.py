import math

def turbine_calculations(H1=2.0, Q=2.0, L_D=1.5, k_ostr=0.2, tl=2.0, vstupni_uhel_vody=15, vstupni_uhel_lopatky=30, vystupni_uhel_lopatky=90, pocet_lopatek=32, ucinnost=78):
    ucinnost = ucinnost / 100  # convert efficiency to decimal
    g = 9.81  # gravitational constant m/s²

    # Calculations
    c1 = 0.98 * math.sqrt(19.81 * H1)  # water inlet speed in m/sec
    a = Q / (1000 * c1)  # slot area in m2
    vykon = round(g * H1 * Q * ucinnost, 3)  # power in W

    # Calculation of s before D as it is used in the calculation of D
    s = 1000 * math.sqrt((a * k_ostr) / L_D)  # slot opening in mm

    D = 0.5 * round(s / k_ostr * 2, 0)  # diameter of the runner in mm

    n = 9898 * c1 / D  # nominal speed of the turbine in rev/min
    prubezne_otacky = 1.8 * n  # continuous speed in rev/min
    d2 = 0.66 * D  # inner diameter in mm
    L = 0.5 * round(2 * D * L_D, 0)  # length of the slot in mm
    delka_lopatky = L + 10  # length of the blade in mm
    #DN = 0.326 * D - tl  # pipe for blade production in mm
    DN = (D**2 - d2**2)/(math.sqrt(3)*D)
    dh = round((160 * ((H1 * Q / (75 * n))**(1/3))) * 5, -1) / 5  # approximate shaft diameter in mm

    # Results
    results = [
        'Water inlet speed (c1) [m/sec]: ' + str(round(c1, 3)),
        'Slot area (a) [m2]: ' + str(round(a, 6)),
        'Power (vykon) [W]: ' + str(round(vykon, 3)),
        'Nominal speed 👎 [rev/min]: ' + str(round(n, 0)),
        'Continuous speed [rev/min]: ' + str(round(prubezne_otacky, 0)),
        'Runner diameter (D) [mm]: ' + str(round(D, 3)),
        'Inner diameter (d2) [mm]: ' + str(round(d2, 3)),
        'Slot length (L) [mm]: ' + str(round(L, 3)),
        'Blade length [mm]: ' + str(round(delka_lopatky, 3)),
        'Slot opening (s) [mm]: ' + str(round(s, 3)),
        'Pipe for blade production (DN) [mm]: ' + str(round(DN, 3)),
        'Approximate shaft diameter (dh) [mm]: ' + str(round(dh, 3))
    ]

    # Return all the variables
    return (c1, a, vykon, n, prubezne_otacky, D, d2, L, delka_lopatky, s, DN, dh, results)