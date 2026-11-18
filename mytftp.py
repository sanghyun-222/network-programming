import socket
import argparse

# 기본 설정
DEFAULT_PORT = 69
BLOCK_SIZE = 512
TIME_OUT = 1.0
MAX_TRY = 5

# TFTP 명령어 번호
OPCODE = {
    'RRQ': 1,
    'WRQ': 2,
    'DATA': 3,
    'ACK': 4,
    'ERROR': 5
}


# 파일 다운로드
def do_download(server_ip, server_port, filename):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(TIME_OUT)

    server_address = (server_ip, server_port)

    # RRQ 요청 메시지 생성
    rrq_message = (
        OPCODE['RRQ'].to_bytes(2, 'big') +
        filename.encode('utf-8') +
        b'\x00octet\x00'
    )

    expected_block = 1
    last_ack = 0
    retry = 0

    try:
        sock.sendto(rrq_message, server_address)
        print('RRQ request sent:', filename)

        with open(filename, 'wb') as file:

            while True:

                try:
                    message, address = sock.recvfrom(516)
                    retry = 0

                except socket.timeout:
                    retry += 1

                    if retry > MAX_TRY:
                        print('Error: Server response timeout.')
                        return

                    print('Timeout. Retry:', retry)

                    if last_ack == 0:
                        sock.sendto(rrq_message, server_address)
                    else:
                        ack_message = (
                            OPCODE['ACK'].to_bytes(2, 'big') +
                            last_ack.to_bytes(2, 'big')
                        )
                        sock.sendto(ack_message, server_address)

                    continue

                # 첫 번째 DATA를 받으면 서버의 통신 포트로 변경
                server_address = address

                opcode = int.from_bytes(message[0:2], 'big')

                if opcode == OPCODE['DATA']:

                    if len(message) < 4:
                        print('Error: Invalid DATA message.')
                        return

                    block_number = int.from_bytes(message[2:4], 'big')
                    data = message[4:]

                    if block_number == expected_block:

                        file.write(data)

                        # ACK 메시지 생성 및 전송
                        ack_message = (
                            OPCODE['ACK'].to_bytes(2, 'big') +
                            block_number.to_bytes(2, 'big')
                        )

                        sock.sendto(ack_message, server_address)

                        print('Received block:', block_number)

                        last_ack = block_number
                        expected_block = (expected_block + 1) % 65536

                        if len(data) < BLOCK_SIZE:
                            print('Download complete!')
                            break

                    elif block_number == last_ack:

                        # 중복 DATA에 이전 ACK 재전송
                        ack_message = (
                            OPCODE['ACK'].to_bytes(2, 'big') +
                            last_ack.to_bytes(2, 'big')
                        )

                        sock.sendto(ack_message, server_address)

                elif opcode == OPCODE['ERROR']:

                    if len(message) < 5:
                        print('Error: Invalid ERROR message.')
                        return

                    error_code = int.from_bytes(message[2:4], 'big')
                    error_message = message[4:-1].decode(
                        'utf-8', errors='replace'
                    )

                    print('TFTP Error:', error_code, error_message)
                    return

                else:
                    print('Error: Unexpected message:', opcode)
                    return

    except OSError as e:
        print('Error:', e)

    finally:
        sock.close()


# 파일 업로드
def do_upload(server_ip, server_port, filename):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(TIME_OUT)

    server_address = (server_ip, server_port)

    try:
        file = open(filename, 'rb')

    except OSError:
        print('Error: File not found:', filename)
        sock.close()
        return

    try:
        # WRQ 요청 메시지 생성
        wrq_message = (
            OPCODE['WRQ'].to_bytes(2, 'big') +
            filename.encode('utf-8') +
            b'\x00octet\x00'
        )

        sock.sendto(wrq_message, server_address)
        print('WRQ request sent:', filename)

        # 서버의 ACK 0 응답 대기
        retry = 0

        while True:
            try:
                message, address = sock.recvfrom(516)
                break

            except socket.timeout:
                retry += 1

                if retry > MAX_TRY:
                    print('Error: Server response timeout.')
                    return

                print('Timeout. Retry:', retry)
                sock.sendto(wrq_message, server_address)

        server_address = address

        opcode = int.from_bytes(message[0:2], 'big')

        if opcode == OPCODE['ERROR']:
            print('Server error:', message[4:-1].decode(
                'utf-8', errors='replace'))
            return

        if len(message) < 4:
            print('Error: Invalid ACK message.')
            return

        block_number = int.from_bytes(message[2:4], 'big')

        if opcode != OPCODE['ACK'] or block_number != 0:
            print('Error: Invalid ACK response.')
            return

        print('ACK 0 received.')

        # 파일 데이터를 512바이트씩 전송
        block_number = 1

        while True:

            data = file.read(BLOCK_SIZE)

            data_message = (
                OPCODE['DATA'].to_bytes(2, 'big') +
                block_number.to_bytes(2, 'big') +
                data
            )

            retry = 0

            while True:
                sock.sendto(data_message, server_address)

                try:
                    message, address = sock.recvfrom(516)

                    if address != server_address:
                        continue

                    break

                except socket.timeout:
                    retry += 1

                    if retry > MAX_TRY:
                        print('Error: Server response timeout.')
                        return

                    print('Timeout. Retry:', retry)

            opcode = int.from_bytes(message[0:2], 'big')

            if opcode == OPCODE['ERROR']:
                print('Server error:', message[4:-1].decode(
                    'utf-8', errors='replace'))
                return

            if len(message) < 4:
                print('Error: Invalid ACK message.')
                return

            ack_number = int.from_bytes(message[2:4], 'big')

            if opcode != OPCODE['ACK'] or ack_number != block_number:
                print('Error: Invalid ACK response.')
                return

            print('ACK received:', ack_number)

            # 마지막 데이터 블록 확인
            if len(data) < BLOCK_SIZE:
                print('Upload complete!')
                break

            block_number = (block_number + 1) % 65536

    except OSError as e:
        print('Error:', e)

    finally:
        file.close()
        sock.close()


# 메인 프로그램
def main():

    parser = argparse.ArgumentParser(description='TFTP Client')

    parser.add_argument('host', help='Server IP address')

    parser.add_argument('-p', '--port', type=int,
                        default=DEFAULT_PORT, help='Server port')

    parser.add_argument('operation', choices=['get', 'put'],
                        help='get or put')

    parser.add_argument('filename', help='File name')

    args = parser.parse_args()

    if args.operation == 'get':
        do_download(args.host, args.port, args.filename)

    elif args.operation == 'put':
        do_upload(args.host, args.port, args.filename)


if __name__ == "__main__":
    main()
