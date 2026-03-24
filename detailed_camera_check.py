import cv2
import sys
import os

def detailed_camera_check():
    """详细的摄像头诊断"""
    print("=" * 50)
    print("🔍 深度摄像头诊断")
    print("=" * 50)
    
    # 检查摄像头数量
    print("\n1. 检测可用摄像头设备:")
    for i in range(10):  # 检查前10个摄像头索引
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"   ✅ 摄像头 {i}: 可用")
            cap.release()
        else:
            print(f"   ❌ 摄像头 {i}: 不可用")
    
    # 尝试使用不同的后端
    print("\n2. 测试不同后端:")
    backends = [
        cv2.CAP_AVFOUNDATION,  # macOS原生
        cv2.CAP_ANY,
        cv2.CAP_FFMPEG
    ]
    
    for backend in backends:
        try:
            cap = cv2.VideoCapture(0, backend)
            if cap.isOpened():
                print(f"   ✅ 后端 {backend}: 成功")
                cap.release()
            else:
                print(f"   ❌ 后端 {backend}: 失败")
        except Exception as e:
            print(f"   ❌ 后端 {backend}: 错误 - {e}")
    
    print("\n3. 系统权限建议:")
    print("   💡 请检查系统设置 → 隐私与安全性 → 摄像头")
    print("   💡 确保终端或Python有摄像头访问权限")
    print("   💡 如果使用IDE，也需要授权IDE访问摄像头")
    
    print("\n4. 替代解决方案:")
    print("   💡 尝试使用USB外接摄像头")
    print("   💡 检查是否有其他应用占用摄像头")
    print("   💡 重启电脑后重试")

if __name__ == "__main__":
    detailed_camera_check()