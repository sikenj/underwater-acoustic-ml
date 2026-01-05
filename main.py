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
    
    # Create signal generator
    print("\nCreating signal generator...")
    generator = UnderwaterSignalGenerator(sample_rate=44100, duration=1.0)
    
    # Generate naval-relevant signals
    print("\nGenerating signals for analysis:")
    tonal = generator.generate_tonal(frequency=127)  # Submarine frequency
    broadband = generator.generate_broadband()       # Ocean noise
    impulse = generator.generate_impulse()           # Sonar ping
    
    print(f"✓ 127 Hz tonal (submarine machinery)")
    print(f"✓ Broadband (ocean ambient noise)")
    print(f"✓ Impulse (sonar ping)")
    
    # Create visualization
    print("\nCreating visualization...")
    
    fig, axes = plt.subplots(3, 1, figsize=(10, 8))
    
    # Plot first 0.05 seconds
    samples_to_plot = 2205  # 0.05 seconds at 44.1 kHz
    
    axes[0].plot(generator.time[:samples_to_plot], tonal[:samples_to_plot], 'b')
    axes[0].set_title('Tonal: 127 Hz (Submarine Machinery)', fontweight='bold')
    axes[0].set_ylabel('Amplitude')
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(generator.time[:samples_to_plot], broadband[:samples_to_plot], 'g')
    axes[1].set_title('Broadband: Ocean Ambient Noise', fontweight='bold')
    axes[1].set_ylabel('Amplitude')
    axes[1].grid(True, alpha=0.3)
    
    axes[2].plot(generator.time[:samples_to_plot], impulse[:samples_to_plot], 'r')
    axes[2].set_title('Impulse: Sonar Ping', fontweight='bold')
    axes[2].set_xlabel('Time (seconds)')
    axes[2].set_ylabel('Amplitude')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('acoustic_analysis.png', dpi=150, bbox_inches='tight')
    print("\n✓ Saved: 'acoustic_analysis.png'")
    
    print("\n" + "=" * 50)
    print("PROJECT COMPLETE!")
    print("This demonstrates signal processing for:")
    print("- Naval sonar applications (ASW)")
    print("- Acoustic data analysis")
    print("- Machine learning feature extraction")
    print("=" * 50)

if __name__ == "__main__":
    main()
