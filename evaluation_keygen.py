import subprocess
import time
import os
import psutil

message = "Messageis32byteforAES25612345678"
def run_ntru_operations(security_levels):
    # 현재 프로세스 ID를 기반으로 psutil Process 객체 생성
    process = psutil.Process(os.getpid())

    for level in security_levels:
        # 키 생성 성능 측정 시작
        start_time = time.time()
        process = psutil.Process(os.getpid())
        start_cpu = process.cpu_percent(interval=None)
        start_memory = process.memory_info().rss

        # 키 생성
        key_gen_cmd = f"python3 NTRU.py -G -{level} -k NTRU_key_level{level}"
        subprocess.run(key_gen_cmd, shell=True)

        # 키 생성 성능 측정 종료
        end_time = time.time()
        key_gen_time_usage = end_time - start_time

        print(f"LEVEL: {level} => Key Generation time: {key_gen_time_usage:.4f} seconds")


security_levels = [80, 112, 128, 160, 192, 256]
run_ntru_operations(security_levels)
