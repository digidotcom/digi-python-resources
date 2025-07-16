# Copyright (c) 2025, Digi International, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import socket
import argparse
import threading


PORT = 9750


def receiver(sock):
    """
    Background thread: receive and print incoming UDP datagrams.
    """
    while True:
        try:
            data, address = sock.recvfrom(1024)
            print("Received from [%s]:%s >> %s\n> " % (
                address[0], address[1], data.decode().rstrip()),
                  end='', flush=True)
        except OSError as e:
            print("Receive error: %s" % e)

def main():
    print("---------------------------------------+")
    print(" | XBee Hive Wi-SUN Get Started Sample |")
    print(" +-------------------------------------+\n")

    parser = argparse.ArgumentParser(
        description='Simple IPv6 UDP socket client')
    parser.add_argument('-a', '--address', required=True,
                        help='IPv6 address of the server')
    args = parser.parse_args()

    # Create an IPv6 UDP socket.
    server = (args.address, PORT)
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    s.bind(('::', PORT))

    # Start receiver thread.
    thread = threading.Thread(target=receiver, args=(s,), daemon=True)
    thread.start()

    print("\nType a message and hit Enter to send it to [%s]:%s." % (
        args.address, PORT))
    try:
        while True:
            # Read a line from stdin and send it as a UDP datagram.
            line = input("> ")
            if not line:
                print("Please, enter some data to send to [%s]:%s." % (
                    args.address, PORT))
                continue

            try:
                s.sendto(line.encode(), server)
            except OSError as e:
                print("Error sending data: %s" % e)
    except KeyboardInterrupt:
        print('\nInterrupted by user, closing...')
    finally:
        s.close()

if __name__ == '__main__':
    main()
