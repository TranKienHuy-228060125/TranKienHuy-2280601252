import sys
from PIL import Image

def decode_image(encoded_image_path):
    try:
        img = Image.open(encoded_image_path)
    except Exception as e:
        print(f"Error: Cannot open image file '{encoded_image_path}'.\nDetails: {e}")
        return None  # Trả về None nếu có lỗi

    width, height = img.size
    binary_message = ""

    # Duyệt từng pixel và lấy bit ẩn
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):  
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển đổi từ binary sang text
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':  # Ký tự kết thúc chuỗi
            break
        message += char

    if message == "":
        print("Warning: No hidden message found in the image!")
        return None

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)

    if decoded_message:
        print("\nDecoded message:", decoded_message)

if __name__ == "__main__":
    main()
