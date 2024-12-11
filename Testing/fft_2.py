import numpy as np
import matplotlib.pyplot as plt

# Tạo tín hiệu sóng sin 5 Hz
fs = 1000  # Tần số lấy mẫu 1000 Hz
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t)

# Thực hiện FFT với các tùy chọn norm khác nhau
fft_result_default = np.fft.fft(signal) # Không cung cấp n 
fft_result_shorter = np.fft.fft(signal, n=500) # n nhỏ hơn độ dài đầu vào 
fft_result_longer = np.fft.fft(signal, n=2000)
fft_frequency = np.fft.fftfreq(len(signal), d=1/fs)
fft_frequency_2 = np.fft.fftfreq(500, d=1/fs)
fft_frequency_3 = np.fft.fftfreq(2000, d=1/fs)


plt.subplot(3, 1, 1)
plt.plot(fft_frequency, np.abs(fft_result_default))

plt.subplot(3, 1, 2)
plt.plot(fft_frequency_2, np.abs(fft_result_shorter))

plt.subplot(3, 1, 3)
plt.plot(fft_frequency_3, np.abs(fft_result_longer))

plt.show()

# Hiển thị kết quả
# print("FFT Result (backward):", fft_result_backward)
# print("FFT Result (ortho):", fft_result_ortho)
# print("FFT Result (forward):", fft_result_forward)
