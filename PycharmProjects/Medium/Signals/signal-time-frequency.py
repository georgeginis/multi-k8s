########################################################################################################################
#
# Python code for demonstrating signal representation in the time-domain and in the frequency-domain
# Uses the numpy and matplotlib libraries to achieve functionality similar to MATLAB
#
########################################################################################################################

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')


########################################################################################################################
# Figure 1
# Example of a continuous-time signal
# Pulse starting at time zero with duration of T_p
# Figure displays the function in the time interval between T_start and T_end
########################################################################################################################

T_p = 4         # pulse duration
T_start = -5    # start of time interval
T_end = 10      # end of time interval
T_s = 0.0001    # sampling period

# Generate the time samples as a numpy array
t = np.linspace(T_start, T_end, int((T_end-T_start)/T_s))

# Generate the function values as a numpy array
x_values = [1 if (0 <= t_value <= T_p) else 0 for t_value in t]
x = np.array(x_values)
x = x / np.sqrt(T_p)

# Produce the plot
plt.figure(1)
plt.plot(t, x)
plt.xlim(T_start, T_end)
plt.ylim(-0.5, 1)
plt.title("Continuous-time Pulse Signal")
plt.xlabel("t")
plt.ylabel("x(t)")

########################################################################################################################
# Figure 2
# Example of a discrete-time signal
# Pulse starting at time zero with duration of T_p
# Figure displays the function in the time interval between T_start and T_end
########################################################################################################################

T_p = 4         # pulse duration
T_start = -5    # start of time interval
T_end = 10      # end of time interval
T_s = 0.5       # sampling period

# Generate the time samples as a numpy array
t = np.arange(int((T_end-T_start)/T_s))
t = t * T_s + T_start

# Generate the function values as a numpy array
x_values = [1 if (0 <= t_value <= T_p) else 0 for t_value in t]
x = np.array(x_values)
x = x / np.sqrt(T_p)

# Produce the plot
plt.figure(2)
plt.stem(t, x)
plt.xlim(T_start, T_end)
plt.ylim(-0.5, 1)
plt.title("Discrete-time Pulse Signal")
plt.xlabel("t")
plt.ylabel("x(t)")

#######################################################################################################################
# Figure 3
# Example of a fourier transform of a continuous-time signal
# Pulse starting at time zero with duration of T_p
# Figure displays the function in the frequency interval between f_start and f_end
########################################################################################################################

T_p = 4         # pulse duration
f_start = -5    # start of frequency interval
f_end = 5       # end of frequency interval
f_s = 0.0001    # sampling period in the frequency domain

# Generate the frequency samples as a numpy array
f = np.arange(int((f_end-f_start)/f_s))
f = f * f_s + f_start

# Generate the function values as a numpy array
X_values = [np.sqrt(T_p) * np.exp(-1j * np.pi * f_value * T_p) * np.sinc(f_value * T_p) for f_value in f]
X = np.array(X_values)

# Produce the plot
plt.figure(3)
plt.subplot(2, 1, 1)
plt.plot(f, np.absolute(X))
#plt.plot(f, np.angle(X), '--')
plt.xlim(f_start, f_end)
plt.ylim(-1, 3)
plt.title("Fourier Transform of Continuous-Time Pulse Signal")
plt.xlabel("f")
plt.ylabel("Magnitude of X(f)")
plt.subplot(2, 1, 2)
plt.plot(f, np.angle(X))
#plt.plot(f, np.angle(X), '--')
plt.xlim(f_start, f_end)
plt.ylim(-4, 4)
plt.xlabel("f")
plt.ylabel("Phase of X(f)")

#######################################################################################################################
# Figure 4
# Example of a fourier transform of a discrete-time signal
# Pulse starting at time zero with duration of T_p and sample period T_s
# Figure displays the function in the frequency interval between f_start and f_end
########################################################################################################################

T_p = 4         # pulse duration
T_s = 0.5       # sampling period
f_start = -5    # start of frequency interval
f_end = 5       # end of frequency interval
f_s = 0.0001    # sampling period in the frequency domain

# Generate the frequency samples as a numpy array
f = np.arange(int((f_end-f_start)/f_s))
f = f * f_s + f_start

# Fourier Transform of continuous-time signal
# Generate the function values as a numpy array
X_values = [np.sqrt(T_p) * np.exp(-1j * np.pi * f_value * T_p) * np.sinc(f_value * T_p) for f_value in f]
X = np.array(X_values)

# Fourier Transform of the derived discrete-time signal
# Create replicas of the fourier transform of the continuous-time signal

X_T = 1./T_s * X

Xshift_minus1 = 1./T_s * np.roll(X, int(1/T_s * 1./f_s))
Xshift_minus2 = 1./T_s * np.roll(X, 2 * int(1/T_s * 1./f_s))
Xshift_plus1 = 1./T_s * np.roll(X, -int(1/T_s * 1./f_s))
Xshift_plus2 = 1./T_s * np.roll(X, -2 * int(1/T_s * 1./f_s))
X_T = 1./T_s * X + Xshift_minus1 + Xshift_minus2 + Xshift_plus1 + Xshift_plus2

# Produce the plot
plt.figure(4)
plt.subplot(2, 1, 1)
plt.plot(f, np.absolute(X_T))
plt.xlim(f_start, f_end)
plt.ylim(-1, 5)
plt.title("Fourier Transform of Discrete-Time Pulse Signal")
plt.xlabel("f")
plt.ylabel("Magnitude of X_T(f)")
plt.subplot(2, 1, 2)
plt.plot(f, np.angle(X_T))
plt.xlim(f_start, f_end)
plt.ylim(-4, 4)
plt.xlabel("f")
plt.ylabel("Phase of X_T(f)")

#######################################################################################################################
# Figure 5
# Example of a discrete fourier transform
# Pulse starting at time zero with duration of T_p and sample period T_s
# Figure displays the function in the frequency interval between f_start and f_end
########################################################################################################################

T_p = 4         # pulse duration
T_s = 0.5       # sampling period
T_start = -5    # start of time interval
T_end = 10      # end of time interval
T_s = 0.5       # sampling period
f_start = -1.5    # start of frequency interval
f_end = 1.5       # end of frequency interval
f_s = 0.0001    # sampling period in the frequency domain

# Generate the time samples as a numpy array
t = np.arange(int((T_end-T_start)/T_s))
t = t * T_s + T_start

# Generate the function values as a numpy array
x_values = [1 if (0 <= t_value <= T_p) else 0 for t_value in t]
x = np.array(x_values)
x = x / np.sqrt(T_p)

X = np.fft.fft(x, np.size(x))
f = np.fft.fftfreq(np.size(x), T_s)

# Produce the plot
plt.figure(5)
plt.subplot(2, 1, 1)
plt.stem(f, np.real(X))
plt.xlim(f_start, f_end)
plt.ylim(-5, 5)
plt.title("Discrete Fourier Transform of Pulse Signal")
plt.xlabel("f")
plt.ylabel("Real part of X[k]")
plt.subplot(2, 1, 2)
plt.stem(f, np.imag(X))
plt.xlim(f_start, f_end)
plt.ylim(-5, 5)
plt.xlabel("f")
plt.ylabel("Imaginary part of X[k]")
plt.show()

