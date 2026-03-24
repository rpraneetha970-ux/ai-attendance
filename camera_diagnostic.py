import cv2
import sys

def test_camera():
    """测试摄像头功能和图像质量"""
    print("🔍 开始摄像头诊断测试...")
    
    # 尝试打开摄像头
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ 错误: 无法打开摄像头")
        print("可能的原因:")
        print("1. 摄像头被其他应用程序占用")
        print("2. 驱动程序问题")
        print("3. 硬件连接问题")
        return False
    
    print("✅ 摄像头成功打开")
    
    # 获取摄像头参数
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    print(f"📊 摄像头参数: {int(width)}x{int(height)}, {fps:.1f} FPS")
    
    # 测试捕获几帧图像
    print("📸 测试图像捕获...")
    success_count = 0
    
    for i in range(30):  # 尝试30帧
        ret, frame = cap.read()
        if ret:
            success_count += 1
            if i == 0:  # 保存第一帧用于分析
                cv2.imwrite('camera_test_frame.jpg', frame)
                print("✅ 成功捕获测试图像: camera_test_frame.jpg")
    
    cap.release()
    
    success_rate = (success_count / 30) * 100
    print(f"📈 捕获成功率: {success_rate:.1f}%")
    
    if success_rate > 90:
        print("✅ 摄像头功能正常")
        return True
    else:
        print("❌ 摄像头捕获不稳定")
        return False

if __name__ == "__main__":
    test_camera()