from constants import black_locations, white_locations

def check_bishop(position, color):
    """
    Kiểm tra các nước đi hợp lệ của quân Tượng dựa trên vị trí hiện tại và màu sắc.

    Args:
        position (tuple): Tọa độ hiện tại của quân Tượng (x, y).
        color (str): Màu sắc của quân Tượng ('white' hoặc 'black').

    Returns:
        list: Danh sách các nước đi hợp lệ cho quân Tượng.
    """
    moves_list = []
    # Xác định danh sách đối thủ và đồng minh dựa trên màu sắc của quân cờ
    enemies_list = black_locations if color == 'white' else white_locations
    friends_list = white_locations if color == 'white' else black_locations
    
    # Các hướng đi của quân Tượng: lên phải, lên trái, xuống phải, xuống trái
    directions = [(1, -1), (-1, -1), (1, 1), (-1, 1)]
    
    for x, y in directions:
        path = True
        chain = 1
        while path:
            next_position = (position[0] + chain * x, position[1] + chain * y)
            
            # Kiểm tra xem nước đi có nằm trong bàn cờ và không bị cản bởi quân đồng minh
            if next_position not in friends_list and 0 <= next_position[0] <= 7 and 0 <= next_position[1] <= 7:
                moves_list.append(next_position)
                
                # Nếu nước đi là vị trí của đối thủ, dừng lại tại đây
                if next_position in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
                
    return moves_list
