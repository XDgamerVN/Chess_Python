from constants import white_locations, black_locations


def check_knight(position, color):
    """
    Kiểm tra các nước đi hợp lệ của quân Mã dựa trên vị trí hiện tại và màu sắc.

    Args:
        position (tuple): Tọa độ hiện tại của quân Mã (x, y).
        color (str): Màu sắc của quân Mã ('white' hoặc 'black').

    Returns:
        list: Danh sách các nước đi hợp lệ cho quân Mã.
    """
    moves_list = []
    # Xác định danh sách đối thủ và đồng minh dựa trên màu sắc của quân cờ
    enemies_list = black_locations if color == 'white' else white_locations
    friends_list = white_locations if color == 'white' else black_locations

    # Các nước đi có thể của quân Mã: đi hai ô theo một hướng và một ô theo hướng khác
    knight_moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    for dx, dy in knight_moves:
        target = (position[0] + dx, position[1] + dy)

        # Kiểm tra xem nước đi có nằm trong bàn cờ và không bị cản bởi quân đồng minh
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)

    return moves_list
