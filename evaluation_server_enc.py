import subprocess
import time
import os
import psutil


def run_ntru_operations(security_levels, iterations=1):
    message = "Messageis32byteforAES25612345678"
    # 현재 프로세스 ID를 기반으로 psutil Process 객체 생성
    process = psutil.Process(os.getpid())
    for level in security_levels:
        # 키 생성 성능 측정 시작
        start_time = time.time()
        process = psutil.Process(os.getpid())
        start_cpu = process.cpu_percent(interval=None)
        #start_memory = process.memory_info().rss

        # 키 생성
        key_gen_cmd = f"python3 NTRU.py -G -{level} -k NTRU_key_level{level}"
        subprocess.run(key_gen_cmd, shell=True)

        # 키 생성 성능 측정 종료
        #end_memory = process.memory_info().rss
        end_time = time.time()
        #key_gen_cpu_usage = process.cpu_percent(interval=None) - start_cpu
        key_gen_cpu_usage = process.cpu_percent(interval=None)
        #key_gen_memory_usage = end_memory - start_memory
        key_gen_time_usage = end_time - start_time

        # 메시지 파일 작성
        with open("message.txt", "w") as f:
            f.write(message)

        # 암호화 및 복호화 실행 전 CPU 사용률 초기화
        process.cpu_percent(interval=None)

        # 암호화 성능 측정 시작
        start_time = time.time()
        process = psutil.Process(os.getpid())
        start_cpu = process.cpu_percent(interval=None)
        start_memory = process.memory_info().rss

        # 암호화
        encrypt_cmd = f"python3 NTRU.py -k NTRU_key_level{level} -eF message.txt -O enc_level{level}.dat"
        subprocess.run(encrypt_cmd, shell=True, input=message.encode())

        # 암호화 성능 측정 종료
        end_memory = process.memory_info().rss
        end_time = time.time()
        #dec_cpu_usage = process.cpu_percent(interval=None) - start_cpu
        enc_cpu_usage = process.cpu_percent(interval=None)
        enc_memory_usage = end_memory - start_memory
        enc_time_usage = end_time - start_time

        time.sleep(5)

        # 복호화
        decrypt_cmd = f"python3 NTRU.py -k NTRU_key_level{level} -dF enc_level{level}.dat -O decoded_level{level}.dat"
        subprocess.run(decrypt_cmd, shell=True)

        # 복호화된 메시지 확인
        with open(f"decoded_level{level}.dat", "r") as f:
            decrypted_message = f.read()

        if decrypted_message == message:
            print(f"Decryption successful at security level {level}.")
            print(f"LEVEL: {level} => CPU usage for Key Gen: {key_gen_cpu_usage}%, Time for Key Gen: {key_gen_time_usage} seconds")
            print(f"LEVEL: {level} => CPU usage for encryption: {enc_cpu_usage}%, Time for encryption: {enc_time_usage} seconds")
        else:
            print(f"Decryption failed at security level {level}.")


security_levels = [80, 112, 128, 160, 192, 256]
run_ntru_operations(security_levels)
