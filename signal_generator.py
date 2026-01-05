import numpy as np
import matplotlib.pyplot as plt

class UnderwaterSignalGenerator:
    """Generates synthetic underwater acoustic signals"""
    
    def __init__(self, sample_rate=44100, duration=1.0):
        self.sample_rate = sample_rate
        self.duration = duration
        self.time = np.linspace(0, duration, int(sample_rate * duration))
    
    def generate_tonal(self, frequency=1000, noise_level=0.1):
        """Generates a tonal signal (like machinery or marine mammal)"""
        signal = np.sin(2 * np.pi * frequency * self.time)
        noise = noise_level * np.random.randn(len(self.time))
        return signal + noise
    
    def generate_broadband(self, low_freq=100, high_freq=5000, noise_level=0.3):
        """Generates broadband noise (like waves or rain)"""
        signal = np.random.randn(len(self.time))
        # Apply frequency bounds
        freqs = np.fft.fftfreq(len(signal), 1/self.sample_rate)
        fft_signal = np.fft.fft(signal)
        fft_signal[(np.abs(freqs) < low_freq) | (np.abs(freqs) > high_freq)] = 0
        signal = np.fft.ifft(fft_signal).real
        return signal * noise_level
    
    def generate_impulse(self, position=0.5, width=0.01):
        """Generates an impulse (like snapping shrimp or sonar ping)"""
        signal = np.zeros_like(self.time)
        center_idx = int(position * len(self.time))
        width_idx = int(width * len(self.time))
        signal[center_idx-width_idx:center_idx+width_idx] = 1.0
        return signal

# Example usage
if __name__ == "__main__":
    generator = UnderwaterSignalGenerator()
    tonal = generator.generate_tonal(frequency=1500)  # Submarine tonal
    broadband = generator.generate_broadband()  # Ocean noise
    impulse = generator.generate_impulse()  # Sonar ping
    
    print(f"Generated {len(tonal)} samples")
    print(f"Signal types: Tonal (machinery), Broadband (ambient), Impulse (transient)")
