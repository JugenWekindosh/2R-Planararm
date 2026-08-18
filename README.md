This project is the implementation of a 2-DOF planar revolute manipulator to demonstrate how it works. Kinematic calculation is done in a C source file for faster execution, while visualization and animation is done in a Python source file using Matplotlib.

## Repository Structure
* **`kinematics.c`**: Core C module computing kinematic data and outputting text files.
* **`plot_robot.py`**: Python script reading generated data to display animations and static singularity plots.
* **`traj_data.txt`**: Generated motion trajectory dataset.
* **`sing_max.txt`**: Workspace boundary configuration data ($\theta_2 = 0$).
* **`sing_min.txt`**: Internal boundary configuration data ($\theta_2 = \pi$).

## Mathematical Formulation
The direct kinematics equations used to compute joint positions $A = (x_a, y_a)$ and end-effector position $P = (x_p, y_p)$ are:

$$
\begin{aligned}
x_a &= L_1 \cos(\theta_1) \\
y_a &= L_1 \sin(\theta_1) \\
x_p &= x_a + L_2 \cos(\theta_1 + \theta_2) \\
y_p &= y_a + L_2 \sin(\theta_1 + \theta_2)
\end{aligned}
$$

## Build and Run Instructions
### Prerequisites
* **C Compiler**: `gcc` or `clang` with standard math library support (`libm`).
* **Python 3.x** with required packages:
  ```bash
  pip install numpy matplotlib

To compile `kinematics.c` you can use the `Makefile` provided in the repo. It's reccomended to create a virtual environment where to install the required Python packages.

