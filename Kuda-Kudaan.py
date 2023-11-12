def is_safe(board, row, col, k):
    # Fungsi ini memeriksa apakah tempat (row, col) aman untuk menempatkan kuda kedua.

    # Daftar kemungkinan langkah kuda dalam bentuk delta baris dan kolom
    delta_row = [2, 1, -1, -2, -2, -1, 1, 2]
    delta_col = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(8):
        new_row = row + delta_row[i]
        new_col = col + delta_col[i]

        # Memeriksa apakah langkah tersebut masih berada di papan catur
        if 1 <= new_row <= k and 1 <= new_col <= k:
            # Memeriksa apakah kotak tersebut sudah diisi
            if board[new_row][new_col] == 1:
                return False

    return True

def count_ways_to_place_knights(k):
    ways = 0
    for row in range(1, k + 1):
        for col in range(1, k + 1):
            # Jika tempat tersebut aman, coba tempatkan kuda kedua di sana
            if is_safe(board, row, col, k):
                board[row][col] = 1
                # Jika k = 1, ini adalah satu cara
                if k == 1:
                    ways += 1
                else:
                    # Jika k > 1, tambahkan cara-cara dari submasalah dengan ukuran k-1
                    ways += count_ways_to_place_knights(k - 1)
                # Kembalikan keadaan sebelumnya untuk mencoba langkah berikutnya
                board[row][col] = 0

    return ways

# Input
n = int(input())

# Mencetak output untuk setiap k dari k-1 hingga n
for k in range(n - 1, n + 1):
    # Inisialisasi papan catur
    board = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
    ways = count_ways_to_place_knights(k)
    print(ways)
