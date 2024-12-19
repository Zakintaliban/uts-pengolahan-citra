"""
Module untuk memproses citra dengan kontras rendah.
Fitur: Histogram Equalization dan Penyesuaian Kontras.
"""

import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

# Membaca citra input dengan kontras rendah
IMAGE_PATH = "Wack.jpg"  # Ganti dengan path ke citra Anda
low_contrast_image = imageio.imread(IMAGE_PATH, mode="L")

# Normalisasi ke rentang [0, 255] jika belum dalam rentang tersebut
low_contrast_image = (low_contrast_image - low_contrast_image.min()) / (
    low_contrast_image.max() - low_contrast_image.min()
)
low_contrast_image = (low_contrast_image * 255).astype(np.uint8)


def histogram_equalization(img):
    """
    Melakukan histogram equalization pada citra untuk meningkatkan kontras.

    Parameters:
        img (numpy.ndarray): Citra input dalam format array 2D.

    Returns:
        numpy.ndarray: Citra setelah histogram equalization.
    """
    histogram, _ = np.histogram(img.flatten(), 256, [0, 256])
    cdf = histogram.cumsum()  # Cumulative Distribution Function
    cdf_masked = np.ma.masked_equal(cdf, 0)  # Masking nilai nol
    cdf_masked = (
        (cdf_masked - cdf_masked.min()) * 255 / (cdf_masked.max() - cdf_masked.min())
    )
    cdf = np.ma.filled(cdf_masked, 0).astype("uint8")
    equalized_img = cdf[img]
    return equalized_img


def contrast_adjustment(img, level=1.2):
    """
    Menyesuaikan kontras citra berdasarkan level tertentu.

    Parameters:
        img (numpy.ndarray): Citra input dalam format array 2D.
        level (float): Tingkat penyesuaian kontras. Default 1.2.

    Returns:
        numpy.ndarray: Citra setelah penyesuaian kontras.
    """
    img_normalized = img / 255.0  # Normalisasi ke rentang [0, 1]
    adjusted_img = np.clip(128 + level * (img_normalized * 255 - 128), 0, 255)
    return adjusted_img.astype(np.uint8)


equalized_image = histogram_equalization(low_contrast_image)
contrast_adjusted_image = contrast_adjustment(low_contrast_image, level=1.5)

# Koreksi inversi jika terjadi
if contrast_adjusted_image.mean() < low_contrast_image.mean():
    contrast_adjusted_image = 255 - contrast_adjusted_image

# Plot histogram untuk verifikasi
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.hist(low_contrast_image.flatten(), bins=256, range=[0, 256], color="gray")
plt.title("Histogram Citra Asli")

plt.subplot(1, 3, 2)
plt.hist(equalized_image.flatten(), bins=256, range=[0, 256], color="gray")
plt.title("Histogram Setelah HE")

plt.subplot(1, 3, 3)
plt.hist(contrast_adjusted_image.flatten(), bins=256, range=[0, 256], color="gray")
plt.title("Histogram Setelah Kontras Level 1.5")

plt.tight_layout()  # Untuk menghindari overlap antar subplot
plt.show()

# Visualisasi hasil
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(low_contrast_image, cmap="gray", vmin=0, vmax=255)
axs[0].set_title("Citra Asli")
axs[0].axis("off")

axs[1].imshow(equalized_image, cmap="gray", vmin=0, vmax=255)
axs[1].set_title("Histogram Equalization")
axs[1].axis("off")

axs[2].imshow(contrast_adjusted_image, cmap="gray", vmin=0, vmax=255)
axs[2].set_title("Peningkatan Kontras Level 1.5")
axs[2].axis("off")

plt.tight_layout()
plt.show()
