def f_calc4(az, b_traverse):
        az = float(az)
        b_traverse = float(b_traverse)
        sum_angles = az + b_traverse
        if sum_angles < 200:
                az_next = sum_angles + 200
        elif 200 < sum_angles < 600:
                az_next = sum_angles - 200
        elif sum_angles > 600:
                  az_next = sum_angles - 600
        return az_next
azimuth = f_calc4 (115.1420, 165.3140)
print("Next Azimuth: ", format (azimuth, ".4f"))
