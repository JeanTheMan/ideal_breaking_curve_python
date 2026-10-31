import matplotlib.pyplot as plt
import numpy as np

# Constants
g = 9.81 # ms^-2
m = 280 # kg
h_cg = 0.25 # m
d_wheel = 1.590 # m
wd_front = 0.5 # weight distribiution on front axle
gravitational_force = m * g # saw this twice on formula so can't be having duplicate stuff
fig, ax = plt.subplots()


# inital graph setup
ax.set_title('Ideal Break Curve')
ax.set_xlabel('Front Break Force (N)')
ax.set_ylabel('Rear Break Force (N)')


# calculate front and rear for 200 coefficients between 0 and 1 to get smooth curve
friction_coefficients = np.linspace(0.0, 1.0, 200)
x = []
y = []

for fc in friction_coefficients:
    acceleration = fc * g
    longitudinal_weight_transfer = (m * acceleration * h_cg) / d_wheel

    front_force = fc * (gravitational_force * wd_front + longitudinal_weight_transfer)
    rear_force = fc * (gravitational_force * (1 - wd_front) - longitudinal_weight_transfer)

    x.append(front_force)
    y.append(rear_force)

max_x = max(x)
max_y = max(y)


# plot diagonal lines that rerpresent the coefficients and the lables
for line_number in np.arange(0.1, 1.1, 0.1):

    corresponding_x = line_number * max_x
    corresponding_y = line_number * max_y

    # diagonal line this will appear as the correct coordinate because the coeficient is basically a percentage of the max values kinda idk
    ax.plot([0, corresponding_x], [corresponding_y, 0], linestyle='--', color='gray', alpha=0.5)

    # add lable the .1f makes it so bc in python sometimes its like 3.00000000001 for no reason and it gets rid of it
    ax.text(corresponding_x, 0, f' μ={line_number:.1f}', verticalalignment='bottom', horizontalalignment='right', fontsize=8, color='gray')




# set grid properties that may depend on max vals
ax.set_xlim(0, max_x)
ax.set_ylim(0, max_y)
ax.set_aspect('equal', adjustable='box')
ax.grid()


plt.show()