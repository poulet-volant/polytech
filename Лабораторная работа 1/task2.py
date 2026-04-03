FLOPPYDISK = 1.44 # Mbytes
booksize_B = 4 * 25 * 50 * 100 # bytes
booksize_mb = booksize_B / 1024**2 # Mbytes
fitting = int(FLOPPYDISK / booksize_mb)

print("Количество книг, помещающихся на дискету:", fitting)
