import numpy as np
import cv2
from htpa import *

i = 0
dev = HTPA(0x1A)

while(True):
	print("Ambil gambar " + str(i))
	if (i == 5):
		dev.measure_observed_offset()

	(pixel_values, ptats) = dev.capture_image()
	im = dev.temperature_compensation(pixel_values, ptats)
	im = dev.offset_compensation(im)
	im = dev.sensitivity_compensation(im)

	# ubah ukuran dan skala gambar agar terlihat di layar raspberry pi
	im = cv2.resize(im, None, fx=12, fy=12)	
	im -= np.min(im)
	im /= np.max(im)

	cv2.imshow('frame', im)
	i += 1

	if cv2.waitKey(1) & 0xFF == ord('k'):
		break
#keluar dari eksekusi program
dev.close()

#mengentikan aplikasi yang jalan
cv2.destroyAllWindows()
