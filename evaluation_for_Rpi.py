import subprocess
import time
import os
import psutil

message = "Messageis32byteforAES25612345678"
def run_ntru_operations(security_levels, iterations=1):
    # 현재 프로세스 ID를 기반으로 psutil Process 객체 생성
    process = psutil.Process(os.getpid())
    for level in security_levels:
        time.sleep(5)

        # 복호화 성능 측정 시작
        start_time = time.time()
        process = psutil.Process(os.getpid())
        start_cpu = process.cpu_percent(interval=None)

        # 복호화
        decrypt_cmd = f"python3 NTRU.py -k NTRU_key_level{level} -dF enc_level{level}.dat -O decoded_level{level}.dat"
        subprocess.run(decrypt_cmd, shell=True)

        # 복호화 성능 측정 종료
        end_time = time.time()
        dec_cpu_usage = process.cpu_percent(interval=None) - start_cpu
        #dec_cpu_usage = process.cpu_percent(interval=None)
        dec_time_usage = end_time - start_time

        # 복호화된 메시지 확인
        with open(f"decoded_level{level}.dat", "r") as f:
            decrypted_message = f.read()

        if decrypted_message == message:
            print(f"Decryption successful at security level {level}.")
            print(f"LEVEL: {level} => CPU usage for Decryption: {dec_cpu_usage}%, Time for Decryption: {dec_time_usage} seconds")
        else:
            print(f"Decryption failed at security level {level}.")


security_levels = [80, 112, 128, 160, 192, 256]
run_ntru_operations(security_levels)
