import argparse
from collections import defaultdict
import numpy as np
from ultralytics import YOLO
import random
import os
import math
import requests
import time
import cv2 # type: ignore

class FishTracking:
    def __init__(self, model_path, video_path, base_path, output_path):
        # Load the YOLOv8 model  '
        self.model = YOLO(model_path)
        self.video_path = video_path
        self.base_path = base_path
        self.output_path = output_path
        self.track_history = defaultdict(lambda: [])
        self.track_colors = {}

        # Initialize video capture and video writer
        self.cap = cv2.VideoCapture(self.video_path)
        frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(self.output_path, fourcc, fps, (frame_width, frame_height))

        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def generate_random_color(self):
        return [random.randint(0, 255) for _ in range(3)]

    def process_frame(self, frame):
        # Run YOLOv8 tracking
        results = self.model.track(frame, persist=True, tracker="botsort.yaml", save=True)

        # Get the tracking data
        track_ids = results[0].boxes.id.int().cpu().tolist()
        boxes = results[0].boxes.xywh.cpu()
        keypoints = results[0].keypoints.xy.cpu().numpy()

        # Process each track_id in the current frame
        for idx, (box, track_id) in enumerate(zip(boxes, track_ids)):
            x, y, w, h = box

            # Get or assign a random color to the track_id
            if track_id not in self.track_colors:
                self.track_colors[track_id] = self.generate_random_color()

            color = self.track_colors[track_id]

            # Calculate the center point of the bounding box (for drawing tail)
            center_x, center_y = int(x), int(y)

            # Draw the bounding box
            x1, y1, x2, y2 = int(x - w / 2), int(y - h / 2), int(x + w / 2), int(y + h / 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 1)

            # Draw the track ID near the bounding box
            cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 1)

            # Draw keypoints
            for point in keypoints[idx]:
                px, py = int(point[0]), int(point[1])
                cv2.circle(frame, (px, py), 1, color, 2)

            # Update track history (retain last 20 frames for the tail effect)
            self.track_history[track_id].append((center_x, center_y))
            if len(self.track_history[track_id]) > 20:
                self.track_history[track_id].pop(0)

            # Draw the tail (past trajectory) for each track_id
            for i in range(1, len(self.track_history[track_id])):
                cv2.line(frame, self.track_history[track_id][i - 1], self.track_history[track_id][i], color, 2)

        # Remove track history for IDs that are no longer in the current frame
        current_track_ids = set(track_ids)
        for old_id in list(self.track_history.keys()):
            if old_id not in current_track_ids:
                del self.track_history[old_id]  # Clear history for old IDs

        # Save track data to file for each track_id
        for track_id in track_ids:
            track = self.track_history[track_id]
            x, y, w, h = boxes[track_ids.index(track_id)]
            k1, k2, k3 = keypoints[track_ids.index(track_id)]
            file_path = os.path.join(self.base_path, f"{track_id}.txt")
            with open(file_path, 'a') as file:
                file.write(f'{track_id} {x} {y} {w} {h} {k1[0]} {k1[1]} {k2[0]} {k2[1]} {k3[0]} {k3[1]}\n')

        return frame

    def process_video(self):
        while self.cap.isOpened():
            success, frame = self.cap.read()

            if success:
                # Process each frame
                annotated_frame = self.process_frame(frame)

                # Write the annotated frame to the output video
                self.out.write(annotated_frame)

                # Display the annotated frame (optional)


                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break

        # Release resources
        self.cap.release()
        self.out.release()


def calculate_average(file_path):
    averages = []  # 用于存储每行的平均值
    try:
        with open(file_path, 'r') as file:
            for line in file:
                values = list(map(float, line.strip().split()))  # 将每行数据转换为浮点数列表
                avg = sum(values) / len(values)  # 计算每行的平均值
                averages.append(avg)  # 将平均值添加到列表中
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return averages

def process_position_files(position_path, final_path):
    if not os.path.exists(position_path):
        os.makedirs(position_path)
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    path_list = [os.path.join(position_path, "position{}".format(a)) for a in range(1, len(os.listdir(position_path)) + 1)]

    # Lists for storing intermediate results
    x, y, w, h, k1, k2, k3 = [], [], [], [], [], [], []
    distance_res = []
    angle = []
    f = []
    s = []
    v_res = []
    v = []
    a_res = []
    a = []

    num = 0
    for i in path_list:  # Loop through all position directories
        num += 1
        txt_id = len(os.listdir(i))
        for j in range(1, txt_id + 1):  # Loop through all text files for each fish
            txt_path = os.path.join(i, "{}.txt".format(j))
            try:
                with open(txt_path, 'r') as file1:
                    for line_num, line in enumerate(file1):
                        values = line.strip().split()
                        x.append(float(values[1]))
                        y.append(float(values[1]))
                        w.append(float(values[3]))
                        h.append(float(values[4]))
                        k1.append((float(values[5]), float(values[6])))
                        k2.append((float(values[7]), float(values[8])))
                        k3.append((float(values[9]), float(values[10])))

                    # Calculate xcenter and ycenter
                    xcenter = [a + b / 2 for a, b in zip(x, w)]
                    ycenter = [c + d / 2 for c, d in zip(y, h)]

                    # Calculate distance between consecutive points
                    for k in range(len(xcenter) - 1):
                        distance = math.sqrt((xcenter[k + 1] - xcenter[k]) ** 2 + (ycenter[k + 1] - ycenter[k]) ** 2)
                        distance_res.append(distance)

                    # Convert distance to real-world values
                    distance_res = [o * (5 / 24) for o in distance_res]

                    # Calculate velocity from distance
                    for m in distance_res:
                        v_res.append(30 * m)

                    # Calculate acceleration from velocity
                    for n in range(1, len(v_res)):
                        acceleration = abs(v_res[n] - v_res[n - 1]) * 30
                        a_res.append(acceleration)

                    # Calculate angle between vectors k1k2 and k3k2
                    for l in range(len(k1)):
                        x1, y1 = k1[l]
                        x2, y2 = k2[l]
                        x3, y3 = k3[l]

                        vector_k1k2 = (x1 - x2, y1 - y2)
                        vector_k3k2 = (x3 - x2, y3 - y2)

                        dot_product = vector_k1k2[0] * vector_k3k2[0] + vector_k1k2[1] * vector_k3k2[1]
                        magnitude_k1k2 = math.sqrt(vector_k1k2[0] ** 2 + vector_k1k2[1] ** 2)
                        magnitude_k3k2 = math.sqrt(vector_k3k2[0] ** 2 + vector_k3k2[1] ** 2)

                        cos_angle = dot_product / (magnitude_k1k2 * magnitude_k3k2)
                        cos_angle = max(-1, min(1, cos_angle))  # Avoid floating-point errors
                        angle_radians = math.acos(cos_angle)
                        angle_degrees = math.degrees(angle_radians)

                        angle.append(180 - angle_degrees)

                    # Count the tail-beat frequency
                    f_count = 0
                    for m in range(1, len(angle) - 1):
                        if angle[m] > angle[m - 1] and angle[m] > angle[m + 1] and angle[m] > 5:
                            f_count += 1
                    f_single = f_count

                    # Clear lists after processing
                    x.clear()
                    y.clear()
                    w.clear()
                    h.clear()
                    xcenter.clear()
                    ycenter.clear()
                    k1.clear()
                    k2.clear()
                    k3.clear()

                    # Calculate fish metrics
                    s_single = sum(distance_res)  # Individual displacement
                    v_single = sum(v_res) / (len(v_res) + 0.00000001)  # Average velocity
                    a_single = sum(a_res) / (len(a_res) + 0.00000001)  # Average acceleration

                    # Clear intermediate result lists
                    distance_res.clear()
                    v_res.clear()
                    a_res.clear()
                    angle.clear()

                    # Append individual metrics to global lists
                    f.append(f_single)
                    s.append(s_single)
                    v.append(v_single)
                    a.append(a_single)

                    # Round metrics to 4 decimal places
                    f = [round(f_single, 4) for f_single in f]
                    s = [round(s_single, 4) for s_single in s]
                    v = [round(v_single, 4) for v_single in v]
                    a = [round(a_single, 4) for a_single in a]

            except FileNotFoundError:
                print(f"File not found: {txt_path}, skipping...")
                continue  # Skip missing files and continue

        # Write the results to the output file
        output_txt = os.path.join(final_path, '{}.txt'.format(num))
        with open(output_txt, 'w') as file2:
            file2.write(' '.join(map(str, s)) + '\n')
            file2.write(' '.join(map(str, v)) + '\n')
            file2.write(' '.join(map(str, f)) + '\n')
            file2.write(' '.join(map(str, a)) + '\n')

        # Clear the global lists for the next video
        s.clear()
        v.clear()
        f.clear()
        a.clear()

def download_file(url, path, retries=3, backoff_factor=0.5):
    if os.path.exists(path):
        print("权重文件已在本地存在，无需下载。")
        return  # 如果文件存在则直接返回
    
    for attempt in range(retries):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # 如果响应状态码不是200，将引发HTTPError
            
            # 写入文件
            with open(path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"权重文件下载并保存成功！文件路径: {path}, 大小: {len(response.content)} 字节")
            return  # 成功后退出函数

        except requests.exceptions.RequestException as e:
            print(f"下载过程中出现错误: {str(e)}")
            if attempt < retries - 1:
                wait_time = backoff_factor * (2 ** attempt)  # 指数回退
                print(f"等待 {wait_time:.1f} 秒后重试...")
                time.sleep(wait_time)

    print("下载失败，请检查连接或文件URL。")

def track(video_path):
    parser = argparse.ArgumentParser(description="Fish Tracking using YOLOv8 and BotSort")
    parser.add_argument('--model_path', default='/home/zsl/Agent/Agent/best.pt', type=str, help='Path to the YOLOv8 model file')
    parser.add_argument('--video_path', default='/home/zsl/Agent/Agent/fish.mp4', type=str, help='Path to the input video file')
    parser.add_argument('--base_path', default='./track_data/position/position1', type=str, help='Directory path to save tracking data')
    parser.add_argument('--output_path', default='./track_data/track_video/result.mp4', type=str, help='Path to save the output video with tracking')
    parser.add_argument('--position_path', default='./track_data/position', type=str, help='Directory path to save position data')
    parser.add_argument('--final_path', default='./track_data/final', type=str, help='Path to save the behaviour information')
    parser.add_argument('--behaviour_path', default='./track_data/final/1.txt', type=str, help='Path to save the behaviour information')
    args = parser.parse_args()
    
    github_weight_url = "http://192.168.5.35:3000/chwang/mumu-fishllm/raw/branch/main/best.pt"  # Example
    print(args.model_path)
    download_file(github_weight_url, args.model_path)
    
    # 继续后续处理
    args.video_path = video_path
    tracker = FishTracking(args.model_path, args.video_path, args.base_path, args.output_path)
    tracker.process_video()
    process_position_files(position_path=args.position_path, final_path=args.final_path)
    result = calculate_average(file_path=args.behaviour_path)

    import subprocess
    folder_path1 = "/home/zsl/Agent/Agent/Tools/runs"  # 替换为你要删除的文件夹路径
    folder_path2 = "/home/zsl/Agent/Agent/Tools/track_data"  # 替换为你要删除的文件夹路径
    subprocess.run(f"rm -rf {folder_path1}", shell=True, check=True)
    subprocess.run(f"rm -rf {folder_path2}", shell=True, check=True)
    return result


if __name__ == "__main__":
    track()




