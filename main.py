"""
Underwater Acoustic Signal Analysis
Project by Jacob Siken - Former U.S. Navy Sonar Technician
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_generator import UnderwaterSignalGenerator

def main():
    print("=" * 50)
    print("UNDERWATER ACOUSTIC ANALYSIS")
    print("By: Jacob Siken - Former Navy Sonar Technician")
    print("=" * 50)
    
    # Create signal generator with longer duration for better visualization
    print("\nCreating signal generator...")
    generator = UnderwaterSignalGenerator(sample_rate=44100, duration=2.0)
    
    # Generate naval-relevant signals
    print("\nGenerating signals for analysis:")
    
    # 1. Tonal signal - 127 Hz is a common submarine frequency
    tonal = generator.generate_tonal(frequency=127, noise_level=0.05)
    print(f"✓ 127 Hz tonal (submarine machinery)")
    
    # 2. Broadband noise - typical ocean ambient
    broadband = generator.generate_broadband(low_freq=20, high_freq=1000, noise_level=0.2)
    print(f"✓ Broadband (ocean ambient noise, 20-1000 Hz)")
    
    # 3. Impulse - make it WIDER so we can see it
    impulse = generator.generate_impulse(position=0.5, width=0.02)  # 20ms wide now
    print(f"✓ Impulse (sonar ping, 20ms duration)")
    
    # Create visualization
    print("\nCreating visualization...")
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # PLOT 1: Tonal Signal (show first 0.1 seconds)
    time_ms_1 = generator.time[:4410] * 1000  # Convert to milliseconds
    axes[0].plot(time_ms_1, tonal[:4410], 'b', linewidth=1.5)
    axes[0].set_title('TONAL SIGNAL: 127 Hz (Submarine Machinery Frequency)', 
                      fontweight='bold', fontsize=12)
    axes[0].set_ylabel('Amplitude', fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim([0, 100])  # First 100ms
    
    # PLOT 2: Broadband Noise (show first 0.1 seconds)
    time_ms_2 = generator.time[:4410] * 1000
    axes[1].plot(time_ms_2, broadband[:4410], 'g', linewidth=1.5)
    axes[1].set_title('BROADBAND NOISE: Ocean Ambient (20-1000 Hz)', 
                      fontweight='bold', fontsize=12)
    axes[1].set_ylabel('Amplitude', fontweight='bold')
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xlim([0, 100])  # First 100ms
    
    # PLOT 3: Impulse Signal (ZOOM IN around the impulse)
    # Find the impulse location
    impulse_position = 0.5 * generator.duration  # Middle at 1 second
    samples_before_after = 500  # Show 500 samples before and after
    
    center_sample = int(impulse_position * generator.sample_rate)
    start_sample = max(0, center_sample - samples_before_after)
    end_sample = min(len(generator.time), center_sample + samples_before_after)
    
    time_ms_3 = generator.time[start_sample:end_sample] * 1000
    axes[2].plot(time_ms_3, impulse[start_sample:end_sample], 'r', linewidth=2)
    axes[2].set_title('IMPULSE SIGNAL: Sonar Ping (20ms duration) - ZOOMED VIEW', 
                      fontweight='bold', fontsize=12)
    axes[2].set_xlabel('Time (milliseconds)', fontweight='bold')
    axes[2].set_ylabel('Amplitude', fontweight='bold')
    axes[2].grid(True, alpha=0.3)
    
    # Add a red vertical line at the center of the impulse
    axes[2].axvline(x=impulse_position*1000, color='darkred', linestyle='--', 
                    alpha=0.7, label='Ping Center')
    axes[2].legend()
    
    plt.tight_layout()
    plt.savefig('acoustic_analysis.png', dpi=150, bbox_inches='tight')
    print("\n✓ Saved: 'acoustic_analysis.png'")
    
    # Print signal statistics
    print("\n" + "=" * 50)
    print("SIGNAL STATISTICS:")
    print(f"Tonal Signal:")
    print(f"  - Frequency: 127 Hz")
    print(f"  - Samples: {len(tonal)}")
    print(f"  - Duration: {generator.duration} seconds")
    
    print(f"\nBroadband Noise:")
    print(f"  - Frequency range: 20-1000 Hz")
    print(f"  - RMS amplitude: {np.sqrt(np.mean(broadband**2)):.4f}")
    
    print(f"\nImpulse (Sonar Ping):")
    print(f"  - Position: {impulse_position} seconds")
    print(f"  - Width: 0.02 seconds (20ms)")
    print(f"  - Max amplitude: {np.max(np.abs(impulse)):.4f}")
    
    print("\n" + "=" * 50)
    print("PROJECT COMPLETE!")
    print("This demonstrates signal processing for:")
    print("- Naval sonar applications (ASW)")
    print("- Acoustic data analysis")
    print("- Machine learning feature extraction")
    print("=" * 50)

if __name__ == "__main__":
    main()
